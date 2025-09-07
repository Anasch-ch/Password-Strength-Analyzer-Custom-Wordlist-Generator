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

zxcvbn-python (password strength estimation)

tkinter (GUI)

os, itertools, re (core Python)
