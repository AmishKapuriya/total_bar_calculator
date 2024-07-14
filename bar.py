import tkinter as tk
from tkinter import messagebox, Label


def calculate_bars():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        cover = float(entry_cover.get())
        spacing = float(entry_spacing.get())
        if length > 300:
            if width < 300:
                along_width = 2.0
                along_length = round(((length - (2 * cover)) / spacing) + 1, 0)
                total_bars = round(2 * ((along_length) + (along_width - 2)), 0)
                empty_label_1.config(text=str(along_length) + ' bars on each side')
                empty_label_2.config(text=str(along_width) + ' bars on each side')

                empty_label.config(text='Total: ' + str(total_bars) + ' bars')

            else:
                along_length = round(((length - (2 * cover)) / spacing) + 1, 0)
                along_width = round(((width - (2 * cover)) / spacing) + 1, 0)
                total_bars = round(2 * ((along_length) + (along_width - 2)), 0)
                empty_label_1.config(text=str(along_length) + ' bars on each side')
                empty_label_2.config(text=str(along_width) + ' bars on each side')

                empty_label.config(text='Total: ' + str(total_bars) + ' bars')
        else:
            if width < 300:
                along_width = 2.0
                along_length = 2.0
                total_bars = round(2 * ((along_length) + (along_width - 2)), 0)
                empty_label_1.config(text=str(along_length) + ' bars on each side')
                empty_label_2.config(text=str(along_width) + ' bars on each side')

                empty_label.config(text='Total: ' + str(total_bars) + ' bars')

            else:
                along_length = 2.0
                along_width = round(((width - (2 * cover)) / spacing) + 1, 0)
                total_bars = round(2 * ((along_length) + (along_width - 2)), 0)
                empty_label_1.config(text=str(along_length) + ' bars on each side')
                empty_label_2.config(text=str(along_width) + ' bars on each side')

                empty_label.config(text='Total: ' + str(total_bars) + ' bars')

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for length and width.")


def on_enter(next_widget):
    next_widget.focus_set()


# Create the main window
root = tk.Tk()
root.title("Bar Calculator")
root.geometry('600x300')

# Create and place the labels and entries for length and width
label_cover = tk.Label(root, text="Cover:", fg='blue', font=('Work Sans', 16))
label_cover.grid(row=0, column=0, padx=10, pady=10)
entry_cover = tk.Entry(root, fg='blue', font=('Work Sans', 14))
entry_cover.grid(row=0, column=1, padx=10, pady=10)
entry_cover.bind("<Return>", lambda event: on_enter(entry_spacing))

label_spacing = tk.Label(root, text="Spacing:", fg='blue', font=('Work Sans', 16))
label_spacing.grid(row=1, column=0, padx=10, pady=10)
entry_spacing = tk.Entry(root, fg='blue', font=('Work Sans', 14))
entry_spacing.grid(row=1, column=1, padx=10, pady=10)
entry_spacing.bind("<Return>", lambda event: on_enter(entry_length))

label_length = tk.Label(root, text="Length:", fg='blue', font=('Work Sans', 16))
label_length.grid(row=2, column=0, padx=10, pady=10)
entry_length = tk.Entry(root, fg='blue', font=('Work Sans', 14))
entry_length.grid(row=2, column=1, padx=10, pady=10)
empty_label_1 = Label(root, fg='green', font=('Work Sans', 14))
empty_label_1.grid(row=2, column=2, padx=10, pady=10)
entry_length.bind("<Return>", lambda event: on_enter(entry_width))

label_width = tk.Label(root, text="Width:", fg='blue', font=('Work Sans', 16))
label_width.grid(row=3, column=0, padx=10, pady=10)
entry_width = tk.Entry(root, fg='blue', font=('Work Sans', 14))
entry_width.grid(row=3, column=1, padx=10, pady=10)
empty_label_2 = Label(root, fg='green', font=('Work Sans', 14))
empty_label_2.grid(row=3, column=2, padx=10, pady=10)

empty_label = Label(root, fg='green', font=('Work Sans', 14))
empty_label.grid(row=5, column=1, padx=10, pady=20)

entry_width.bind("<Return>", lambda event: on_enter(button_calculate))

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate_bars)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
