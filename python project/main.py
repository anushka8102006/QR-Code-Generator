import tkinter as tk
from tkinter import messagebox
import qrcode

def generate_qr():

    text = entry.get()

    if text == "":
        messagebox.showerror(
            "Error",
            "Please enter text"
        )

    else:

        qr = qrcode.make(text)

        qr.save("my_qr.png")

        messagebox.showinfo(
            "Success",
            "QR Code Saved as my_qr.png"
        )

root = tk.Tk()

root.title("QR Code Generator")

root.geometry("500x350")

root.configure(bg="#1e1e2f")

heading = tk.Label(
    root,
    text="QR Code Generator",
    font=("Arial", 24, "bold"),
    bg="#1e1e2f",
    fg="white"
)

heading.pack(pady=30)


entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 14)
)

entry.pack(pady=20)


generate_btn = tk.Button(
    root,
    text="Generate QR",
    font=("Arial", 14, "bold"),
    bg="#00ffff",
    fg="black",
    padx=20,
    pady=10,
    command=generate_qr
)

generate_btn.pack(pady=30)

root.mainloop()