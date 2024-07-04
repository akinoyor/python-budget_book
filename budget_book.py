import tkinter as tk
from tkinter import messagebox
import re
import sys
import pickle
from pathlib import Path
import os
import datetime

dir = os.path.dirname(__file__)
file_name = 'pickled.pkl'
file_path = os.path.join(dir, file_name)
WINDOW_SIZE="500x200"
class Total:
    def __init__(self):  
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                try:
                    records = pickle.load(f)
                    self.records = records
                except EOFError:
                    self.records = []
        else:
            with open(file_path, 'wb') as f:
                self.records = []
                pickle.dump(self.records, f)

    def add_record(self, record):
        self.records.append(record)
    def write_records(self):
        with open(file_path, 'wb') as f:
            pickle.dump(self.records, f)
   
        # 中身確認用あとで消す
    def print_records(self):
        for record in self.records:
            print(record)
class Record:
    def __init__(self, date, amount, content):
        self.date = date
        self.amount = amount
        self.content = content

    # 内容確認用　あとで消す
    def __str__(self):
        return f"日付: {self.date}, 金額: {self.amount}, 内容: {self.content}"

def input_window_boot():
    global date_entry, amount_entry, content_entry, input_window, total

    total = Total()
    input_window = tk.Tk()
    input_window.title('入力')
    input_window.geometry(WINDOW_SIZE)
    entry_frame = tk.Frame(input_window)
    input_buttons_frame = tk.Frame(input_window)
    entry_frame.grid(row=0, sticky=tk.EW)
    input_buttons_frame.grid(row=1, column=0, pady=10,sticky=tk.EW)
    input_window.grid_columnconfigure(0, weight=1)

    date_label = tk.Label(entry_frame, text='日付')
    date_entry = tk.Entry(entry_frame)
    content_label = tk.Label(entry_frame, text='内容')
    content_entry = tk.Entry(entry_frame)
    amount_label = tk.Label(entry_frame, text='金額')
    amount_entry = tk.Entry(entry_frame)
    entry_button = tk.Button(input_buttons_frame, text='追加', command=input)
    close_button = tk.Button(input_buttons_frame, text='閉じる', command=input_window.destroy)

    date_label.grid(row=0, column=0, padx=5)
    date_entry.grid(row=1, column=0, padx=5)
    content_label.grid(row=0, column=1, sticky=tk.EW)
    content_entry.grid(row=1, column=1, sticky=tk.EW)
    amount_label.grid(row=0, column=2, padx=5, sticky=tk.EW)
    amount_entry.grid(row=1, column=2, padx=5, sticky=tk.EW)
    entry_frame.grid_columnconfigure(1, weight=3, minsize='200')
    entry_frame.grid_columnconfigure(2, weight=1, minsize='100')
    entry_button.grid(row=0, column=0, padx=130)
    close_button.grid(row=0, column=1)

    input_window.mainloop()

def input():
    date = date_entry.get()
    
    amount = amount_entry.get()
    content = content_entry.get()
    
    if not date or not amount or not content:
        messagebox.showerror('エラー', '全てのフィールドを入力してください')
        input_window.lift()
        return
    if not re.match(r'^\d{4}/\d{2}/\d{2}$', date):
        messagebox.showerror('エラー', '日付はYYYY/MM/DD形式で入力してください')
        input_window.lift()
        return
    if not amount.isdigit():
        messagebox.showerror('エラー', '金額は数字で入力してください')
        input_window.lift()
        return
    
    date_format = datetime.datetime.strptime(date, '%Y/%m/%d').date()
    new_record = Record(date_format, amount, content) 
    print('-----------')
    total.add_record(new_record)
    total.print_records()
    total.write_records()

def totalling_window():
    totalling_window = tk.Tk()
    totalling_window.title('集計')
    totalling_window.geometry(WINDOW_SIZE)

    close_button = tk.Button(totalling_window, text='閉じる', command=totalling_window.destroy)
    close_button.pack(fill='x', side='bottom')
    totalling_window.mainloop()

root = tk.Tk()
root.title('家計簿アプリ')
root.geometry(WINDOW_SIZE)

input_button = tk.Button(root, text='入力', command=input_window_boot)
totalling_button = tk.Button(root, text='集計', command=totalling_window)
exit_button = tk.Button(root, text='exit', command=sys.exit)

exit_button.pack(fill='x', side='bottom')
input_button.pack(fill='x')
totalling_button.pack(fill='x')

root.mainloop()
