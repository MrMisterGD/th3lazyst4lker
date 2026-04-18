#!/usr/bin/env python3
import subprocess
import sys
import os
import argparse
import shutil
import platform

IS_WINDOWS = platform.system() == "Windows"
PYTHON_BIN = "python" if IS_WINDOWS else "python3"

# I forgot the purpose of this to be honest
class C:
    RED    = "\033[91m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    WHITE  = "\033[97m"
    DIM    = "\033[2m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"

BANNER = f"""{C.BOLD}
*******************************************************************
*                                                                 *
*                   Th3LazySt4lker v0.3                           *
*                      Coded by Mr. Mister GD                     *
*                                                                 *
*******************************************************************
{C.RESET}
"""

# just helpers
def resolve_bin(name):
    return shutil.which(name) or ""

def run_cmd(cmd):
    try:
        print(f"{C.DIM}$ {' '.join(cmd)}{C.RESET}")
        subprocess.run(cmd, shell=IS_WINDOWS)
    except Exception as e:
        print(f"{C.RED}ERROR: {e}{C.RESET}")

def run_in_new_terminal(cmd_list):
    try:
        if IS_WINDOWS:
            subprocess.Popen(["cmd.exe", "/k"] + cmd_list)
        else:
            subprocess.Popen(["x-terminal-emulator", "-e"] + cmd_list)
    except Exception as e:
        print(f"{C.RED}Failed to open new terminal: {e}{C.RESET}")

# the intensity settings
def apply_intensity(cmd, tool, intensity):
    if intensity == 1:  # HIGH
        if tool == "maigret":
            cmd += ["-a", "-n", "20"]
        elif tool == "sherlock":
            cmd += ["--timeout", "10"]
    elif intensity == 2:  # MEDIUM
        if tool == "maigret":
            cmd += ["-n", "10"]
    elif intensity == 3:  # LOW
        if tool == "maigret":
            cmd += ["-n", "5"]
    return cmd

# tools :D
def run_maigret(u, intensity):
    b = resolve_bin("maigret")
    if not b:
        print("[-] Maigret not installed")
        return
    cmd = [b, u]
    cmd = apply_intensity(cmd, "maigret", intensity)
    run_cmd(cmd)

def run_sherlock(u, intensity):
    b = resolve_bin("sherlock")
    if not b:
        print("[-] Sherlock not installed")
        return
    cmd = [b, u]
    cmd = apply_intensity(cmd, "sherlock", intensity)
    run_cmd(cmd)

def run_socialscan(u):
    b = resolve_bin("socialscan")
    if not b:
        print("[-] Socialscan not installed")
        return
    run_cmd([b, u])

def run_holehe(e):
    b = resolve_bin("holehe")
    if not b:
        print("[-] Holehe not installed")
        return
    run_cmd([b, e])

def run_harvester(target):
    b = resolve_bin("theHarvester")

    if b:
        print("[+] Launching theHarvester in new terminal")
        run_in_new_terminal([b, "-d", target, "-b", "all"])
    else:
        print("[-] theHarvester not found in PATH")

def run_reconng():
    b = resolve_bin("recon-ng")

    if b:
        print("[+] Opening Recon-ng in new terminal")
        run_in_new_terminal([b])
    else:
        print("[-] recon-ng not found in PATH")

def run_spiderfoot():
    b = resolve_bin("spiderfoot")

    if b:
        print("[+] Opening SpiderFoot in new terminal")
        run_in_new_terminal([b])
    else:
        print("[-] SpiderFoot not found in PATH")

# scan stuff
def scan_username(u, intensity):
    print(f"\n[USERNAME] {u}\n")
    run_maigret(u, intensity)
    run_sherlock(u, intensity)
    run_socialscan(u)

def scan_email(e):
    print(f"\n[EMAIL] {e}\n")
    run_holehe(e)
    run_socialscan(e)

    domain = e.split("@")[-1]
    run_harvester(domain)

def scan_name(n):
    print(f"\n[NAME] {n}\n")
    run_reconng()
    run_spiderfoot()

# the tool check I forgot to delete, I stole it from another code but I don't remember from where
def check_tools():
    tools = ["maigret", "sherlock", "socialscan", "holehe", "theHarvester", "recon-ng", "spiderfoot"]
    print("\nTool Status:\n")
    for t in tools:
        print(f"{t:<15} -> {'OK' if resolve_bin(t) else 'MISSING'}")

# Main
def main():
    print(BANNER)

    parser = argparse.ArgumentParser(
        description="Th3LazySt4lker - OSINT Multi Tool",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-u", help="Search by username")
    parser.add_argument("-e", help="Search by email")
    parser.add_argument("-n", help="Search by full name")
    parser.add_argument("-i", type=int, choices=[1,2,3], default=0,
                        help="Intensity level:\n 1 = High\n 2 = Medium\n 3 = Low")
    parser.add_argument("--check-tools", action="store_true", help="Check installed tools")

    args = parser.parse_args()

    if args.check_tools:
        check_tools()
    elif args.u:
        scan_username(args.u, args.i)
    elif args.e:
        scan_email(args.e)
    elif args.n:
        scan_name(args.n)
    else:
        parser.print_help()

    if IS_WINDOWS:
        input("\nPress ENTER to exit...")

if __name__ == "__main__":
    main()