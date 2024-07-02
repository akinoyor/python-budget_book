import tkinter as tk
import sys
WINDOW_SIZE="400x300"

def input_window():
    input_window = tk.Tk()
    input_window.title('入力')
    input_window.geometry(WINDOW_SIZE)

    exit_button = tk.Button(input_window, text='閉じる', command=input_window.destroy)
    exit_button.pack(fill='x', side='bottom')
    input_window.mainloop()

def totalling_window():
    totalling_window = tk.Tk()
    totalling_window.title('集計')
    totalling_window.geometry(WINDOW_SIZE)

    exit_button = tk.Button(totalling_window, text='閉じる', command=totalling_window.destroy)
    exit_button.pack(fill='x', side='bottom')
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


