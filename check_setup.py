#!/usr/bin/env python3
"""
Setup verification tool for Telegram Terminal Client
Run this to check if everything is configured correctly
"""

import sys
import os
from colorama import init, Fore, Style

init(autoreset=True)

def check_python_version():
    """Check if Python version is 3.7+"""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}", end=" ")
    
    if version.major >= 3 and version.minor >= 7:
        print(f"{Fore.GREEN}✓")
        return True
    else:
        print(f"{Fore.RED}✗ (Need 3.7+)")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    packages = [
        ('telethon', 'Telethon'),
        ('dotenv', 'python-dotenv'),
        ('colorama', 'Colorama')
    ]
    
    all_ok = True
    for module, name in packages:
        try:
            __import__(module)
            print(f"📦 {name}: {Fore.GREEN}✓ Installed")
        except ImportError:
            print(f"📦 {name}: {Fore.RED}✗ Missing")
            all_ok = False
    
    return all_ok

def check_env_file():
    """Check if .env file exists and is configured"""
    env_path = '.env'
    
    if not os.path.exists(env_path):
        print(f"📄 .env file: {Fore.RED}✗ Not found")
        print(f"\n{Fore.YELLOW}Create .env file:")
        print(f"{Fore.WHITE}  1. Copy .env.example to .env")
        print(f"{Fore.WHITE}  2. Get credentials from https://my.telegram.org")
        print(f"{Fore.WHITE}  3. Fill in API_ID, API_HASH, PHONE_NUMBER")
        return False
    
    print(f"📄 .env file: {Fore.GREEN}✓ Exists")
    
    # Read and check contents
    with open(env_path, 'r') as f:
        content = f.read()
    
    required_vars = ['API_ID', 'API_HASH', 'PHONE_NUMBER']
    missing = []
    placeholder = []
    
    for var in required_vars:
        if var not in content:
            missing.append(var)
        elif 'your_' in content.lower() or 'here' in content.lower():
            # Check if it's still a placeholder
            for line in content.split('\n'):
                if line.startswith(var) and ('your_' in line.lower() or 'here' in line.lower()):
                    placeholder.append(var)
                    break
    
    if missing:
        print(f"   {Fore.RED}✗ Missing variables: {', '.join(missing)}")
        return False
    
    if placeholder:
        print(f"   {Fore.YELLOW}⚠ Placeholder values detected: {', '.join(placeholder)}")
        print(f"   {Fore.YELLOW}   Please replace with real values from https://my.telegram.org")
        return False
    
    print(f"   {Fore.GREEN}✓ All variables configured")
    return True

def check_file_structure():
    """Check if all required files exist"""
    required_files = [
        'main.py',
        'config.py',
        'requirements.txt',
        '.env.example'
    ]
    
    all_ok = True
    for file in required_files:
        if os.path.exists(file):
            print(f"📁 {file}: {Fore.GREEN}✓")
        else:
            print(f"📁 {file}: {Fore.RED}✗ Missing")
            all_ok = False
    
    return all_ok

def main():
    """Run all checks"""
    print(f"{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}  🔍 Telegram Terminal Client - Setup Verification")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    results = []
    
    print(f"{Fore.CYAN}Checking Python environment...")
    results.append(check_python_version())
    print()
    
    print(f"{Fore.CYAN}Checking dependencies...")
    results.append(check_dependencies())
    print()
    
    print(f"{Fore.CYAN}Checking file structure...")
    results.append(check_file_structure())
    print()
    
    print(f"{Fore.CYAN}Checking configuration...")
    results.append(check_env_file())
    print()
    
    # Summary
    print(f"{Fore.CYAN}{'='*60}")
    if all(results):
        print(f"{Fore.GREEN}✓ All checks passed! You're ready to run the app.")
        print(f"\n{Fore.WHITE}Run: {Fore.GREEN}python3 main.py")
    else:
        print(f"{Fore.RED}✗ Some checks failed. Please fix the issues above.")
        print(f"\n{Fore.WHITE}Quick fixes:")
        if not results[1]:  # Dependencies
            print(f"  {Fore.YELLOW}Install dependencies: {Fore.WHITE}pip3 install -r requirements.txt")
        if not results[3]:  # Config
            print(f"  {Fore.YELLOW}Setup .env: {Fore.WHITE}cp .env.example .env")
            print(f"  {Fore.YELLOW}Get API keys: {Fore.WHITE}https://my.telegram.org")
    
    print(f"{Fore.CYAN}{'='*60}\n")
    
    return 0 if all(results) else 1

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Check cancelled by user.")
        sys.exit(1)

