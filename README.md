# 📱 Telegram Terminal Client

A modern, feature-rich Telegram client for terminal, written in Python using the Telethon library.

## ✨ Features

- 🔐 Authenticate with Telegram via terminal
- 💬 Interactive chat mode with **real-time message updates**
- 🎨 **Separate display** for channels and personal chats/groups
- 🖼️ **ASCII art rendering** for images directly in terminal
- ✍️ Send text messages with markdown formatting
- 📎 Send photos, videos, and documents
- 🔍 Search through your chats
- 👤 View detailed chat/user information
- 🎯 Streamlined, intuitive interface
- 🌈 Colorful output for better readability
- ⚡ Auto-refreshing messages in conversations

## 📋 Requirements

- Python 3.7 or higher
- Telegram account
- API ID and API Hash from Telegram

## 🚀 Installation

### 1. Clone/Create Project

If you haven't created the project yet, create a directory and navigate to it.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

or if using pip3:

```bash
pip3 install -r requirements.txt
```

### 3. Get API Credentials

1. Go to https://my.telegram.org
2. Log in to your Telegram account
3. Navigate to "API development tools"
4. Create a new application (if you haven't already)
5. Copy your **API ID** and **API Hash**

**Step-by-step:**
- **App title**: Any name (e.g., "MyTerminalClient")
- **Short name**: Any alphanumeric (e.g., "terminal")
- **Platform**: Select **Desktop**
- **Description**: Any text (e.g., "Terminal client")

### 4. Configure Settings

1. Create a `.env` file in the project root:

```bash
cd /Something/Vaib_tg
nano .env
```

**Important:** Phone number must be in international format (with country code)

Example:
```env
API_ID=1234567
API_HASH=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
PHONE_NUMBER=+79161234567
```

## 💻 Usage

### Launch Application

```bash
python main.py
```

or

```bash
python3 main.py
```

### First Launch

On the first run, you'll need to:
1. Enter the confirmation code that Telegram sends you
2. If you have two-factor authentication enabled, enter your password

After that, the session is saved and you won't need to authenticate again.

### Application Menu

After successful authentication, you'll see the main menu:

```
1. Open chat (interactive mode) - Browse and select a chat to start messaging
2. Search chats - Find chats by name
3. Show current chat info - View details about the active chat
4. Send file to current chat - Upload a file/photo
5. Exit - Close the application
```

**New streamlined workflow**: Just press `1`, select a chat, and start chatting immediately!

### Usage Examples

#### Starting a Chat (Main Feature)
1. Select option `1` from main menu
2. You'll see two sections:
   - **👥 Personal Chats & Groups** - numbered 1, 2, 3...
   - **📢 Channels** - access with 'c' prefix (c1, c2, c3...)
3. Enter a number (e.g., `5`) for personal chats or `c5` for channels
4. You're instantly in **interactive mode** - start typing!

#### Interactive Mode Features
- **Real-time updates**: New messages appear automatically while you type
- **ASCII art images**: Photos are rendered as ASCII art in terminal
- **Simple messaging**: Just type and press Enter to send
- **Commands available**:
  - `exit` - Leave interactive mode
  - `/help` - Show available commands
  - `/info` - Show chat information
  - `/file <path>` - Send a file
  - `/refresh` - Manually check for new messages
  - `/images` - Reload recent messages with images

#### Message Formatting
Use Telegram's markdown syntax:
- `**bold text**` for **bold**
- `__italic text__` for *italic*
- `` `code` `` for `monospace`
- `[link](URL)` for hyperlinks

#### Send Files
1. In interactive mode, type `/file <path>`
2. Or use option `4` from main menu
3. Enter file path and optional caption

#### Search Chats
1. Select option `2` from main menu
2. Enter search query
3. See matching results

## 🎨 Color Scheme

- 🟢 Green - Personal chats and user messages
- 🔵 Blue - Channels
- 🟡 Yellow - Groups and ASCII art images
- 🟣 Purple - Your messages in interactive mode
- 🔴 Red - Errors
- 🟠 Orange - System notifications

## 📁 Project Structure

```
Vaib_tg/
├── main.py              # Main application file
├── config.py            # Configuration
├── requirements.txt     # Python dependencies (includes Pillow for images)
├── CHANGELOG.md         # Version history
├── .env                 # Your credentials file (create this)
├── .gitignore          # Ignored files
└── README.md           # This file
```

Clean and minimal structure - removed excessive documentation files!

## 🔒 Security

- ⚠️ **Never** share your API credentials
- ⚠️ The `.env` file is added to `.gitignore` and should not be committed
- ⚠️ Session files (`.session`) are also not committed - they contain auth data
- ✅ Telethon uses MTProto protocol with end-to-end encryption

## 🎯 Advanced Features

### Real-time Message Updates
Messages automatically appear in interactive mode as they arrive - no manual refresh needed!

### ASCII Art Image Rendering
Photos are converted to ASCII art and displayed directly in your terminal. Adjust terminal width for best results.

### Separated Chat Lists
- **Personal Chats & Groups** shown first (numbered 1, 2, 3...)
- **Channels** shown separately (access with 'c' prefix: c1, c2, c3...)
- No more scrolling through 20 channel messages to find personal chats!

### Message Formatting
Use Telegram's markdown syntax:
- `**bold text**` - Bold
- `__italic text__` - Italic
- `` `code` `` - Monospace
- `[link text](URL)` - Hyperlinks

### File Sending
Supported file types:
- 📷 Photos (`.jpg`, `.png`, `.gif`, etc.)
- 🎥 Videos (`.mp4`, `.mov`, etc.)
- 📄 Documents (any file type)

### Chat Search
Quickly find chats by name, username, or partial match

## 🐛 Troubleshooting

### Error: "API_ID and API_HASH are required"
- Make sure you created the `.env` file
- Check that API_ID and API_HASH are correct (no quotes needed)

### Authentication Error
- Verify phone number format (+1234567890)
- Make sure API credentials are correct

### Confirmation Code Not Received
- Check Telegram on all your devices
- Code arrives in Telegram app, not SMS (usually)
- Look in "Telegram" system chat or "Saved Messages"

### Module Import Error
- Make sure all dependencies are installed:
  ```bash
  pip install -r requirements.txt
  ```

### File Upload Error
- Check file path is correct and absolute
- Make sure file exists and is readable
- Check file size (Telegram has limits)

## 📚 Additional Information

### Telethon Documentation
https://docs.telethon.dev/

### Telegram API Documentation
https://core.telegram.org/api

### Telegram Bot API
https://core.telegram.org/bots/api

## 🆕 Recent Updates (v3.0)

### Major Interface Overhaul
- ✅ **Streamlined UI**: Reduced menu from 9 to 5 options
- ✅ **Interactive mode as default**: No need to navigate through multiple menus
- ✅ **Separated chat lists**: Channels and personal chats shown separately
- ✅ **ASCII art images**: Photos rendered directly in terminal
- ✅ **Real-time auto-refresh**: Messages update automatically in interactive mode
- ✅ **Cleaner project structure**: Removed 10+ redundant documentation files
- ✅ **Improved workflow**: Select chat and start messaging in 2 clicks

## 🤝 Support

If you have questions or issues:
1. Check the "Troubleshooting" section
2. Make sure all dependencies are installed
3. Verify your `.env` file is configured correctly

## 🛠️ Development

Want to contribute or modify?
- The code is well-commented in English
- Main logic is in `main.py`
- Configuration in `config.py`
- Follow Python best practices

## 📝 License

MIT

---

**Enjoy using the terminal Telegram client! 🚀**

*Stay connected, stay in the terminal!* ⌨️
