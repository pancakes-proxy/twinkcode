// GoonLang Syntax Highlighting for Prism.js

// Define GoonLang language for Prism.js
Prism.languages.goon = {
    'comment': {
        pattern: /\/\/.*$/m,
        greedy: true
    },
    'string': {
        pattern: /"(?:[^"\\]|\\.)*"/,
        greedy: true
    },
    'goon-phrase': {
        pattern: /\bi\s+like\s+femboys\b/i,
        alias: 'keyword'
    },
    'goon-shout': {
        pattern: /\bI\s+LIKE\s+FEMBOYS\b/,
        alias: 'keyword'
    },
    'goon-mixed': {
        pattern: /\b[iI]\s+[lL][iI][kK][eE]\s+[fF][eE][mM][bB][oO][yY][sS]\b/,
        alias: 'keyword'
    },
    'goon-reverse': {
        pattern: /\bsyobmef\s+ekil\s+i\b/,
        alias: 'keyword'
    },
    'goon-number': {
        pattern: /\bi\s+like\s+\d+\s+femboys\b/i,
        alias: 'keyword'
    },
    'goon-algorithm': {
        pattern: /\bi\s+like\s+femboys\s+(?:fibonacci|prime|factorial|sort|art|binary|hex|reverse|palindrome|class|import|export|try|catch|throw|length|type|clone)\b/i,
        alias: 'function'
    },
    'number': /\b\d+(?:\.\d+)?\b/,
    'goon-operator': {
        pattern: /[=!<>]=?|[+\-*/%^&|~]/,
        alias: 'operator'
    },
    'goon-punctuation-exclamation': {
        pattern: /!{1,5}/,
        alias: 'punctuation'
    },
    'goon-punctuation-question': {
        pattern: /\?{1,3}/,
        alias: 'punctuation'
    },
    'goon-punctuation-dots': {
        pattern: /\.{1,3}/,
        alias: 'punctuation'
    },
    'punctuation': /[{}[\]();:,.$@#]/,
    'keyword': /\b(?:class|function|if|else|while|for|return|import|export|try|catch|throw|async|await|new|var|let|const)\b/,
    'boolean': /\b(?:true|false|null|undefined)\b/,
    'operator': /[=!<>]=?|[+\-*/%^&|~]|&&|\|\|/
};

// Add GoonLang language alias
Prism.languages.goonlang = Prism.languages.goon;

