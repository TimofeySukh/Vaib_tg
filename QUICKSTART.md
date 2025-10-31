# 🚀 Quick Start Guide

## Installation (5 minutes)

### 1. Install dependencies
```bash
pip3 install -r requirements.txt
```

### 2. Get Telegram API credentials
1. Go to: https://my.telegram.org
2. Login with your phone number
3. Open "API development tools"
4. Create app:
   - **App title**: MyTerminalClient
   - **Short name**: terminal
   - **Platform**: **Desktop** ⚠️ Important!
   - **Description**: Terminal client
5. Copy your **API ID** and **API Hash**

### 3. Create .env file
```bash
nano .env
```

Paste this (replace with your values):
```env
API_ID=1234567
API_HASH=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
PHONE_NUMBER=+79161234567
```

**No quotes needed!** Just values.

### 4. Run
```bash
python3 main.py
```

Enter the code Telegram sends you (5 digits, e.g., `12345`)

---

## 🎯 Main Features

| Option | Feature | Description |
|--------|---------|-------------|
| 1 | 📱 Show chats | List all your chats |
| 2 | 📨 Read messages | Read chat history |
| 3 | ✍️ Send message | Send text with formatting |
| 4 | 📎 Send file | Upload photos/documents |
| 5 | 🔍 Search | Find chats by name |
| 6 | ℹ️ Info | Show chat details |
| 7 | 💬 Interactive | Live chat mode (best!) |
| 8 | 🔔 Notifications | Toggle real-time alerts |
| 9 | ❌ Exit | Close app |

---

## 💡 Pro Tips

### Interactive Mode Commands
```
exit            - Leave chat
/help           - Show commands
/info           - Chat info
/file <path>    - Send file
/clear          - Clear screen
/history        - Load more messages
```

### Message Formatting
```
**bold text**           - Bold
__italic text__         - Italic
`code`                  - Monospace
[link text](URL)        - Hyperlink
```

### Keyboard Shortcuts
- `Ctrl+C` - Exit current operation
- `Ctrl+D` - Close interactive mode

---

## 🐛 Troubleshooting

### "Invalid code" error
- Don't enter digits one by one!
- Enter the full 5-digit code (e.g., `12345`)
- Code is in Telegram app, not SMS

### "API_ID required" error
```bash
# Check .env file exists
ls -la .env

# View contents
cat .env

# Should look like:
# API_ID=1234567
# API_HASH=abc123...
# PHONE_NUMBER=+79161234567
```

### Module import errors
```bash
# Reinstall dependencies
pip3 install --upgrade -r requirements.txt
```

### File upload fails
- Use absolute path: `/Users/tim/photo.jpg`
- Not relative: `~/photo.jpg` or `photo.jpg`

---

## 📝 Example Session

```bash
# Start app
python3 main.py

# Output:
# ✓ Successfully logged in as: John
# ✓ Username: @john_doe

# Select option 1 - Show chats
# Select option 7 - Interactive mode
# Enter chat number: 1

# Now you're chatting!
You > Hello! **This is bold**
✓ Message sent!

You > /file /Users/tim/photo.jpg
Caption (optional): Check this out!
✓ File sent successfully!

You > exit
👋 Leaving chat...
```

---

## 🎨 Interface Preview

```
==============================================================
        🚀 Telegram Terminal Client v2.0 🚀
==============================================================

✓ Successfully logged in as: John Doe
✓ Username: @john_doe
✓ User ID: 123456789

==============================================================
  📱 Your Chats
==============================================================

 1. 👤 Alice Smith 🔴 3
    └─ Hey, are you coming today?...
 2. 📢 News Channel
    └─ Breaking: New updates available...
 3. 👥 Work Team 🔴 7
    └─ Meeting at 3 PM tomorrow...
```

---

**That's it! You're ready to chat from the terminal! 🎉**

Need more info? Check `README.md` (English) or `README_RU.md` (Russian)

