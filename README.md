# 📱 Telegram Terminal Client

A simple and convenient Telegram client for terminal, written in Python using the Telethon library.

## ✨ Features

- 🔐 Authenticate with Telegram via terminal
- 💬 View your chat list with icons and unread counts
- 📨 Read messages from any chat with pagination
- ✍️ Send text messages and files to chats
- 🔍 Search through your chats
- 👤 View detailed chat/user information
- 🎯 Interactive chat mode for live conversations
- 🔔 Real-time message notifications
- 🎨 Colorful interface for better readability
- 📝 Message formatting support (bold, italic, code)
- 📎 Send photos, videos, and documents

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
cd /Users/tim/Cursor_projects/Vaib_tg
nano .env
```

2. Fill in your credentials:

```env
API_ID=your_api_id
API_HASH=your_api_hash
PHONE_NUMBER=+1234567890
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
1. Show chats - Display list of your chats
2. Read messages - Read messages from selected chat
3. Send message - Send text message to current chat
4. Send file - Send photo/video/document to current chat
5. Search chats - Find chats by name
6. Chat info - View detailed information about current chat
7. Interactive mode - Live chat mode with auto-refresh
8. Toggle notifications - Enable/disable real-time notifications
9. Exit - Close the application
```

### Usage Examples

#### View Chats
1. Select option `1`
2. You'll see a list of your recent chats with numbers
3. Icons indicate type: 👤 user, 📢 channel, 👥 group
4. Unread message counts are shown

#### Read Messages
1. Select option `2`
2. Enter chat number from the list
3. You'll see recent messages from that chat
4. Use pagination to load more messages

#### Send Message
1. First select a chat (option `2`)
2. Then select option `3`
3. Type your message and press Enter
4. Use formatting:
   - `**bold**` for **bold text**
   - `__italic__` for *italic text*
   - `` `code` `` for `monospace`

#### Send Files
1. Select a chat first
2. Choose option `4`
3. Enter the full path to the file
4. Optionally add a caption

#### Search Chats
1. Select option `5`
2. Enter search query
3. See matching chats

#### Interactive Mode
1. Select option `7`
2. Enter chat number
3. You enter live chat mode
4. Type messages and they're sent immediately
5. New messages appear automatically
6. Type `exit` to leave, `/help` for commands

#### Interactive Mode Commands
- `exit` - Leave interactive mode
- `/help` - Show available commands
- `/info` - Show chat information
- `/file <path>` - Send a file
- `/clear` - Clear screen
- `/history` - Load more messages

## 🎨 Color Scheme

- 🟢 Green - Personal chats and user messages
- 🔵 Blue - Channels
- 🟡 Yellow - Groups
- 🟣 Purple - Your messages in interactive mode
- 🔴 Red - Errors
- 🟠 Orange - System notifications

## 📁 Project Structure

```
Vaib_tg/
├── main.py              # Main application file
├── config.py            # Configuration
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables file
├── .env                 # Your credentials file (not committed to git)
├── .gitignore          # Ignored files
└── README.md           # This file
```

## 🔒 Security

- ⚠️ **Never** share your API credentials
- ⚠️ The `.env` file is added to `.gitignore` and should not be committed
- ⚠️ Session files (`.session`) are also not committed - they contain auth data
- ✅ Telethon uses MTProto protocol with end-to-end encryption

## 🎯 Advanced Features

### Real-time Notifications
Enable notifications (option `8`) to receive alerts when new messages arrive while browsing the menu.

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
Quickly find chats by:
- Name
- Username
- Part of the name

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

## 🆕 Recent Updates

- ✅ Added real-time message notifications
- ✅ Added file/photo sending capability
- ✅ Added chat search functionality
- ✅ Added chat information display
- ✅ Improved interactive mode with auto-refresh
- ✅ Added message formatting support
- ✅ Added interactive mode commands

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

This project is created for educational purposes. Use at your own risk.

---

**Enjoy using the terminal Telegram client! 🚀**

*Stay connected, stay in the terminal!* ⌨️
