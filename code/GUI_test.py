import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# window
window = ttk.Window(themename="journal")
window.title("Miles to KM converter")
window.geometry("400x150")

# title
title_label = ttk.Label(
    master=window,
    text="Miles to KM converter",
    font="Calibri 24")

title_label.pack()
# input field
input_frame = ttk.Frame(master=window)
entry_int = ttk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=10)

# output
output_string = ttk.StringVar()
output_label = ttk.Label(
    master=window,
    text="Output",
    font="Calibri 24",
    textvariable=output_string)
output_label.pack(pady=10)

## run
window.mainloop()