# 📝 Changelog

All notable changes to Telegram Terminal Client.

---

## [3.0.0] - 2025-11-05

### 🎉 Major Interface Overhaul

#### ✨ Revolutionary Features
- **🖼️ ASCII Art Image Rendering** - Photos displayed as ASCII art directly in terminal!
- **⚡ Real-time Auto-refresh** - Messages update automatically with event handlers
- **🎯 Streamlined Interface** - Reduced from 9 menu options to just 5
- **🔀 Separated Chat Lists** - Channels and personal chats displayed separately
- **💬 Interactive Mode as Default** - Start chatting in 2 clicks

#### 🎨 UX Improvements
- **Simplified workflow**: Press 1 → Select chat → Start messaging
- **Better chat organization**: Personal chats first, channels separate with 'c' prefix
- **No more scrolling**: Channels don't dominate the first 20 entries anymore
- **Intuitive selection**: Type `5` for personal chat #5 or `c5` for channel #5
- **Enhanced commands**: `/refresh`, `/images` for better control

#### 📚 Project Cleanup
- **Removed 10+ redundant files**: All Russian-language documentation removed
- **Cleaner structure**: Only essential files remain
- **Single source of truth**: One comprehensive README
- **Better organization**: Focus on English-speaking audience

#### 🛠️ Technical Improvements
- Added Pillow library for image processing
- Event-based message handlers for real-time updates
- Async executor for concurrent input handling
- Better message ID tracking
- Separated dialog lists (channels vs chats)
- Enhanced media handling with ASCII rendering

#### 💥 Breaking Changes
- Menu structure completely redesigned
- Option 7 functionality now integrated into option 1
- Removed toggle notifications (always on in interactive mode)
- Removed standalone "read messages" mode (use interactive mode)

---

## [2.0.0] - 2025-10-31

### 🎉 Major Update

#### ✨ New Features
- **Real-time Notifications** - Get alerted when new messages arrive
- **File Sending** - Send photos, videos, and documents
- **Chat Search** - Quickly find chats by name
- **Chat Info Display** - View detailed information about users and groups
- **Enhanced Interactive Mode** - Commands and better UX
- **Message Formatting** - Full markdown support (bold, italic, code, links)
- **Media Detection** - Shows icons for photos and files in messages

#### 🎨 UI Improvements
- Colorful menu with icons
- Better message display with timestamps
- Chat list shows last message preview
- Unread message counter with 🔴 indicator
- Status indicators in menu (current chat, notifications)
- Improved spacing and separators

#### 💬 Interactive Mode Enhancements
- `/help` - Show commands
- `/info` - Display chat information
- `/file <path>` - Send files
- `/clear` - Clear screen
- `/history` - Load more messages
- Better message formatting
- Cleaner interface

#### 📚 Documentation
- English README.md
- Russian README_RU.md
- Quick start guide (QUICKSTART.md)
- Usage examples (EXAMPLES.md)
- Setup verification tool (check_setup.py)
- This changelog!

#### 🛠️ Technical Improvements
- Better error handling
- More informative error messages
- Support for different message types
- Async notifications handler
- Code refactoring and cleanup
- Better separation of concerns

---

## [1.0.0] - Initial Release

### Features
- Basic authentication with Telegram
- View chat list
- Read messages from chats
- Send text messages
- Simple interactive mode
- Colored terminal output
- Basic error handling

---

## 🔮 Planned Features (Future)

### Version 2.1 (Planned)
- [ ] Message editing
- [ ] Message deletion
- [ ] Reply to specific messages
- [ ] Forward messages
- [ ] Voice message support
- [ ] Sticker support
- [ ] Poll creation
- [ ] Contact sharing

### Version 2.2 (Planned)
- [ ] Chat creation
- [ ] Add/remove members
- [ ] Admin actions
- [ ] Pin messages
- [ ] Mute/unmute chats
- [ ] Archive chats
- [ ] Custom themes
- [ ] Configuration file

### Version 3.0 (Planned)
- [ ] Multiple accounts support
- [ ] Bot functionality
- [ ] Automated responses
- [ ] Message scheduling
- [ ] Export chat history
- [ ] Advanced search filters
- [ ] Plugin system
- [ ] Custom commands

---

## 🐛 Known Issues

### Current
- None reported yet!

### Fixed in 2.0.0
- File paths not working with `~` (use absolute paths now)
- No feedback when sending messages
- Unclear error messages
- Limited message type support

---

## 📋 Version Compatibility

| Version | Python | Telethon | Pillow | Status |
|---------|--------|----------|--------|--------|
| 3.0.0 | 3.7+ | 1.35.0 | 10.1.0 | Current |
| 2.0.0 | 3.7+ | 1.35.0 | - | Legacy |
| 1.0.0 | 3.7+ | 1.35.0 | - | Legacy |

---

## 🤝 Contributing

Want to contribute? Ideas for new versions are welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📄 License

This project is created for educational purposes.

---

**Stay tuned for more updates!** 🚀

