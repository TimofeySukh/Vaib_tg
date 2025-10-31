# 📚 Usage Examples & Tips

## 🎨 Message Formatting Examples

### Bold Text
```
Input: Hello **world**!
Output: Hello world! (bold)
```

### Italic Text
```
Input: This is __important__
Output: This is important (italic)
```

### Code / Monospace
```
Input: Run `python main.py` to start
Output: Run python main.py to start (monospace)
```

### Combining Formats
```
Input: **Bold** and __italic__ with `code`
Output: Bold (bold) and italic (italic) with code (monospace)
```

### Links
```
Input: Check [Telegram](https://telegram.org)
Output: Check Telegram (clickable link)
```

### Multi-line Code Block
```
Input: 
```python
def hello():
    print("Hello!")
`` ` (remove space)

Output: Formatted code block
```

---

## 📎 File Sending Examples

### Send Photo
```
Interactive mode:
/file /Users/tim/Pictures/photo.jpg
Caption: Beautiful sunset! 🌅
```

### Send Document
```
Interactive mode:
/file /Users/tim/Documents/report.pdf
Caption: Monthly report
```

### Send Video
```
Interactive mode:
/file /Users/tim/Videos/demo.mp4
Caption: Check this demo!
```

### From Menu (Option 4)
```
Select option: 4
Enter file path: /Users/tim/Desktop/presentation.pptx
Caption (optional): Tomorrow's presentation
```

---

## 🔍 Search Examples

### Search by Name
```
Select option: 5
Search query: Alice
Result: Shows all chats with "Alice" in the name
```

### Search by Username
```
Search query: @john
Result: Finds users with "john" in username
```

### Partial Match
```
Search query: wor
Result: Finds "Work Team", "Workshop", etc.
```

---

## 💬 Interactive Mode Workflow

### Example 1: Quick Chat
```bash
# Launch app
python3 main.py

# From menu:
Select option: 7
Enter chat number: 1

# Now chatting with Alice:
You > Hey! Are you free today?
✓ Message sent!

You > Let's meet at **3 PM** at the cafe
✓ Message sent!

You > exit
👋 Leaving chat...
```

### Example 2: Send Files in Chat
```bash
# In interactive mode:
You > /file /Users/tim/photo.jpg
Caption: From yesterday's event
✓ File sent successfully!

You > Did you receive it?
✓ Message sent!
```

### Example 3: Check Info
```bash
# In interactive mode:
You > /info

# Shows:
ℹ️  Chat Information
==================================
Name: Alice Smith
ID: 123456789
Username: @alice
Phone: +1234567890
Bot: No
```

### Example 4: Load More History
```bash
# In interactive mode:
You > /history

# Loads 30 more messages
```

---

## 🔔 Notifications Usage

### Enable Notifications
```
Select option: 8
Output: 🔔 Notifications enabled!

# Now while in menu, you'll see:
🔔 New message from Bob: Hey, how are you?
```

### Disable Notifications
```
Select option: 8
Output: 🔕 Notifications disabled
```

### Use Case
Enable notifications when:
- Waiting for important messages
- Monitoring group activity
- Multitasking in terminal

---

## 🎯 Real-World Scenarios

### Scenario 1: Morning Routine
```bash
# Check unread messages
1. Show chats (option 1)
   - See unread counts: 🔴 3, 🔴 7, etc.

# Read important ones
2. Read messages (option 2)
   - Enter chat numbers for unread chats

# Quick replies
3. Interactive mode (option 7)
   - Reply to important messages
```

### Scenario 2: File Sharing
```bash
# Select recipient
1. Show chats → choose contact

# Send file
2. Send file (option 4)
   - Path: /Users/tim/Documents/contract.pdf
   - Caption: Signed contract

# Confirm
3. Chat info (option 6)
   - Verify recipient details
```

### Scenario 3: Group Management
```bash
# Find group
1. Search (option 5)
   - Query: "Project Team"

# Check group info
2. Read messages (option 2)
   - Enter group number
3. Chat info (option 6)
   - See member count, description

# Announce something
4. Send message (option 3)
   - Use **formatting** for important parts
```

### Scenario 4: Monitoring Channel
```bash
# Enable notifications
1. Toggle notifications (option 8)

# Continue working in menu
2. Show chats, read messages, etc.

# Get alerted when channel posts:
🔔 New message from Tech News: Breaking: New...
```

---

## 🚀 Advanced Tips

### Tip 1: Use Absolute Paths
```bash
# Bad:
~/photo.jpg
./document.pdf

# Good:
/Users/tim/photo.jpg
/Users/tim/Documents/document.pdf
```

### Tip 2: Formatting in Captions
```bash
/file /path/to/file.jpg
Caption: **Important!** Check this __amazing__ photo!
```

### Tip 3: Quick Navigation
```bash
# Don't keep selecting "show chats"
# Remember chat numbers:
# 1 = Alice
# 2 = Work Team
# 3 = Tech Channel

# Go directly:
Select option: 7  (interactive mode)
Enter chat number: 2  (Work Team)
```

### Tip 4: Multi-line Messages
```bash
# Can't do multi-line in interactive mode
# Use option 3 (send message) instead:
Select option: 3
Enter message: Line 1
Line 2
Line 3
(press Ctrl+D when done)
```

### Tip 5: Clear Screen for Focus
```bash
# In interactive mode:
You > /clear
# Screen cleared, only chat visible
```

---

## 🎨 Emoji Support

### Using Emojis
```bash
You > Great work! 🎉👏
You > Meeting at 3 PM ⏰
You > Check this 👇
```

### Common Emojis
```
👍 👎 ❤️ 😂 😊 😎 🔥 ⭐ ✅ ❌
📱 💻 📧 📞 🏠 🚀 💡 ⚡ 🎉 🎁
⏰ 📅 ⏳ ⚠️ 🔴 🟢 🔵 🟡
```

---

## 🐛 Common Mistakes & Solutions

### Mistake 1: Entering Code Digit by Digit
```bash
# Wrong:
Please enter code: 1
Invalid code. Please try again.

# Correct:
Please enter code: 12345
✓ Success!
```

### Mistake 2: Using Relative File Paths
```bash
# Wrong:
Enter file path: ~/photo.jpg
❌ File not found

# Correct:
Enter file path: /Users/tim/photo.jpg
✓ File sent!
```

### Mistake 3: Forgetting to Select Chat
```bash
# Wrong:
Select option: 3  (send message)
❌ No chat selected!

# Correct:
Select option: 2  (read messages)
Enter chat number: 1
Select option: 3  (send message)
✓ Message sent!
```

### Mistake 4: Not Exiting Interactive Mode
```bash
# In interactive mode, typing menu numbers won't work
You > 1
✓ Message sent!  (sends "1" as message)

# Exit first:
You > exit
# Now back in menu
Select option: 1  (works!)
```

---

## 📊 Keyboard Shortcuts Reference

| Key | Action |
|-----|--------|
| `Ctrl + C` | Interrupt/Cancel |
| `Ctrl + D` | EOF/Exit input |
| `Ctrl + L` | Clear screen (in some terminals) |
| `↑` / `↓` | Navigate command history (in some terminals) |

---

## 🎓 Best Practices

1. **Always use absolute paths** for files
2. **Enable notifications** when multitasking
3. **Use interactive mode** for conversations
4. **Use menu options** for quick actions
5. **Format important messages** with **bold**
6. **Check chat info** before sending to groups
7. **Use search** for large chat lists
8. **Keep terminal window wide** for better formatting

---

**Need more help? Check README.md or README_RU.md!**

