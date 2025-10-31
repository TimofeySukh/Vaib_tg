#!/usr/bin/env python3
"""
Telegram Terminal Client
Advanced terminal-based Telegram client using Telethon
"""

import asyncio
import sys
import os
from datetime import datetime
from telethon import TelegramClient, events
from telethon.tl.types import User, Chat, Channel, MessageMediaPhoto, MessageMediaDocument
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from colorama import init, Fore, Style
import config

# Initialize colorama for colored terminal output
init(autoreset=True)


class TelegramTerminalClient:
    """Advanced terminal-based Telegram client"""
    
    def __init__(self):
        """Initialize the Telegram client"""
        if not config.API_ID or not config.API_HASH:
            print(f"{Fore.RED}Error: API_ID and API_HASH are required!")
            print(f"{Fore.YELLOW}Please create a .env file based on .env.example")
            print(f"{Fore.YELLOW}Get your API credentials from https://my.telegram.org")
            sys.exit(1)
        
        self.client = TelegramClient(
            config.SESSION_NAME,
            config.API_ID,
            config.API_HASH
        )
        self.current_chat = None
        self.dialogs = []
        self.notifications_enabled = False
        self.message_handler = None
    
    async def start(self):
        """Start and authenticate the client"""
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}        🚀 Telegram Terminal Client v2.0 🚀")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        await self.client.start(phone=config.PHONE_NUMBER)
        
        me = await self.client.get_me()
        print(f"{Fore.GREEN}✓ Successfully logged in as: {me.first_name}")
        if me.username:
            print(f"{Fore.GREEN}✓ Username: @{me.username}")
        print(f"{Fore.GREEN}✓ User ID: {me.id}\n")
    
    async def show_dialogs(self, limit=30):
        """Display list of recent chats"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}  📱 Your Chats")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        self.dialogs = await self.client.get_dialogs(limit=limit)
        
        for idx, dialog in enumerate(self.dialogs, 1):
            entity = dialog.entity
            name = self._get_entity_name(entity)
            unread = dialog.unread_count
            
            # Get last message preview
            last_msg = dialog.message.text[:30] + "..." if dialog.message and dialog.message.text and len(dialog.message.text) > 30 else (dialog.message.text if dialog.message and dialog.message.text else "")
            
            # Color coding based on entity type
            if isinstance(entity, User):
                color = Fore.GREEN
                type_icon = "👤"
            elif isinstance(entity, Channel):
                color = Fore.BLUE
                type_icon = "📢"
            else:
                color = Fore.YELLOW
                type_icon = "👥"
            
            unread_str = f" 🔴 {unread}" if unread > 0 else ""
            print(f"{color}{idx:2d}. {type_icon} {name}{unread_str}")
            if last_msg:
                print(f"{Fore.WHITE}    └─ {last_msg}")
        
        print()
    
    def _get_entity_name(self, entity):
        """Get display name for an entity"""
        if isinstance(entity, User):
            if entity.first_name and entity.last_name:
                return f"{entity.first_name} {entity.last_name}"
            elif entity.first_name:
                return entity.first_name
            elif entity.username:
                return f"@{entity.username}"
            return "Unknown User"
        elif isinstance(entity, (Chat, Channel)):
            return entity.title
        return "Unknown"
    
    async def show_messages(self, chat_index, limit=30):
        """Display recent messages from a chat"""
        if chat_index < 1 or chat_index > len(self.dialogs):
            print(f"{Fore.RED}❌ Invalid chat number!")
            return
        
        dialog = self.dialogs[chat_index - 1]
        self.current_chat = dialog.entity
        chat_name = self._get_entity_name(self.current_chat)
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}  💬 Chat: {chat_name}")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        messages = await self.client.get_messages(self.current_chat, limit=limit)
        
        # Display messages in chronological order (oldest first)
        for msg in reversed(messages):
            await self._display_message(msg)
        
        print(f"\n{Fore.CYAN}{'─'*60}\n")
        print(f"{Fore.WHITE}💡 Tip: Use option 7 for interactive mode!")
    
    async def _display_message(self, message):
        """Format and display a single message"""
        sender = await message.get_sender()
        sender_name = self._get_entity_name(sender) if sender else "System"
        
        # Format timestamp
        time_str = message.date.strftime("%H:%M:%S")
        date_str = message.date.strftime("%d.%m.%Y")
        
        # Check if message is from current user
        me = await self.client.get_me()
        is_me = sender and sender.id == me.id
        
        if is_me:
            color = Fore.MAGENTA
            prefix = "You"
        else:
            color = Fore.GREEN
            prefix = sender_name
        
        # Handle different message types
        msg_content = ""
        if message.text:
            msg_content = message.text
        elif message.media:
            if isinstance(message.media, MessageMediaPhoto):
                msg_content = "📷 [Photo]"
                if message.message:
                    msg_content += f" {message.message}"
            elif isinstance(message.media, MessageMediaDocument):
                msg_content = "📎 [File]"
                if message.message:
                    msg_content += f" {message.message}"
            else:
                msg_content = "📎 [Media]"
        
        if msg_content:
            print(f"{Fore.CYAN}[{time_str}] {color}{prefix}{Style.RESET_ALL}: {msg_content}")
    
    async def send_message(self, text, parse_mode='md'):
        """Send a message to the current chat with formatting support"""
        if not self.current_chat:
            print(f"{Fore.RED}❌ No chat selected! Please select a chat first.")
            return
        
        try:
            await self.client.send_message(
                self.current_chat, 
                text,
                parse_mode=parse_mode
            )
            print(f"{Fore.GREEN}✓ Message sent!")
        except Exception as e:
            print(f"{Fore.RED}❌ Error sending message: {str(e)}")
    
    async def send_file(self, file_path, caption=""):
        """Send a file to the current chat"""
        if not self.current_chat:
            print(f"{Fore.RED}❌ No chat selected! Please select a chat first.")
            return
        
        if not os.path.exists(file_path):
            print(f"{Fore.RED}❌ File not found: {file_path}")
            return
        
        try:
            print(f"{Fore.YELLOW}⏳ Uploading file...")
            await self.client.send_file(
                self.current_chat,
                file_path,
                caption=caption
            )
            print(f"{Fore.GREEN}✓ File sent successfully!")
        except Exception as e:
            print(f"{Fore.RED}❌ Error sending file: {str(e)}")
    
    async def search_chats(self, query):
        """Search for chats by name"""
        print(f"\n{Fore.CYAN}🔍 Searching for '{query}'...\n")
        
        found = []
        for idx, dialog in enumerate(self.dialogs, 1):
            entity = dialog.entity
            name = self._get_entity_name(entity)
            
            if query.lower() in name.lower():
                found.append((idx, entity, name))
        
        if not found:
            print(f"{Fore.YELLOW}No chats found matching '{query}'")
            return
        
        print(f"{Fore.GREEN}Found {len(found)} chat(s):\n")
        for idx, entity, name in found:
            if isinstance(entity, User):
                icon = "👤"
                color = Fore.GREEN
            elif isinstance(entity, Channel):
                icon = "📢"
                color = Fore.BLUE
            else:
                icon = "👥"
                color = Fore.YELLOW
            
            print(f"{color}{idx}. {icon} {name}")
        print()
    
    async def show_chat_info(self):
        """Display detailed information about the current chat"""
        if not self.current_chat:
            print(f"{Fore.RED}❌ No chat selected!")
            return
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}  ℹ️  Chat Information")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        entity = self.current_chat
        name = self._get_entity_name(entity)
        
        print(f"{Fore.WHITE}Name: {Fore.GREEN}{name}")
        print(f"{Fore.WHITE}ID: {Fore.GREEN}{entity.id}")
        
        if isinstance(entity, User):
            try:
                full_user = await self.client(GetFullUserRequest(entity))
                user = full_user.users[0]
                
                if user.username:
                    print(f"{Fore.WHITE}Username: {Fore.GREEN}@{user.username}")
                if user.phone:
                    print(f"{Fore.WHITE}Phone: {Fore.GREEN}{user.phone}")
                
                print(f"{Fore.WHITE}Bot: {Fore.GREEN}{'Yes' if user.bot else 'No'}")
                
                if full_user.full_user.about:
                    print(f"{Fore.WHITE}Bio: {Fore.GREEN}{full_user.full_user.about}")
                
            except Exception as e:
                print(f"{Fore.YELLOW}Could not fetch full user info")
        
        elif isinstance(entity, (Chat, Channel)):
            print(f"{Fore.WHITE}Type: {Fore.GREEN}{'Channel' if isinstance(entity, Channel) else 'Group'}")
            
            if hasattr(entity, 'username') and entity.username:
                print(f"{Fore.WHITE}Username: {Fore.GREEN}@{entity.username}")
            
            if hasattr(entity, 'participants_count'):
                print(f"{Fore.WHITE}Members: {Fore.GREEN}{entity.participants_count}")
            
            try:
                if isinstance(entity, Channel):
                    full_chat = await self.client(GetFullChannelRequest(entity))
                    if full_chat.full_chat.about:
                        print(f"{Fore.WHITE}Description: {Fore.GREEN}{full_chat.full_chat.about}")
            except:
                pass
        
        print(f"\n{Fore.CYAN}{'='*60}\n")
    
    async def toggle_notifications(self):
        """Toggle real-time message notifications"""
        if self.notifications_enabled:
            # Disable notifications
            if self.message_handler:
                self.client.remove_event_handler(self.message_handler)
                self.message_handler = None
            self.notifications_enabled = False
            print(f"{Fore.YELLOW}🔕 Notifications disabled")
        else:
            # Enable notifications
            @self.client.on(events.NewMessage(incoming=True))
            async def handler(event):
                sender = await event.get_sender()
                sender_name = self._get_entity_name(sender) if sender else "Unknown"
                msg_preview = event.text[:50] + "..." if event.text and len(event.text) > 50 else (event.text if event.text else "[Media]")
                print(f"\n{Fore.CYAN}🔔 New message from {Fore.GREEN}{sender_name}{Fore.CYAN}: {msg_preview}\n")
            
            self.message_handler = handler
            self.notifications_enabled = True
            print(f"{Fore.GREEN}🔔 Notifications enabled! You'll see new messages in real-time.")
    
    async def interactive_chat(self):
        """Enhanced interactive chat mode with commands"""
        if not self.current_chat:
            print(f"{Fore.RED}❌ No chat selected! Please select a chat first.")
            return
        
        chat_name = self._get_entity_name(self.current_chat)
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}  💬 Interactive Chat: {chat_name}")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.WHITE}Commands: {Fore.YELLOW}exit{Fore.WHITE}, {Fore.YELLOW}/help{Fore.WHITE}, {Fore.YELLOW}/info{Fore.WHITE}, {Fore.YELLOW}/file{Fore.WHITE}, {Fore.YELLOW}/clear{Fore.WHITE}, {Fore.YELLOW}/history")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        # Show recent messages
        messages = await self.client.get_messages(self.current_chat, limit=15)
        for msg in reversed(messages):
            await self._display_message(msg)
        
        print(f"\n{Fore.CYAN}{'─'*60}\n")
        
        while True:
            try:
                user_input = input(f"{Fore.MAGENTA}You >{Style.RESET_ALL} ")
                
                if not user_input.strip():
                    continue
                
                # Handle commands
                if user_input.lower() == 'exit':
                    print(f"{Fore.GREEN}👋 Leaving chat...\n")
                    break
                
                elif user_input == '/help':
                    self._show_interactive_help()
                    continue
                
                elif user_input == '/info':
                    await self.show_chat_info()
                    continue
                
                elif user_input == '/clear':
                    os.system('clear' if os.name != 'nt' else 'cls')
                    print(f"{Fore.CYAN}Chat: {chat_name}\n")
                    continue
                
                elif user_input == '/history':
                    print(f"\n{Fore.YELLOW}Loading more messages...\n")
                    messages = await self.client.get_messages(self.current_chat, limit=30)
                    for msg in reversed(messages):
                        await self._display_message(msg)
                    print()
                    continue
                
                elif user_input.startswith('/file '):
                    file_path = user_input[6:].strip()
                    caption = input(f"{Fore.YELLOW}Caption (optional): {Style.RESET_ALL}")
                    await self.send_file(file_path, caption)
                    continue
                
                # Send regular message with markdown support
                await self.send_message(user_input)
                
            except KeyboardInterrupt:
                print(f"\n{Fore.GREEN}👋 Leaving chat...\n")
                break
            except EOFError:
                print(f"\n{Fore.GREEN}👋 Leaving chat...\n")
                break
            except Exception as e:
                print(f"{Fore.RED}❌ Error: {str(e)}")
    
    def _show_interactive_help(self):
        """Show help for interactive mode"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}  📖 Interactive Mode Commands")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.WHITE}  exit              - Leave interactive mode")
        print(f"{Fore.WHITE}  /help             - Show this help")
        print(f"{Fore.WHITE}  /info             - Show chat information")
        print(f"{Fore.WHITE}  /file <path>      - Send a file")
        print(f"{Fore.WHITE}  /clear            - Clear screen")
        print(f"{Fore.WHITE}  /history          - Load more messages")
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}  📝 Message Formatting")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.WHITE}  **bold**          - Bold text")
        print(f"{Fore.WHITE}  __italic__        - Italic text")
        print(f"{Fore.WHITE}  `code`            - Monospace text")
        print(f"{Fore.WHITE}  [text](url)       - Hyperlink")
        print(f"{Fore.CYAN}{'='*60}\n")
    
    def show_menu(self):
        """Display enhanced main menu"""
        status = f"{Fore.GREEN}🔔 ON" if self.notifications_enabled else f"{Fore.YELLOW}🔕 OFF"
        current = f"{Fore.GREEN}{self._get_entity_name(self.current_chat)}" if self.current_chat else f"{Fore.RED}None"
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}  📋 Main Menu")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.WHITE}  Current chat: {current}")
        print(f"{Fore.WHITE}  Notifications: {status}")
        print(f"{Fore.CYAN}{'─'*60}")
        print(f"{Fore.WHITE}  1. 📱 Show chats")
        print(f"{Fore.WHITE}  2. 📨 Read messages from chat")
        print(f"{Fore.WHITE}  3. ✍️  Send text message")
        print(f"{Fore.WHITE}  4. 📎 Send file/photo")
        print(f"{Fore.WHITE}  5. 🔍 Search chats")
        print(f"{Fore.WHITE}  6. ℹ️  Show chat info")
        print(f"{Fore.WHITE}  7. 💬 Interactive chat mode")
        print(f"{Fore.WHITE}  8. 🔔 Toggle notifications")
        print(f"{Fore.WHITE}  9. ❌ Exit")
        print(f"{Fore.CYAN}{'='*60}\n")
    
    async def run(self):
        """Main application loop"""
        await self.start()
        
        while True:
            try:
                self.show_menu()
                choice = input(f"{Fore.YELLOW}Select option: {Style.RESET_ALL}").strip()
                
                if choice == '1':
                    await self.show_dialogs()
                
                elif choice == '2':
                    if not self.dialogs:
                        await self.show_dialogs()
                    
                    try:
                        chat_num = int(input(f"{Fore.YELLOW}Enter chat number: {Style.RESET_ALL}"))
                        await self.show_messages(chat_num)
                    except ValueError:
                        print(f"{Fore.RED}❌ Invalid number!")
                
                elif choice == '3':
                    if not self.current_chat:
                        print(f"{Fore.YELLOW}⚠️  Please select a chat first (option 2)")
                        continue
                    
                    print(f"{Fore.WHITE}💡 Tip: Use **bold**, __italic__, `code` for formatting")
                    message = input(f"{Fore.YELLOW}Enter message: {Style.RESET_ALL}")
                    if message.strip():
                        await self.send_message(message)
                
                elif choice == '4':
                    if not self.current_chat:
                        print(f"{Fore.YELLOW}⚠️  Please select a chat first (option 2)")
                        continue
                    
                    file_path = input(f"{Fore.YELLOW}Enter file path: {Style.RESET_ALL}").strip()
                    if file_path:
                        caption = input(f"{Fore.YELLOW}Caption (optional): {Style.RESET_ALL}")
                        await self.send_file(file_path, caption)
                
                elif choice == '5':
                    if not self.dialogs:
                        await self.show_dialogs()
                    
                    query = input(f"{Fore.YELLOW}Search query: {Style.RESET_ALL}").strip()
                    if query:
                        await self.search_chats(query)
                
                elif choice == '6':
                    await self.show_chat_info()
                
                elif choice == '7':
                    if not self.dialogs:
                        await self.show_dialogs()
                    
                    try:
                        chat_num = int(input(f"{Fore.YELLOW}Enter chat number: {Style.RESET_ALL}"))
                        if 1 <= chat_num <= len(self.dialogs):
                            dialog = self.dialogs[chat_num - 1]
                            self.current_chat = dialog.entity
                            await self.interactive_chat()
                        else:
                            print(f"{Fore.RED}❌ Invalid chat number!")
                    except ValueError:
                        print(f"{Fore.RED}❌ Invalid number!")
                
                elif choice == '8':
                    await self.toggle_notifications()
                
                elif choice == '9':
                    print(f"\n{Fore.GREEN}👋 Goodbye! Thanks for using Telegram Terminal Client!\n")
                    break
                
                else:
                    print(f"{Fore.RED}❌ Invalid option!")
            
            except KeyboardInterrupt:
                print(f"\n{Fore.GREEN}👋 Goodbye!\n")
                break
            except EOFError:
                print(f"\n{Fore.GREEN}👋 Goodbye!\n")
                break
            except Exception as e:
                print(f"{Fore.RED}❌ Unexpected error: {str(e)}")
        
        await self.client.disconnect()


async def main():
    """Entry point"""
    client = TelegramTerminalClient()
    await client.run()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.GREEN}Application terminated by user.\n")
        sys.exit(0)
