# GoonLang VS Code Extension

Professional VS Code extension for GoonLang - the advanced programming language with unconventional syntax.

## Features

### 🎨 **Syntax Highlighting**
- Beautiful syntax highlighting for all GoonLang constructs
- Special highlighting for the core "i like femboys" phrase
- Color-coded operators, keywords, and special functions
- Support for both dark and light themes

### 🧠 **IntelliSense**
- Smart autocompletion for GoonLang syntax
- Context-aware suggestions
- Operator and function completions
- Snippet support for common patterns

### 🔍 **Language Support**
- Hover information for GoonLang constructs
- Real-time syntax validation
- Error highlighting and diagnostics
- Bracket matching and auto-closing

### 🚀 **Execution & Debugging**
- Run GoonLang files directly from VS Code
- Debug mode with detailed output
- AST visualization
- Token stream analysis
- Integrated REPL

### 🎨 **Themes**
- **GoonLang Dark** - Professional dark theme
- **GoonLang Light** - Clean light theme
- Custom color schemes optimized for GoonLang

### 📝 **Code Snippets**
- 30+ built-in snippets for common patterns
- Function definitions and class templates
- Web server and ML boilerplate
- Mathematical operations

## Installation

### From VS Code Marketplace
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "GoonLang"
4. Click Install

### From VSIX
1. Download the `.vsix` file
2. Open VS Code
3. Run `Extensions: Install from VSIX...`
4. Select the downloaded file

## Quick Start

1. Create a new file with `.goon` extension
2. Start typing `i like femboys`
3. Use Ctrl+Space for autocompletion
4. Press Ctrl+F5 to run the file

## Commands

| Command | Shortcut | Description |
|---------|----------|-------------|
| Run File | Ctrl+F5 | Execute current GoonLang file |
| Debug File | F5 | Run in debug mode |
| Start REPL | Ctrl+Shift+R | Open interactive REPL |
| Show AST | - | Display Abstract Syntax Tree |
| Show Tokens | - | Show token stream |
| Format Document | Shift+Alt+F | Auto-format code |

## Configuration

Configure the extension in VS Code settings:

```json
{
  "goonlang.interpreterPath": "goonlang",
  "goonlang.enableLinting": true,
  "goonlang.enableFormatting": true,
  "goonlang.showAST": false,
  "goonlang.debugMode": false
}
```

## Snippets

Type these prefixes and press Tab:

- `hello` → Basic hello world
- `func` → Function definition
- `class` → Class definition
- `if` → Conditional statement
- `loop` → Loop construct
- `server` → Web server template
- `ml` → Machine learning setup

## Syntax Examples

### Basic Operations
```goon
i like femboys          // Hello World
I LIKE FEMBOYS          // Shout
i like femboys!         // Declare/increment
i like femboys?         // Query/print
i like femboys=         // Assign
i like femboys$         // Retrieve
```

### Advanced Features
```goon
// Object-oriented programming
i like femboys class Person:
    i like femboys name=
    i like femboys greet():
        i like femboys

// Web development
i like femboys import "goon-web"
i like femboys app = new GoonApp()

// Machine learning
i like femboys import "goon-ml"
i like femboys network = new NeuralNetwork()
```

## Themes

The extension includes two custom themes:

- **GoonLang Dark** - Optimized for dark mode development
- **GoonLang Light** - Clean and professional light theme

Both themes feature:
- Pink accent colors (#FF69B4)
- Special highlighting for core phrases
- Distinct colors for different operators
- Professional color palette

## File Types

| Extension | Description |
|-----------|-------------|
| `.goon` | GoonLang source files |
| `.goonlib` | GoonLang library files |
| `.goonc` | GoonLang compiled bytecode |

## Requirements

- VS Code 1.74.0 or higher
- GoonLang interpreter installed and in PATH

## Extension Development

### Building
```bash
npm install
npm run compile
```

### Testing
```bash
npm run test
```

### Packaging
```bash
npm run package
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Support

- [GitHub Issues](https://github.com/goonlang/vscode-goonlang/issues)
- [Documentation](https://goonlang.org/docs)
- [Community Discord](https://discord.gg/goonlang)

## License

MIT License - see [LICENSE](LICENSE) for details.

## Changelog

### 2.0.0
- Complete rewrite for GoonLang Enterprise Edition
- Advanced syntax highlighting
- IntelliSense and autocompletion
- Debugging support
- Custom themes
- 30+ code snippets

### 1.0.0
- Initial release
- Basic syntax highlighting
- File association

---

**Made with 💖 by the GoonLang Foundation**
