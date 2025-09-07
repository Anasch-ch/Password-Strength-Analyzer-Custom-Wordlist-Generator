import tkinter as tk
from tkinter import messagebox, filedialog
from zxcvbn import zxcvbn

def analyze_password():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showwarning("Input Error", "Enter a password to analyze")
        return
    result = zxcvbn(pwd)
    result_label.config(text=f"Score: {result['score']}\n"
                             f"Crack Time: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")

def generate_wordlist():
    name = name_entry.get()
    date = date_entry.get()
    pet = pet_entry.get()

    if not (name or date or pet):
        messagebox.showwarning("Input Error", "Enter at least one input")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not file_path:
        return

    patterns = [name, date, pet]
    wordlist = set(patterns)

    leet_map = str.maketrans("aeios", "43105")
    for p in list(wordlist):
        wordlist.add(p.translate(leet_map))

    for p in list(wordlist):
        for year in ["2023", "2024", "123", "321"]:
            wordlist.add(p + year)

    with open(file_path, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    messagebox.showinfo("Success", f"Wordlist saved → {file_path}")

root = tk.Tk()
root.title("Password Strength Analyzer")

tk.Label(root, text="Enter Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Analyze", command=analyze_password).pack()
result_label = tk.Label(root, text="")
result_label.pack()

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Date:").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Pet:").pack()
pet_entry = tk.Entry(root)
pet_entry.pack()

tk.Button(root, text="Generate Wordlist", command=generate_wordlist).pack()

root.mainloop()

