#!/bin/bash

# GoonLang VS Code Extension Publish Script

set -e

echo "🏳️‍⚧️ Publishing GoonLang VS Code Extension..."

# Check if vsce is installed
if ! command -v vsce &> /dev/null; then
    echo "📦 Installing vsce..."
    npm install -g vsce
fi

# Check if user is logged in
echo "🔐 Checking authentication..."
vsce ls-publishers

# Build the extension
echo "🔨 Building extension..."
./scripts/build.sh

# Publish to marketplace
echo "🚀 Publishing to VS Code Marketplace..."
vsce publish

echo "✅ Extension published successfully!"
echo "🌐 Available at: https://marketplace.visualstudio.com/items?itemName=goonlang-foundation.goonlang"
echo ""
echo "📊 To check stats:"
echo "vsce show goonlang-foundation.goonlang"