// Custom highlighting for specific GoonLang patterns
document.addEventListener('DOMContentLoaded', function() {
    // Enhanced syntax highlighting for GoonLang
    function enhanceGoonLangHighlighting() {
        const goonCodeBlocks = document.querySelectorAll('code.language-goon, code.language-goonlang');
        
        goonCodeBlocks.forEach(codeBlock => {
            let html = codeBlock.innerHTML;
            
            // Highlight core phrases with special styling
            html = html.replace(
                /(\bi\s+like\s+femboys\b)(?!\s+(?:fibonacci|prime|factorial|sort|art|binary|hex|reverse|palindrome|class|import|export|try|catch|throw|length|type|clone))/gi,
                '<span class="token goon-phrase">$1</span>'
            );
            
            // Highlight shout phrases
            html = html.replace(
                /\bI\s+LIKE\s+FEMBOYS\b/g,
                '<span class="token goon-shout">I LIKE FEMBOYS</span>'
            );
            
            // Highlight mixed case phrases
            html = html.replace(
                /\b[iI]\s+[lL][iI][kK][eE]\s+[fF][eE][mM][bB][oO][yY][sS]\b/g,
                function(match) {
                    if (match !== 'i like femboys' && match !== 'I LIKE FEMBOYS') {
                        return `<span class="token goon-mixed">${match}</span>`;
                    }
                    return match;
                }
            );
            
            // Highlight reverse phrases
            html = html.replace(
                /\bsyobmef\s+ekil\s+i\b/g,
                '<span class="token goon-reverse">syobmef ekil i</span>'
            );
            
            // Highlight number phrases
            html = html.replace(
                /(\bi\s+like\s+)(\d+)(\s+femboys\b)/gi,
                '$1<span class="token number">$2</span>$3'
            );
            
            // Highlight algorithm keywords
            html = html.replace(
                /(\bi\s+like\s+femboys\s+)(fibonacci|prime|factorial|sort|art|binary|hex|reverse|palindrome|class|import|export|try|catch|throw|length|type|clone)\b/gi,
                '$1<span class="token goon-algorithm">$2</span>'
            );
            
            // Highlight special operators
            html = html.replace(
                /([=!<>]=?|[+\-*/%^&|~]|\$|@|#)/g,
                '<span class="token goon-operator">$1</span>'
            );
            
            // Highlight exclamation patterns
            html = html.replace(
                /(!{1,5})/g,
                '<span class="token goon-punctuation-exclamation">$1</span>'
            );
            
            // Highlight question patterns
            html = html.replace(
                /(\?{1,3})/g,
                '<span class="token goon-punctuation-question">$1</span>'
            );
            
            // Highlight dot patterns
            html = html.replace(
                /(\.{1,3})/g,
                '<span class="token goon-punctuation-dots">$1</span>'
            );
            
            codeBlock.innerHTML = html;
        });
    }
    
    // Run enhancement after Prism.js has processed the code
    setTimeout(enhanceGoonLangHighlighting, 100);
    
    // Add line numbers to code blocks
    function addLineNumbers() {
        const codeBlocks = document.querySelectorAll('pre[class*="language-"]');
        
        codeBlocks.forEach(pre => {
            if (pre.classList.contains('line-numbers')) return;
            
            const code = pre.querySelector('code');
            if (!code) return;
            
            const lines = code.textContent.split('\n');
            if (lines.length <= 1) return;
            
            pre.classList.add('line-numbers');
            
            const lineNumbersWrapper = document.createElement('span');
            lineNumbersWrapper.className = 'line-numbers-rows';
            
            lines.forEach((line, index) => {
                if (index === lines.length - 1 && line === '') return;
                
                const lineNumber = document.createElement('span');
                lineNumber.textContent = (index + 1).toString();
                lineNumbersWrapper.appendChild(lineNumber);
            });
            
            pre.appendChild(lineNumbersWrapper);
        });
    }
    
    // Add line numbers after a delay
    setTimeout(addLineNumbers, 150);
    
    // Add language labels to code blocks
    function addLanguageLabels() {
        const codeBlocks = document.querySelectorAll('pre[class*="language-"]');
        
        codeBlocks.forEach(pre => {
            const className = pre.className;
            const languageMatch = className.match(/language-(\w+)/);
            
            if (languageMatch) {
                const language = languageMatch[1];
                let displayName = language;
                
                if (language === 'goon' || language === 'goonlang') {
                    displayName = 'GoonLang';
                }
                
                pre.setAttribute('data-language', displayName);
            }
        });
    }
    
    addLanguageLabels();
    
    // Highlight specific lines
    function highlightLines() {
        const codeBlocks = document.querySelectorAll('pre[data-line]');
        
        codeBlocks.forEach(pre => {
            const linesToHighlight = pre.getAttribute('data-line');
            if (!linesToHighlight) return;
            
            const code = pre.querySelector('code');
            if (!code) return;
            
            const lines = code.innerHTML.split('\n');
            const highlightRanges = linesToHighlight.split(',');
            
            highlightRanges.forEach(range => {
                const [start, end] = range.split('-').map(n => parseInt(n.trim()));
                const endLine = end || start;
                
                for (let i = start - 1; i < endLine && i < lines.length; i++) {
                    lines[i] = `<span class="line-highlight">${lines[i]}</span>`;
                }
            });
            
            code.innerHTML = lines.join('\n');
        });
    }
    
    setTimeout(highlightLines, 200);
});

// Custom Prism.js hooks for GoonLang
Prism.hooks.add('before-highlight', function(env) {
    if (env.language === 'goon' || env.language === 'goonlang') {
        // Pre-process GoonLang code if needed
        env.code = env.code.trim();
    }
});

Prism.hooks.add('after-highlight', function(env) {
    if (env.language === 'goon' || env.language === 'goonlang') {
        // Post-process GoonLang code if needed
        // Add any additional styling or functionality
    }
});

// Export for use in other scripts
window.GoonLangSyntax = {
    enhanceHighlighting: function() {
        // Re-run syntax highlighting enhancement
        setTimeout(() => {
            const event = new Event('DOMContentLoaded');
            document.dispatchEvent(event);
        }, 100);
    }
};
