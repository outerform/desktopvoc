import tkinter as tk
import json
import random
from datetime import datetime
import time

class FloatingVocabulary:
    def __init__(self):
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("单词学习")
        
        # 设置窗口属性
        self.root.attributes('-topmost', True)  # 窗口置顶
        self.root.overrideredirect(True)  # 无边框窗口
        self.root.geometry('300x180+1000+100')  # 设置窗口大小和位置
        
        # 设置窗口背景色
        self.root.configure(bg='#f0f0f0')
        
        # 创建标题栏框架
        self.title_bar = tk.Frame(
            self.root, 
            bg='#2c3e50', 
            height=30
        )
        self.title_bar.pack(fill=tk.X)
        self.title_bar.pack_propagate(False)
        
        # 标题文本
        self.title_label = tk.Label(
            self.title_bar,
            text="每日单词",
            bg='#2c3e50',
            fg='white',
            font=('Arial', 10)
        )
        self.title_label.pack(side=tk.LEFT, padx=10)
        
        # 关闭按钮
        self.close_button = tk.Button(
            self.title_bar,
            text="×",
            command=self.root.quit,
            font=('Arial', 12),
            bd=0,
            bg='#2c3e50',
            fg='white',
            activebackground='#e74c3c',
            activeforeground='white'
        )
        self.close_button.pack(side=tk.RIGHT)
        
        
        # 创建内容框架
        self.content_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        

        # 单词标签
        self.word_label = tk.Label(
            self.content_frame,
            text="Loading...",
            font=('Arial', 16, 'bold'),
            wraplength=280,
            bg='#f0f0f0'
        )
        self.word_label.pack(pady=10)
        
        # 释义标签
        self.meaning_label = tk.Label(
            self.content_frame,
            text="",
            font=('Arial', 12),
            wraplength=280,
            bg='#f0f0f0'
        )
        self.meaning_label.pack(pady=5)
        
        # 刷新按钮
        self.refresh_button = tk.Button(
            self.content_frame,
            text="刷新",
            command=self.update_word,
            font=('Arial', 10),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white'
        )
        self.refresh_button.pack(pady=5)  # 添加这行来显示按钮
        # 绑定拖动事件到标题栏
        self.title_bar.bind('<Button-1>', self.start_move)
        self.title_bar.bind('<B1-Motion>', self.on_move)
        self.title_label.bind('<Button-1>', self.start_move)
        self.title_label.bind('<B1-Motion>', self.on_move)
        
        # 加载单词数据
        self.load_vocabulary()
        
        # 启动定时器
        self.update_word()
    
    def load_vocabulary(self):
        try:
            with open('data.json', 'r', encoding='utf-8') as f:
                self.vocabulary = json.load(f)
        except FileNotFoundError:
            self.vocabulary = [
                {"word": "example", "meaning": "示例"},
                {"word": "vocabulary", "meaning": "词汇"}
            ]
            
    def update_word(self):
        # 随机选择一个单词
        word_data = random.choice(self.vocabulary)
        self.word_label.config(text=word_data["word"])
        self.meaning_label.config(text=word_data["meaning"])
        
        # 每60秒更新一次
        self.root.after(60000, self.update_word)
    
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FloatingVocabulary()
    app.run()