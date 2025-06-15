# I like Femboys 🏳️‍⚧️ - GoonLang Official Website

The official website for GoonLang, the revolutionary programming language with unconventional syntax that proves programming languages are about patterns, not keywords.

## 🌟 Website Features

### 🎨 **Professional Design**
- **Trans Pride Colors** - Beautiful color scheme featuring #FF69B4, #55CDFC, and #F7A8B8
- **Responsive Layout** - Perfect on desktop, tablet, and mobile devices
- **Modern UI/UX** - Clean, accessible, and professional interface
- **Custom Animations** - Smooth transitions and engaging interactions

### 📚 **Comprehensive Documentation**
- **Complete Language Reference** - Every syntax pattern documented
- **Installation Guides** - Multiple installation methods for all platforms
- **Code Examples** - From basic to advanced programming concepts
- **API Documentation** - Full standard library reference
- **Best Practices** - Professional development guidelines

### 🎯 **Interactive Features**
- **Syntax Highlighting** - Custom GoonLang syntax highlighting
- **Code Examples** - Runnable code snippets with copy functionality
- **Search Functionality** - Find documentation quickly
- **Mobile Navigation** - Touch-friendly mobile interface
- **Dark/Light Themes** - Customizable appearance

### 🚀 **Performance Optimized**
- **Fast Loading** - Optimized assets and minimal dependencies
- **SEO Friendly** - Proper meta tags and semantic HTML
- **Accessibility** - WCAG 2.1 compliant design
- **Progressive Enhancement** - Works without JavaScript

## 📁 File Structure

```
site/
├── index.html              # Homepage
├── documentation.html      # Complete documentation
├── examples.html          # Code examples and tutorials
├── download.html          # Installation and download
├── community.html         # Community and contributing
├── assets/
│   ├── css/
│   │   ├── main.css       # Core styles and variables
│   │   ├── components.css # UI components
│   │   └── syntax-highlighting.css # Code highlighting
│   ├── js/
│   │   ├── main.js        # Core functionality
│   │   └── syntax-highlighting.js # GoonLang syntax
│   └── images/
│       ├── favicon.ico    # Site favicon
│       └── icons/         # Various icons and graphics
└── README.md              # This file
```

## 🛠️ **Technologies Used**

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS Grid and Flexbox
- **JavaScript (ES6+)** - Interactive functionality
- **Prism.js** - Syntax highlighting
- **Custom GoonLang Grammar** - Specialized syntax support

### Design System
- **CSS Custom Properties** - Consistent theming
- **Component-Based Architecture** - Reusable UI components
- **Mobile-First Design** - Responsive breakpoints
- **Accessibility Features** - Screen reader support, keyboard navigation

### Performance
- **Optimized Assets** - Minified CSS/JS
- **Lazy Loading** - Images and content
- **Caching Headers** - Browser caching optimization
- **CDN Ready** - Optimized for content delivery networks

## 🎨 **Design Guidelines**

### Color Palette
```css
/* Trans Pride Colors */
--trans-blue: #55CDFC;
--trans-pink: #F7A8B8;
--trans-white: #FFFFFF;

/* Primary Colors */
--primary: #FF69B4;
--primary-dark: #FF1493;
--primary-light: #FFB6C1;

/* Secondary Colors */
--secondary: #55CDFC;
--accent: #F7A8B8;
```

### Typography
- **Primary Font**: Inter (Sans-serif)
- **Code Font**: JetBrains Mono (Monospace)
- **Font Weights**: 300, 400, 500, 600, 700, 800

### Spacing System
- **Base Unit**: 0.25rem (4px)
- **Scale**: 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32
- **Consistent Spacing** throughout all components

## 🚀 **Development**

### Local Development
```bash
# Clone the repository
git clone https://github.com/goonlang/goonlang.git
cd goonlang/site

# Serve locally (Python)
python3 -m http.server 8000

# Or with Node.js
npx serve .

# Visit http://localhost:8000
```

### Building for Production
```bash
# Minify CSS
npx clean-css-cli -o assets/css/main.min.css assets/css/*.css

# Minify JavaScript
npx terser assets/js/*.js -o assets/js/main.min.js

# Optimize images
npx imagemin assets/images/* --out-dir=assets/images/optimized
```

### Testing
```bash
# HTML validation
npx html-validate *.html

# CSS validation
npx stylelint assets/css/*.css

# JavaScript linting
npx eslint assets/js/*.js

# Accessibility testing
npx pa11y http://localhost:8000
```

## 📱 **Responsive Breakpoints**

```css
/* Mobile First Approach */
/* Small devices (phones) */
@media (max-width: 768px) { }

/* Medium devices (tablets) */
@media (max-width: 1024px) { }

/* Large devices (desktops) */
@media (min-width: 1025px) { }

/* Extra large devices */
@media (min-width: 1440px) { }
```

## ♿ **Accessibility Features**

- **Semantic HTML** - Proper heading hierarchy and landmarks
- **ARIA Labels** - Screen reader support
- **Keyboard Navigation** - Full keyboard accessibility
- **Color Contrast** - WCAG AA compliant contrast ratios
- **Focus Indicators** - Clear focus states
- **Alt Text** - Descriptive image alternatives
- **Skip Links** - Navigation shortcuts

## 🔍 **SEO Optimization**

- **Meta Tags** - Proper title, description, and keywords
- **Open Graph** - Social media sharing optimization
- **Twitter Cards** - Twitter sharing optimization
- **Structured Data** - Schema.org markup
- **Sitemap** - XML sitemap for search engines
- **Robots.txt** - Search engine crawling instructions

## 🌐 **Browser Support**

- **Chrome** 90+
- **Firefox** 88+
- **Safari** 14+
- **Edge** 90+
- **Mobile Safari** 14+
- **Chrome Mobile** 90+

## 📊 **Performance Metrics**

Target performance scores:
- **Lighthouse Performance**: 95+
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1
- **Time to Interactive**: < 3.5s

## 🤝 **Contributing**

We welcome contributions to improve the website! Here's how you can help:

### Content
- Fix typos and grammar
- Improve documentation clarity
- Add new examples
- Translate content

### Design
- Improve accessibility
- Enhance mobile experience
- Add new components
- Optimize performance

### Development
- Fix bugs
- Add new features
- Improve code quality
- Write tests

### Contribution Process
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 **License**

This website is licensed under the MIT License. See [LICENSE](../LICENSE) for details.

## 🙏 **Acknowledgments**

- **GoonLang Community** - For feedback and contributions
- **Trans Community** - For inspiration and support
- **Web Standards** - For accessibility and performance guidelines
- **Open Source Projects** - For tools and libraries used

---

**Made with 💖 and 🏳️‍⚧️ by the GoonLang Foundation**

Visit the live website: [https://goonlang.org](https://goonlang.org)
