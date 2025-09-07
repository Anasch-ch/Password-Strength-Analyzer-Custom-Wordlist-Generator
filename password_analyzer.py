import argparse
from zxcvbn import zxcvbn
import itertools

def analyze_password(password):
    result = zxcvbn(password)
    print(f"\nPassword: {password}")
    print(f"Strength Score (0-4): {result['score']}")
    print(f"Crack Time: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    print("Suggestions:", result["feedback"]["suggestions"])

def generate_wordlist(name, date, pet, output_file):
    patterns = [name, date, pet]
    patterns = [p for p in patterns if p]

    wordlist = set()

    # Basic combinations
    for p in patterns:
        wordlist.add(p)
        wordlist.add(p.lower())
        wordlist.add(p.upper())
        wordlist.add(p.capitalize())

    # Leetspeak variations
    leet_map = str.maketrans("aeios", "43105")
    for p in list(wordlist):
        wordlist.add(p.translate(leet_map))

    # Append years
    for p in list(wordlist):
        for year in ["2023", "2024", "123", "321"]:
            wordlist.add(p + year)

    with open(output_file, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    print(f"\nWordlist generated → {output_file} ({len(wordlist)} entries)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password Strength Analyzer & Wordlist Generator")
    parser.add_argument("--password", help="Password to analyze")
    parser.add_argument("--name", help="Name input for wordlist", default="")
    parser.add_argument("--date", help="Date input for wordlist", default="")
    parser.add_argument("--pet", help="Pet input for wordlist", default="")
    parser.add_argument("--output", help="Output wordlist file", default="wordlist.txt")

    args = parser.parse_args()

    if args.password:
        analyze_password(args.password)

    if args.name or args.date or args.pet:
        generate_wordlist(args.name, args.date, args.pet, args.output)
