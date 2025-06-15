// GoonLang Website - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Mobile navigation toggle
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
        });
    }
    
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = targetElement.offsetTop - navbarHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                if (navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                    navToggle.classList.remove('active');
                }
            }
        });
    });
    
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Hide/show navbar on scroll
        if (scrollTop > lastScrollTop && scrollTop > 200) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop;
    });
    
    // Active navigation link highlighting
    const sections = document.querySelectorAll('section[id]');
    const navLinksAll = document.querySelectorAll('.nav-link');
    
    function updateActiveNavLink() {
        const scrollPosition = window.scrollY + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinksAll.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }
    
    window.addEventListener('scroll', updateActiveNavLink);
    updateActiveNavLink(); // Initial call
    
    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.feature-card, .stat, .hero-content, .hero-code');
    animateElements.forEach(el => {
        observer.observe(el);
    });
    
    // Copy code functionality
    function addCopyButtons() {
        const codeBlocks = document.querySelectorAll('pre[class*="language-"]');
        
        codeBlocks.forEach(codeBlock => {
            const wrapper = document.createElement('div');
            wrapper.className = 'code-toolbar';
            codeBlock.parentNode.insertBefore(wrapper, codeBlock);
            wrapper.appendChild(codeBlock);
            
            const toolbar = document.createElement('div');
            toolbar.className = 'toolbar';
            
            const copyButton = document.createElement('button');
            copyButton.className = 'copy-button';
            copyButton.textContent = 'Copy';
            copyButton.addEventListener('click', function() {
                const code = codeBlock.querySelector('code');
                const text = code.textContent;
                
                navigator.clipboard.writeText(text).then(function() {
                    copyButton.textContent = 'Copied!';
                    setTimeout(function() {
                        copyButton.textContent = 'Copy';
                    }, 2000);
                }).catch(function() {
                    // Fallback for older browsers
                    const textArea = document.createElement('textarea');
                    textArea.value = text;
                    document.body.appendChild(textArea);
                    textArea.select();
                    document.execCommand('copy');
                    document.body.removeChild(textArea);
                    
                    copyButton.textContent = 'Copied!';
                    setTimeout(function() {
                        copyButton.textContent = 'Copy';
                    }, 2000);
                });
            });
            
            const toolbarItem = document.createElement('div');
            toolbarItem.className = 'toolbar-item';
            toolbarItem.appendChild(copyButton);
            toolbar.appendChild(toolbarItem);
            wrapper.appendChild(toolbar);
        });
    }
    
    // Add copy buttons after Prism.js loads
    setTimeout(addCopyButtons, 100);
    
    // Terminal typing animation
    function typeWriter(element, text, speed = 50) {
        let i = 0;
        element.textContent = '';
        
        function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        
        type();
    }
    
    // Animate terminal commands
    const terminalCommands = document.querySelectorAll('.terminal .command');
    terminalCommands.forEach((cmd, index) => {
        const originalText = cmd.textContent;
        setTimeout(() => {
            typeWriter(cmd, originalText, 30);
        }, index * 1000);
    });
    
    // Theme toggle functionality
    function initThemeToggle() {
        const themeToggle = document.getElementById('theme-toggle');
        if (!themeToggle) return;
        
        const currentTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', currentTheme);
        
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }
    
    initThemeToggle();
    
    // Search functionality
    function initSearch() {
        const searchInput = document.getElementById('search-input');
        const searchResults = document.getElementById('search-results');
        
        if (!searchInput || !searchResults) return;
        
        let searchTimeout;
        
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            const query = this.value.trim();
            
            if (query.length < 2) {
                searchResults.style.display = 'none';
                return;
            }
            
            searchTimeout = setTimeout(() => {
                performSearch(query);
            }, 300);
        });
        
        function performSearch(query) {
            // Simple search implementation
            const searchableElements = document.querySelectorAll('h1, h2, h3, h4, h5, h6, p');
            const results = [];
            
            searchableElements.forEach(element => {
                const text = element.textContent.toLowerCase();
                if (text.includes(query.toLowerCase())) {
                    results.push({
                        element: element,
                        text: element.textContent,
                        type: element.tagName.toLowerCase()
                    });
                }
            });
            
            displaySearchResults(results, query);
        }
        
        function displaySearchResults(results, query) {
            if (results.length === 0) {
                searchResults.innerHTML = '<div class="search-no-results">No results found</div>';
            } else {
                const resultsHTML = results.slice(0, 5).map(result => {
                    const highlightedText = result.text.replace(
                        new RegExp(query, 'gi'),
                        match => `<mark>${match}</mark>`
                    );
                    
                    return `
                        <div class="search-result-item">
                            <div class="search-result-title">${highlightedText}</div>
                            <div class="search-result-type">${result.type}</div>
                        </div>
                    `;
                }).join('');
                
                searchResults.innerHTML = resultsHTML;
            }
            
            searchResults.style.display = 'block';
        }
        
        // Close search results when clicking outside
        document.addEventListener('click', function(e) {
            if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
                searchResults.style.display = 'none';
            }
        });
    }
    
    initSearch();
    
    // Performance monitoring
    function logPerformance() {
        if ('performance' in window) {
            window.addEventListener('load', function() {
                setTimeout(function() {
                    const perfData = performance.getEntriesByType('navigation')[0];
                    console.log('Page load time:', perfData.loadEventEnd - perfData.loadEventStart, 'ms');
                }, 0);
            });
        }
    }
    
    logPerformance();
});

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Export for use in other scripts
window.GoonLang = {
    debounce,
    throttle
};
