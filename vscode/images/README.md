# GoonLang VS Code Extension Icons

This directory contains the icons used by the GoonLang VS Code extension.

## Required Icons

### Extension Icon
- `icon.png` (128x128) - Main extension icon shown in marketplace
- Should feature the GoonLang logo with trans pride colors

### File Icons
- `file-icon-light.svg` - File icon for light themes
- `file-icon-dark.svg` - File icon for dark themes
- Should be simple, recognizable icons for .goon files

## Icon Guidelines

### Colors
- Primary: #FF69B4 (Hot Pink)
- Secondary: #55CDFC (Light Blue)
- Accent: #F7A8B8 (Light Pink)
- Background: #FFFFFF (White) or #000000 (Black)

### Style
- Modern, flat design
- Clear at small sizes (16x16)
- Consistent with VS Code icon style
- Professional appearance

### File Format
- PNG for raster images (icon.png)
- SVG for vector images (file icons)
- High resolution for marketplace display

## Creating Icons

You can create these icons using:
- Adobe Illustrator
- Figma
- Inkscape (free)
- Canva
- Any vector graphics editor

## Placeholder Icons

Until custom icons are created, the extension will use default VS Code icons.

## Icon Specifications

### Extension Icon (icon.png)
- Size: 128x128 pixels
- Format: PNG
- Background: Transparent or solid color
- Content: GoonLang logo or representative symbol

### File Icons (SVG)
- Format: SVG
- Viewbox: 0 0 16 16
- Colors: Optimized for light/dark themes
- Simple, recognizable design

## Example SVG Structure

```svg
<svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
  <rect width="16" height="16" fill="#FF69B4" rx="2"/>
  <text x="8" y="12" text-anchor="middle" fill="white" font-size="8" font-family="monospace">G</text>
</svg>
```

This creates a simple pink square with a "G" for GoonLang.
