## Password-Strength-Analyzer-Custom-Wordlist-Generator
# “Weak passwords are one of the biggest security risks. I wanted to create a tool that both evaluates password strength and generates custom wordlists for penetration testing/red-team use.”

A Python tool to analyze password strength (using zxcvbn/entropy) and generate custom 
wordlists from user-provided information (names, dates, pets, etc.). 
Exports `.txt` lists for use with John/Hashcat.

✅ CLI + GUI (Tkinter)  
✅ Supports leetspeak, year ranges, suffixes  
✅ Great for security training and red-team (authorized only)

## Objectives

Analyze password strength (zxcvbn / entropy fallback).

Generate wordlists from user info (names, pets, dates, etc.).

Support patterns (leet, case, years, suffixes).

Export .txt wordlists compatible with John/Hashcat.

Provide CLI + optional GUI.

## Tools & Libraries

Python 3.10+

argparse (CLI)

NLTK (tokenization, stopwords)

Steps to Use the Tool
1. Clone or Download the Repository
2. git clone https://github.com/Anasch-ch/password-strength-analyzer.git
cd password-strength-analyzer

Set Up Python Environment

Make sure Python 3.8+ is installed.
Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
pip install zxcvbn nltk tkinter argparse


Run the Tool

You can run it in CLI mode or GUI mode.

#CLI Mode

python password_analyzer.py --password "MyP@ssw0rd" --name "John" --date "1995" --pet "Rocky" --output wordlist.txt

--password → password to analyze.

--name, --date, --pet → optional inputs for wordlist generation.

--output → save the wordlist to a .txt file.

Example Output:

Password: MyP@ssw0rd
Strength Score (0-4): 3
Crack Time (offline fast hash): 3 hours
Suggestions: Add more unique characters

Wordlist generated → wordlist.txt (45 entries)



#GUI Mode (Tkinter)

Simply run:
python gui_app.py

You’ll see a window where you can:

Enter a password to check its strength.

Provide personal info (name, date, pet).

Generate and export a wordlist.

