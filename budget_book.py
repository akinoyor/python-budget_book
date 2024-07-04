import tkinter as tk
from tkinter import messagebox
import re
import sys
import pickle
from pathlib import Path
import os
import datetime

today = datetime.datetime.today().date()
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
    # def print_records(self):
    #     for record in self.records:
    #         print(record)
class Record:
    def __init__(self, date, amount, content):
        self.date = date
        self.amount = amount
        self.content = content

    #  内容確認用　あとで消す
    # def __str__(self):
    #     return f"日付: {self.date}, 金額: {self.amount}, 内容: {self.content}"

def input_window_boot():
    global date_entry, amount_entry, content_entry, input_window

    input_window = tk.Tk()
    input_window.title('入力')
    input_window.geometry(WINDOW_SIZE)
    entry_frame = tk.Frame(input_window)
    input_buttons_frame = tk.Frame(input_window)
    entry_frame.grid(row=0, column=0, sticky=tk.EW)
    input_buttons_frame.grid(row=1, column=0, pady=10, sticky=tk.EW)
    input_window.grid_columnconfigure(0, weight=1)

    date_label = tk.Label(entry_frame, text='日付')
    date_entry = tk.Entry(entry_frame)
    date_entry.insert(0, today)
    content_label = tk.Label(entry_frame, text='内容')
    content_entry = tk.Entry(entry_frame)
    amount_label = tk.Label(entry_frame, text='金額')
    amount_entry = tk.Entry(entry_frame)
    entry_button = tk.Button(input_buttons_frame, text='追加', command=input)
    entry_clear_button = tk.Button(input_buttons_frame, text='削除', command=entry_clear)
    close_button = tk.Button(input_buttons_frame, text='閉じる', command=input_window.destroy)

    date_label.grid(row=0, column=0, padx=5)
    date_entry.grid(row=1, column=0, padx=5)
    content_label.grid(row=0, column=1, sticky=tk.EW)
    content_entry.grid(row=1, column=1, sticky=tk.EW)
    amount_label.grid(row=0, column=2, padx=5, sticky=tk.EW)
    amount_entry.grid(row=1, column=2, padx=5, sticky=tk.EW)
    entry_frame.grid_columnconfigure(1, weight=3, minsize='200')
    entry_frame.grid_columnconfigure(2, weight=1, minsize='100')
    entry_button.grid(row=0, column=0)
    entry_clear_button.grid(row=0, column=1)
    close_button.grid(row=0, column=2)
    for i in range(3):
        input_buttons_frame.grid_columnconfigure(i, weight=1)

    input_window.mainloop()

def entry_clear():
    date_entry.delete(0, tk.END)
    date_entry.insert(0, today)
    content_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def input():
    date = date_entry.get()   
    amount = amount_entry.get()
    content = content_entry.get()
    
    if not date or not amount or not content:
        messagebox.showerror('エラー', '全てのフィールドを入力してください')
        input_window.lift()
        return
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        messagebox.showerror('エラー', '日付はYYYY-MM-DD形式で入力してください')
        input_window.lift()
        return
    if not amount.isdigit():
        messagebox.showerror('エラー', '金額は数字で入力してください')
        input_window.lift()
        return
    
    date_format = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    new_record = Record(date_format, amount, content) 
    total.add_record(new_record)
    total.records.sort(key=lambda x: x.date)
    total.write_records()
    entry_clear()

