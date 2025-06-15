#!/bin/bash
# GoonLang Test Runner

echo "🏳️‍⚧️ GoonLang Test Suite 🏳️‍⚧️"
echo "================================"

# Make sure interpreter is executable
chmod +x goonlang.py

# Test all example files
for file in examples/*.goon; do
    if [ -f "$file" ]; then
        echo ""
        echo "Testing: $file"
        echo "-------------------"
        ./goonlang.py "$file"
        echo ""
    fi
done

echo "🎉 All tests completed! 🎉"
