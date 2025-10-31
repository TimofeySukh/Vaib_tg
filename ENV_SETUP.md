# 🔧 Environment Setup Guide

Complete guide for setting up your `.env` configuration file.

---

## 📝 Create .env File

Run this command in the project directory:

```bash
cd /Users/tim/Cursor_projects/Vaib_tg
nano .env
```

Or create the file using any text editor.

---

## 📋 .env File Template

Copy and paste this into your `.env` file:

```env
# =============================================================================
# Telegram API Configuration
# =============================================================================

# Your API ID from https://my.telegram.org
# This is a number like: 1234567
API_ID=your_api_id_here

# Your API Hash from https://my.telegram.org
# This is a long string like: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
API_HASH=your_api_hash_here

# Your phone number in international format
# Must include country code: +1234567890
# Examples:
#   USA: +12025551234
#   Russia: +79161234567
#   UK: +447700900000
PHONE_NUMBER=+1234567890

# =============================================================================
# Notes:
# - DO NOT use quotes around values
# - DO NOT commit this file to git (it's in .gitignore)
# - Keep your credentials secret
# - Get API credentials from: https://my.telegram.org
# =============================================================================
```

---

## 🔑 Getting API Credentials

### Step 1: Open Telegram Website
Go to: **https://my.telegram.org**

### Step 2: Login
- Enter your phone number (with country code)
- Click "Next"
- Enter the confirmation code sent to your Telegram app
- If you have 2FA, enter your password

### Step 3: Create Application
- Click **"API development tools"**
- Fill in the form:

```
App title:        MyTerminalClient
                  (any name you want)

Short name:       terminal
                  (5-32 alphanumeric characters)

Platform:         Desktop
                  ⚠️ IMPORTANT: Select "Desktop"!

Description:      Telegram terminal client
                  (any description)
```

- Click "Create application"

### Step 4: Copy Credentials
You'll see:

```
App api_id:      1234567
App api_hash:    a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

**Copy these values!**

---

## ✍️ Fill in .env File

Replace placeholder values with your actual credentials:

### Example .env File:

```env
API_ID=1234567
API_HASH=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
PHONE_NUMBER=+79161234567
```

### ⚠️ Important Rules:

1. **No quotes needed**
   ```env
   ✅ API_ID=1234567
   ❌ API_ID="1234567"
   ❌ API_ID='1234567'
   ```

2. **No spaces around =**
   ```env
   ✅ API_ID=1234567
   ❌ API_ID = 1234567
   ```

3. **Phone with country code**
   ```env
   ✅ PHONE_NUMBER=+79161234567
   ❌ PHONE_NUMBER=9161234567
   ```

4. **API_HASH is long**
   ```env
   ✅ API_HASH=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
   ❌ API_HASH=short
   ```

---

## ✅ Verify Setup

After creating `.env`, run:

```bash
python3 check_setup.py
```

This will check if everything is configured correctly.

Expected output:

```
==============================================================
  🔍 Telegram Terminal Client - Setup Verification
==============================================================

Checking Python environment...
🐍 Python version: 3.x.x ✓

Checking dependencies...
📦 Telethon: ✓ Installed
📦 python-dotenv: ✓ Installed
📦 Colorama: ✓ Installed

Checking file structure...
📁 main.py: ✓
📁 config.py: ✓
📁 requirements.txt: ✓

Checking configuration...
📄 .env file: ✓ Exists
   ✓ All variables configured

==============================================================
✓ All checks passed! You're ready to run the app.

Run: python3 main.py
==============================================================
```

---

## 🎯 Quick Setup Script

Copy and paste this entire script:

```bash
#!/bin/bash

# Navigate to project
cd /Users/tim/Cursor_projects/Vaib_tg

# Create .env file
cat > .env << 'EOF'
API_ID=your_api_id_here
API_HASH=your_api_hash_here
PHONE_NUMBER=+1234567890
EOF

echo "✅ .env file created!"
echo ""
echo "Now edit the file and replace placeholder values:"
echo "  nano .env"
echo ""
echo "Get API credentials from: https://my.telegram.org"
```

Save as `setup_env.sh`, make executable and run:

```bash
chmod +x setup_env.sh
./setup_env.sh
```

---

## 🔒 Security Tips

### ✅ DO:
- Keep `.env` file private
- Never share your API credentials
- Never commit `.env` to git
- Use strong password for 2FA
- Check `.env` is in `.gitignore`

### ❌ DON'T:
- Share `.env` file
- Post credentials online
- Commit to GitHub/GitLab
- Share session files
- Use on untrusted computers

---

## 🐛 Common Issues

### Issue 1: "API_ID required" error

**Cause:** `.env` file not found or empty

**Solution:**
```bash
# Check if file exists
ls -la .env

# View contents
cat .env

# If missing, create it
nano .env
```

### Issue 2: "Invalid credentials" error

**Cause:** Wrong API_ID or API_HASH

**Solution:**
1. Go to https://my.telegram.org
2. Login and check "API development tools"
3. Verify your credentials
4. Copy exact values (no extra spaces)

### Issue 3: "Phone number invalid" error

**Cause:** Wrong phone format

**Solution:**
```env
❌ PHONE_NUMBER=9161234567
✅ PHONE_NUMBER=+79161234567
     Must have + and country code!
```

### Issue 4: Placeholder values detected

**Cause:** Didn't replace `your_api_id_here`

**Solution:**
Replace ALL placeholder values with real ones:
```env
Before:  API_ID=your_api_id_here
After:   API_ID=1234567
```

---

## 📱 Phone Number Formats

### Country Code Examples:

| Country | Code | Example |
|---------|------|---------|
| 🇺🇸 USA | +1 | +12025551234 |
| 🇷🇺 Russia | +7 | +79161234567 |
| 🇬🇧 UK | +44 | +447700900000 |
| 🇩🇪 Germany | +49 | +491234567890 |
| 🇫🇷 France | +33 | +33612345678 |
| 🇮🇹 Italy | +39 | +393123456789 |
| 🇪🇸 Spain | +34 | +34612345678 |
| 🇨🇦 Canada | +1 | +14165551234 |
| 🇦🇺 Australia | +61 | +61412345678 |
| 🇯🇵 Japan | +81 | +819012345678 |
| 🇨🇳 China | +86 | +8613812345678 |
| 🇮🇳 India | +91 | +919876543210 |
| 🇧🇷 Brazil | +55 | +5511987654321 |
| 🇲🇽 Mexico | +52 | +521234567890 |

Find your country code: https://countrycode.org/

---

## ✨ Template File

If you want a template file to copy:

```bash
# Create template
cat > .env.template << 'EOF'
API_ID=
API_HASH=
PHONE_NUMBER=
EOF

# Copy template to .env
cp .env.template .env

# Edit .env
nano .env
```

---

## 🆘 Need Help?

1. **Read this guide completely**
2. **Run check_setup.py**
3. **Check TROUBLESHOOTING section in README.md**
4. **Verify all steps above**

---

## 📚 Related Documentation

- `README.md` - Full documentation (English)
- `README_RU.md` - Full documentation (Russian)
- `QUICKSTART.md` - 5-minute setup guide
- `check_setup.py` - Automated verification tool
- `CHEATSHEET.md` - Quick reference

---

**Once configured, you never need to do this again!** 🎉

*The session persists across launches.*