def totalling_input():
    global total_yaer_entry, total_month_entry, totalling_input_window
    totalling_input_window = tk.Tk()
    totalling_input_window.geometry(WINDOW_SIZE)
    totalling_input_window.title('集計月')
    input_frame = tk.Frame(totalling_input_window)
    buttons_frame = tk.Frame(totalling_input_window)

    total_label = tk.Label(input_frame, text='集計する年月を入力してください')
    total_yaer_entry = tk.Entry(input_frame)
    total_yaer_entry.insert(0, today.year)
    total_yera_label = tk.Label(input_frame, text='年')
    total_month_entry = tk.Entry(input_frame)
    total_month_entry.insert(0, str(today.month).zfill(2))
    total_month_label = tk.Label(input_frame, text='月')
    enter_button = tk.Button(buttons_frame, text='決定', command=input_year_month)
    close_button = tk.Button(buttons_frame, text='閉じる', command=totalling_input_window.destroy)

    input_frame.grid(row=0, column=0, sticky=tk.EW)
    total_label.grid(row=0, column=0)
    total_yaer_entry.grid(row=1, column=0)
    total_yera_label.grid(row=1, column=1)
    total_month_entry.grid(row=1, column=2)
    total_month_label.grid(row=1,column=3)
    buttons_frame.grid(row=1, column=0, sticky=tk.EW, pady=10)
    enter_button.grid(row=0, column=0)
    close_button.grid(row=0, column=1)
    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)

    totalling_input_window.mainloop()

def input_year_month():
    year = total_yaer_entry.get()
    month = total_month_entry.get()
    if (not re.match(r'^\d{4}', year)) or (not re.match(r'^\d{2}', month)):
        messagebox.showerror('エラー', '年月はYYYY年MM月で入力してください')
        totalling_input_window.lift()
    
    year = int(year)
    month = int(month)
    totalling_input_window.destroy()
    list = totalling_list_create(year, month)
    totalling_window_boot(list)


def totalling_list_create(year, month):
    global list
    list = []
    for record in total.records:
        if record.date.year == year:
            if record.date.month == month:
                list.append(record)
    return list

def delete_data(id):
    remove_item = list[id]
    list.pop(id)
    for i, record in enumerate(total.records):
        if record == remove_item:
            total.records.pop(i)
            total.write_records()
            break
    update_display(list)

def update_display(list):
    for item in record_list_frame.winfo_children():
        item.destroy()
    record_count = 1
    record_sum = 0
    date_label = tk.Label(record_list_frame, text='日付')
    content_label = tk.Label(record_list_frame, text='内容')
    amount_label = tk.Label(record_list_frame, text='金額')
    date_label.grid(row=0, column=0)
    content_label.grid(row=0, column=1)
    amount_label.grid(row=0, column=2)
    for id, record in enumerate(list):
        record_date_label = tk.Label(record_list_frame, text=record.date)
        record_date_label.grid(row=record_count, column=0)
        record_content_label = tk.Label(record_list_frame, text=record.content)
        record_content_label.grid(row=record_count, column=1)
        record_amount_label = tk.Label(record_list_frame, text=record.amount)
        record_amount_label.grid(row=record_count, column=2)
        button = tk.Button(record_list_frame, text='削除', command=lambda i=id: delete_data(i))
        button.grid(row=record_count, column=3)
        record_count+=1
        record_sum+=int(record.amount)
    print(record_sum)

def totalling_window_boot(list):  
    global record_list_frame
    totalling_window = tk.Tk()
    totalling_window.title('集計')
    totalling_window.geometry(WINDOW_SIZE)
    record_list_frame = tk.Frame(totalling_window)
    buttons_frame = tk.Frame(totalling_window)

    update_display(list)
    close_button = tk.Button(buttons_frame, text='閉じる', command=totalling_window.destroy)

    record_list_frame.grid(row=0, column=0, sticky=tk.EW)
    record_list_frame.grid_columnconfigure(0, weight=1)
    record_list_frame.grid_columnconfigure(1, weight=4)
    record_list_frame.grid_columnconfigure(2, weight=2) 
    buttons_frame.grid(row=1, column=0, sticky=tk.EW)
    close_button.grid(row=0, column=0)
    buttons_frame.grid_columnconfigure(0, weight=1)
    totalling_window.mainloop()

root = tk.Tk()
root.title('家計簿アプリ')
root.geometry(WINDOW_SIZE)
total = Total()

input_button = tk.Button(root, text='入力', command=input_window_boot)
totalling_button = tk.Button(root, text='集計', command=totalling_input)
exit_button = tk.Button(root, text='exit', command=sys.exit)

exit_button.pack(fill='x', side='bottom')
input_button.pack(fill='x')
totalling_button.pack(fill='x')

root.mainloop()
