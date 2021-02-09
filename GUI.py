import tkinter as tk
from tkinter.ttk import *
import base64
import pyperclip


# decoder
def decode():
    if len(encoded_input_box.get()) != 0:
        try:
            user_typed = encoded_input_box.get()
            base64_bytes = user_typed.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            progress.grid(row=1, column=0, pady=0, sticky='e')
            progress.start(interval='8')
            decoded["text"] = message_bytes.decode('ascii')
        except ValueError:
            print('oops')
            decoded["text"] = "This is not a valid message!"


def copy():
    print(decoded['text'])
    pyperclip.copy(decoded['text'])


def kill():
    window.destroy()


# window
window = tk.Tk()
window.title("My Awesome And Totally Secret Super Secret Secret Message Decoder!")
window.resizable(width=False, height=True)

# frame
entry_frame = tk.Frame(master=window)
encoded_input_box = tk.Entry(master=entry_frame, width=50)
encoded_input = tk.Label(master=entry_frame, text="Secret and totally NOT just Base64 message")

# buttons
decode_button = tk.Button(
    master=window,
    text="\N{BLACK DIAMOND}",
    command=decode
)
copy_button = tk.Button(master=window, text='C', command=copy)
exit_button = tk.Button(master=window, text='X', command=kill)

# key_binds
window.bind('<Escape>', lambda e: window.destroy())

# decoded strings
decoded_title = tk.Label(master=window, text="Decoded Message:")
decoded = tk.Label(master=window, text="")

# fake loading bar
progress = Progressbar(length=305, mode='indeterminate', orient='horizontal', phase=1)

# separator next to loading bar
bar = Separator(orient='vertical')

# .grid() stuff
entry_frame.grid(row=0, column=0, padx=0)
decode_button.grid(row=0, column=2, pady=10, padx=10)
decoded.grid(row=1, column=3, padx=15)
decoded_title.grid(row=0, column=3, padx=15)
encoded_input_box.grid(row=0, column=1, sticky="e")
encoded_input.grid(row=0, column=0, sticky="w")
bar.grid(row=1, column=1, padx=10, sticky='e')
exit_button.grid(row=2, column=4)
copy_button.grid(row=2, column=5)

# has to be here because tk docs said so
window.mainloop()
