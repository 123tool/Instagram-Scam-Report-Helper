import os
import requests
import time
import webbrowser
from colorama import Fore, Style, init
from report_generator import generate_report

init(autoreset=True)

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.MAGENTA + Style.BRIGHT + """
========================================
   INSTAGRAM SCAM REPORT HELPER
========================================
Tool for reporting scam accounts safely
========================================
""")

def check_username(username):
    url = f"https://www.instagram.com/{username}/"
    try:
        r = requests.get(url)
        return r.status_code == 200
    except:
        return False

def choose_reason():
    reasons = [
        "Scam / Fraud",
        "Fake Account",
        "Impersonation",
        "Spam Activity",
        "Harassment"
    ]

    print(Fore.YELLOW + "\nSelect report reason:\n")

    for i, r in enumerate(reasons,1):
        print(Fore.CYAN + f"[{i}] {r}")

    choice = input("\nEnter number: ")

    try:
        return reasons[int(choice)-1]
    except:
        return reasons[0]

def main():

    banner()

    username = input(Fore.GREEN + "Enter Instagram username: @").strip().replace("@","")

    print(Fore.YELLOW + "\nChecking username...\n")
    time.sleep(1)

    if not check_username(username):
        print(Fore.RED + "Username not found.")
        return

    print(Fore.GREEN + "Username valid!")

    country = input("\nCountry of account (example: Indonesia): ")

    reason = choose_reason()

    print(Fore.BLUE + "\nGenerating report file...\n")
    time.sleep(1)

    filepath = generate_report(username,country,reason)

    print(Fore.GREEN + f"Report saved → {filepath}")

    open_page = input("\nOpen official Instagram report page? (y/n): ")

    if open_page.lower() == "y":
        webbrowser.open("https://help.instagram.com/372161259539444")

if __name__ == "__main__":
    main()
