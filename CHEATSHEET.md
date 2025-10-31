# 📋 Telegram Terminal Client - Cheat Sheet

Quick reference for all commands and features.

---

## ⚡ Quick Start
```bash
pip3 install -r requirements.txt  # Install
nano .env                         # Configure (see .env.example)
python3 main.py                   # Run
```

---

## 🎯 Main Menu Options

| # | Command | Description |
|---|---------|-------------|
| 1 | Show chats | List all chats with unread counts |
| 2 | Read messages | View chat history |
| 3 | Send message | Send text with formatting |
| 4 | Send file | Upload photo/video/document |
| 5 | Search | Find chats by name |
| 6 | Chat info | View user/group details |
| 7 | Interactive | Live chat mode ⭐ |
| 8 | Notifications | Toggle real-time alerts |
| 9 | Exit | Quit app |

---

## 💬 Interactive Mode Commands

```
exit              Exit interactive mode
/help             Show help
/info             Show chat info
/file <path>      Send a file
/clear            Clear screen
/history          Load more messages
```

---

## 📝 Message Formatting

```
**bold**          Bold text
__italic__        Italic text
`code`            Monospace
[text](URL)       Hyperlink
```

---

## 📁 File Sending

```bash
# From menu (option 4)
Enter file path: /Users/tim/photo.jpg
Caption: Optional caption

# From interactive mode
/file /Users/tim/document.pdf
Caption: Optional caption
```

⚠️ **Use absolute paths** (not ~/file.jpg)

---

## 🔍 Search Examples

```
Search query: Alice     # Find user
Search query: @john     # Find by username
Search query: team      # Partial match
```

---

## 🎨 Chat Icons

| Icon | Type | Color |
|------|------|-------|
| 👤 | User | Green |
| 📢 | Channel | Blue |
| 👥 | Group | Yellow |
| 🔴 | Unread | Red |

---

## 🔔 Notifications

```
Option 8:  Toggle ON/OFF
When ON:   See new messages while in menu
When OFF:  Silent mode
```

---

## ⌨️ Keyboard Shortcuts

```
Ctrl+C    Cancel/Interrupt
Ctrl+D    Exit input/EOF
Ctrl+L    Clear screen (some terminals)
```

---

## 🐛 Common Issues

### Invalid Code Error
```
❌ Entering: 1, 2, 3, 4, 5 (one by one)
✅ Correct:  12345 (all at once)
```

### File Not Found
```
❌ ~/photo.jpg
❌ photo.jpg
✅ /Users/tim/photo.jpg
```

### No Chat Selected
```
Must use option 2 first to select chat,
then use options 3, 4, or 6
```

---

## 📚 Documentation Files

```
README.md          English guide (full)
README_RU.md       Russian guide (full)
QUICKSTART.md      5-minute setup
EXAMPLES.md        Usage examples
FEATURES.md        Complete feature list
CHANGELOG.md       Version history
CHEATSHEET.md      This file
check_setup.py     Verify installation
```

---

## 🔐 Setup .env File

```env
API_ID=1234567
API_HASH=abc123def456...
PHONE_NUMBER=+79161234567
```

Get credentials: https://my.telegram.org

---

## 📞 Quick Example Session

```bash
$ python3 main.py
✓ Logged in as: John

Select option: 1          # Show chats
1. 👤 Alice 🔴 3
2. 👥 Work Team

Select option: 7          # Interactive
Enter chat: 1

You > Hey Alice!
✓ Message sent!

You > /file /path/photo.jpg
Caption: Check this out!
✓ File sent!

You > exit
```

---

## 🎯 Pro Tips

1. **Use interactive mode (7)** for conversations
2. **Enable notifications (8)** when multitasking
3. **Remember chat numbers** for quick access
4. **Use absolute file paths** always
5. **Format with markdown** for clarity
6. **Check info (6)** before sending to groups
7. **Run check_setup.py** if issues occur

---

## 🚀 Most Used Commands

```bash
# 90% of usage:
Option 1  → See chats
Option 7  → Chat with someone
  exit    → Leave chat
Option 8  → Toggle notifications
```

---

## 📱 Supported Content

```
✅ Text, Photos, Videos, Documents
✅ Emojis, Links, Formatting
✅ Users, Groups, Channels
⏳ Stickers, Voice (planned)
❌ Calls, Secret chats
```

---

## 🛠️ Troubleshooting Commands

```bash
# Verify setup
python3 check_setup.py

# Reinstall dependencies
pip3 install --upgrade -r requirements.txt

# Check .env
cat .env

# Check Python version (need 3.7+)
python3 --version
```

---

## 💡 Quick Workflow

**Morning Check:**
```
1 → See unread
2 → Read important ones
7 → Reply in interactive mode
```

**Send File:**
```
1 → List chats
2 → Select chat
4 → Send file
```

**Find Someone:**
```
5 → Search by name
7 → Start chatting
```

---

**Print this page for quick reference!** 📄

*Keep coding in the terminal!* ⌨️

