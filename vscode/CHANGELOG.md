# Change Log

All notable changes to the GoonLang VS Code extension will be documented in this file.

## [2.0.0] - 2024-12-15

### Added
- **Complete rewrite** for GoonLang Enterprise Edition
- **Advanced syntax highlighting** with 15+ token types
- **IntelliSense support** with context-aware autocompletion
- **Hover information** for all GoonLang constructs
- **Real-time diagnostics** and error checking
- **Debugging support** with integrated debugger
- **AST visualization** command
- **Token stream analysis** command
- **Code formatting** with automatic indentation
- **Integrated REPL** support
- **Custom themes** (GoonLang Dark & Light)
- **30+ code snippets** for common patterns
- **File icons** for .goon files
- **Bracket matching** and auto-closing pairs
- **Comment toggling** support
- **Folding support** for code regions

### Enhanced
- **Syntax highlighting** now supports:
  - Core phrase variations (basic, shout, mixed case, reverse)
  - Special algorithms (fibonacci, prime, factorial, etc.)
  - All operators (+, -, *, /, %, ^, ==, !=, etc.)
  - Punctuation patterns (!, ?, ., !!!, ???, etc.)
  - String literals and comments
  - Numbers (decimal, hex, binary)
  - Keywords and control flow

### Commands
- `goonlang.runFile` - Run current GoonLang file (Ctrl+F5)
- `goonlang.debugFile` - Debug current file (F5)
- `goonlang.showAST` - Show Abstract Syntax Tree
- `goonlang.showTokens` - Show token stream
- `goonlang.formatDocument` - Format code (Shift+Alt+F)
- `goonlang.startREPL` - Start interactive REPL (Ctrl+Shift+R)

### Configuration
- `goonlang.interpreterPath` - Path to GoonLang interpreter
- `goonlang.enableLinting` - Enable/disable linting
- `goonlang.enableFormatting` - Enable/disable formatting
- `goonlang.showAST` - Show AST in output
- `goonlang.debugMode` - Enable debug mode by default

### Themes
- **GoonLang Dark** - Professional dark theme with pink accents
- **GoonLang Light** - Clean light theme with vibrant colors
- Custom color schemes optimized for GoonLang syntax

### Snippets
- Basic operations (hello, shout, var, assign, etc.)
- Control flow (if, loop, func, class)
- Advanced features (server, ml, async, import)
- Mathematical operations (math, compare, fib, prime)
- Debugging and utilities (debug, random, binary, hex)

## [1.0.0] - 2024-06-15

### Added
- Initial release of GoonLang VS Code extension
- Basic syntax highlighting for .goon files
- File association for GoonLang files
- Simple language configuration
- Basic TextMate grammar

### Features
- Syntax highlighting for core "i like femboys" phrase
- Comment support with //
- String literal highlighting
- Basic operator recognition
- File extension association (.goon)

---

## Upcoming Features

### [2.1.0] - Planned
- **Language Server Protocol** support
- **Go to Definition** functionality
- **Find All References** command
- **Rename Symbol** support
- **Code lens** for functions and classes
- **Outline view** support
- **Breadcrumb navigation**
- **Symbol search** in workspace

### [2.2.0] - Planned
- **Integrated testing** framework
- **Code coverage** visualization
- **Performance profiling** integration
- **Git integration** enhancements
- **Collaborative editing** support
- **Live share** compatibility

### [3.0.0] - Future
- **Visual programming** interface
- **Drag-and-drop** code construction
- **Interactive tutorials** and learning mode
- **AI-powered** code suggestions
- **Cloud synchronization** of settings
- **Mobile development** support

---

## Bug Fixes

### [2.0.0]
- Fixed syntax highlighting edge cases
- Improved error message clarity
- Enhanced performance for large files
- Fixed bracket matching issues
- Resolved theme compatibility problems

### [1.0.0]
- Initial stable release

---

## Breaking Changes

### [2.0.0]
- Complete rewrite of extension architecture
- New configuration schema
- Updated command names and shortcuts
- Requires GoonLang 2.0+ interpreter

---

## Migration Guide

### From 1.x to 2.x
1. Update GoonLang interpreter to version 2.0+
2. Update extension settings:
   - `goonlang.interpreter` → `goonlang.interpreterPath`
3. New themes available - switch to GoonLang Dark/Light
4. New snippets and commands available
5. Enhanced syntax highlighting may change appearance

---

## Acknowledgments

- **GoonLang Community** - For feedback and feature requests
- **VS Code Team** - For excellent extension APIs
- **TextMate** - For grammar syntax inspiration
- **Language Server Protocol** - For standardized language features

---

**For more information, visit [goonlang.org](https://goonlang.org)**
