# GoonLang VS Code Extension - Installation Guide

## 📦 Installation Methods

### Method 1: VS Code Marketplace (Recommended)

1. **Open VS Code**
2. **Open Extensions panel** (Ctrl+Shift+X or Cmd+Shift+X)
3. **Search for "GoonLang"**
4. **Click "Install"** on the GoonLang extension by GoonLang Foundation
5. **Reload VS Code** if prompted

### Method 2: Install from VSIX File

1. **Download** the latest `.vsix` file from releases
2. **Open VS Code**
3. **Open Command Palette** (Ctrl+Shift+P or Cmd+Shift+P)
4. **Type** "Extensions: Install from VSIX..."
5. **Select** the downloaded `.vsix` file
6. **Reload VS Code** if prompted

### Method 3: Build from Source

```bash
# Clone the repository
git clone https://github.com/goonlang/vscode-goonlang.git
cd vscode-goonlang

# Install dependencies
npm install

# Build the extension
npm run compile

# Package the extension
npm run package

# Install the generated .vsix file
code --install-extension goonlang-*.vsix
```

## 🔧 Prerequisites

### Required
- **VS Code 1.74.0** or higher
- **GoonLang interpreter** installed and in PATH

### Optional
- **Node.js 16+** (for development)
- **Git** (for source installation)

## 🚀 GoonLang Interpreter Setup

### Quick Install
```bash
# Clone GoonLang repository
git clone https://github.com/goonlang/goonlang.git
cd goonlang

# Install system-wide
make install

# Verify installation
goonlang --version
```

### Manual Setup
1. Download GoonLang interpreter
2. Add to system PATH
3. Verify with `goonlang --version`

## ⚙️ Configuration

After installation, configure the extension:

1. **Open VS Code Settings** (Ctrl+, or Cmd+,)
2. **Search for "goonlang"**
3. **Configure settings:**

```json
{
  "goonlang.interpreterPath": "goonlang",
  "goonlang.enableLinting": true,
  "goonlang.enableFormatting": true,
  "goonlang.showAST": false,
  "goonlang.debugMode": false
}
```

### Custom Interpreter Path
If GoonLang is not in PATH:

```json
{
  "goonlang.interpreterPath": "/path/to/goonlang"
}
```

Windows example:
```json
{
  "goonlang.interpreterPath": "C:\\Program Files\\GoonLang\\goonlang.exe"
}
```

## 🎨 Theme Setup

1. **Open Command Palette** (Ctrl+Shift+P)
2. **Type** "Preferences: Color Theme"
3. **Select** "GoonLang Dark" or "GoonLang Light"

## 🧪 Verify Installation

1. **Create a new file** with `.goon` extension
2. **Type:** `i like femboys`
3. **Check syntax highlighting** is applied
4. **Press Ctrl+F5** to run the file
5. **Verify output** shows "Hello World"

## 🔍 Troubleshooting

### Extension Not Working
- Check VS Code version (must be 1.74.0+)
- Reload VS Code window
- Check extension is enabled in Extensions panel

### Syntax Highlighting Missing
- Verify file has `.goon` extension
- Check language mode in status bar
- Try reloading VS Code

### Cannot Run Files
- Verify GoonLang interpreter is installed
- Check `goonlang.interpreterPath` setting
- Test interpreter in terminal: `goonlang --version`

### IntelliSense Not Working
- Check file is recognized as GoonLang
- Verify extension is active
- Try restarting VS Code

### Common Issues

#### "Command not found: goonlang"
```bash
# Add GoonLang to PATH
export PATH=$PATH:/path/to/goonlang
```

#### "Extension not found"
- Check spelling: "GoonLang" (not "goonlang")
- Verify publisher: "goonlang-foundation"
- Try direct marketplace link

#### "VSIX installation failed"
- Check VS Code version compatibility
- Try installing from marketplace instead
- Verify VSIX file is not corrupted

## 🆕 Updates

### Automatic Updates
- Extensions auto-update by default
- Check "Auto Update" in Extensions settings

### Manual Updates
1. Open Extensions panel
2. Find GoonLang extension
3. Click "Update" if available

### Beta Versions
- Install from VSIX for pre-release versions
- Check GitHub releases for beta builds

## 🗑️ Uninstallation

1. **Open Extensions panel** (Ctrl+Shift+X)
2. **Find GoonLang extension**
3. **Click gear icon** → "Uninstall"
4. **Reload VS Code** if prompted

## 📞 Support

### Getting Help
- [GitHub Issues](https://github.com/goonlang/vscode-goonlang/issues)
- [Documentation](https://goonlang.org/docs)
- [Community Discord](https://discord.gg/goonlang)

### Reporting Bugs
1. Check existing issues first
2. Include VS Code version
3. Include extension version
4. Provide reproduction steps
5. Include error messages/logs

## 🎉 Next Steps

After installation:
1. **Read the [Quick Start Guide](README.md#quick-start)**
2. **Try the [code snippets](README.md#snippets)**
3. **Explore [example programs](../examples/)**
4. **Join the [community](https://discord.gg/goonlang)**

---

**Welcome to GoonLang development! 🏳️‍⚧️✨**
