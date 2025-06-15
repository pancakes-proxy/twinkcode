#!/bin/bash

# GoonLang VS Code Extension Build Script

set -e

echo "🏳️‍⚧️ Building GoonLang VS Code Extension..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Lint the code
echo "🔍 Linting code..."
npm run lint

# Compile TypeScript
echo "🔨 Compiling TypeScript..."
npm run compile

# Run tests
echo "🧪 Running tests..."
npm run test

# Package the extension
echo "📦 Packaging extension..."
npm run package

echo "✅ Build completed successfully!"
echo "📁 Extension package created: goonlang-*.vsix"
echo ""
echo "To install the extension:"
echo "1. Open VS Code"
echo "2. Press Ctrl+Shift+P"
echo "3. Type 'Extensions: Install from VSIX...'"
echo "4. Select the generated .vsix file"
echo ""
echo "🎉 Happy coding with GoonLang!"
