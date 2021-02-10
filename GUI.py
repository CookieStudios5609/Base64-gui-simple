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
window.title("B64 Decode")
window.resizable(width=False, height=False)
window.configure(bg='#2c2f33')

# frame
entry_frame = tk.Frame(master=window, bg='#696969')
encoded_input_box = tk.Entry(master=entry_frame, width=45, bg='#696969', fg="#d3d3d3")
encoded_input = tk.Label(master=entry_frame, text="Encoded message:", bg='#2c2f33', fg="#d3d3d3")

# buttons
decode_button = tk.Button(master=window, text="\N{White Right-Pointing Triangle}", bg='#99aab5', command=decode)
copy_button = tk.Button(master=window, text='Copy \N{CLIPBOARD}', bg='#2c2f33', fg="#ffffff", command=copy)
exit_button = tk.Button(master=window, text='\N{cross mark}', bg='#2c2f33', fg="red", command=kill)

# key_binds
window.bind('<Escape>', lambda e: window.destroy())

# decoded strings
decoded_title = tk.Label(master=window, text=f"Decoded Message:", bg='#2c2f33', fg="#d3d3d3")
decoded = tk.Label(master=window, bg='#2c2f33', fg="#d3d3d3", text="")


# .grid() stuff
entry_frame.grid(row=0, column=0)
encoded_input_box.grid(row=0, column=1, sticky="w")
encoded_input.grid(row=0, column=0, sticky="w")
decode_button.grid(row=0, column=2, sticky='w')
decoded.grid(row=2, column=0, sticky='nw')
decoded_title.grid(row=1, column=0, sticky='w')
exit_button.grid(row=2, column=4)
copy_button.grid(row=2, column=3)

# has to be here because tk docs said so
window.mainloop()
