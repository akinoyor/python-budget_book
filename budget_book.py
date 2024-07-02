import tkinter as tk
import sys
WINDOW_SIZE="500x200"

class Record:
    def _init_(self, date, amount, content):
        self.date = date
        self.amount = amount
        self.content = content

def input_window():
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
    amount_label = tk.Label(entry_frame, text='金額')
    amount_entry = tk.Entry(entry_frame)
    content_label = tk.Label(entry_frame, text='内容')
    content_entry = tk.Entry(entry_frame)
    entry_button = tk.Button(input_buttons_frame, text='追加', command=input(date_entry, amount_entry, content_entry))
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

def input(date_entry, amount_entry, content_entry):
    date = date_entry.get()
    amount = amount_entry.get()
    content = content_entry.get()
    print(date,amount,content)

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

input_button = tk.Button(root, text='入力', command=input_window)
totalling_button = tk.Button(root, text='集計', command=totalling_window)
exit_button = tk.Button(root, text='exit', command=sys.exit)

exit_button.pack(fill='x', side='bottom')
input_button.pack(fill='x')
totalling_button.pack(fill='x')

root.mainloop()
