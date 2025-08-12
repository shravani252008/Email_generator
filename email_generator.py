import tkinter as tk
import random
import string

def generate_email():
    username_input = entry_username.get()
    if not username_input:
        label_result.config(text="Please enter a username.")
        return

    random_number = str(random.randint(100, 999)) 
    
    generated_email = username_input + random_number + "@gmail.com"
    label_result.config(text="Generated Email: " + generated_email)

root = tk.Tk()
root.title("Email Generator")

label_username = tk.Label(root, text="Enter Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root, width=40)
entry_username.pack(pady=5)

button_generate = tk.Button(root, text="Generate Email", command=generate_email)
button_generate.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=5)

root.mainloop()