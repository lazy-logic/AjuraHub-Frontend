# Material Icons Fix Guide

## Issue Description
When applying brand typography with Raleway font using aggressive CSS selectors like `* { font-family: 'Raleway', sans-serif !important; }`, Material Icons break and display as text instead of symbols.

## Root Cause
The universal selector (`*`) overrides the Material Icons font family, preventing icons from rendering properly.

## Solution Pattern

### 1. Font Loading
Always include both fonts in the HTML head:
```html
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```

### 2. CSS Exclusions
Use selective targeting that excludes icon elements:
```css
/* ❌ WRONG - Breaks icons */
* {
    font-family: 'Raleway', sans-serif !important;
}

/* ✅ CORRECT - Preserves icons */
*:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
    font-family: 'Raleway', sans-serif !important;
}
```

### 3. Material Icons CSS Properties
Ensure Material Icons have proper CSS properties:
```css
.material-icons {
    font-family: 'Material Icons';
    font-weight: normal;
    font-style: normal;
    font-size: 24px;
    line-height: 1;
    letter-spacing: normal;
    text-transform: none;
    display: inline-block;
    white-space: nowrap;
    word-wrap: normal;
    direction: ltr;
    font-feature-settings: 'liga';
    -webkit-font-smoothing: antialiased;
    -webkit-font-feature-settings: 'liga';
}
```

## Complete Implementation Template

```html
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<style>
/* Brand typography - excludes icons */
*:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
    font-family: 'Raleway', sans-serif !important;
}

/* Material Icons properties */
.material-icons {
    font-family: 'Material Icons' !important;
    font-weight: normal;
    font-style: normal;
    font-size: 24px;
    line-height: 1;
    letter-spacing: normal;
    text-transform: none;
    display: inline-block;
    white-space: nowrap;
    word-wrap: normal;
    direction: ltr;
    font-feature-settings: 'liga';
    -webkit-font-smoothing: antialiased;
    -webkit-font-feature-settings: 'liga';
}

/* Typography classes */
.heading-1 { font-size: 3rem; font-weight: 700; line-height: 1.1; }
.heading-2 { font-size: 2.25rem; font-weight: 600; line-height: 1.2; }
.sub-heading { font-size: 1.5rem; font-weight: 500; line-height: 1.4; }
.body-text { font-size: 1rem; font-weight: 400; line-height: 1.6; }
.button-label { font-size: 0.875rem; font-weight: 600; }
.caption { font-size: 0.75rem; font-weight: 400; }

/* Brand colors */
.brand-primary { color: #0055B8; }
.brand-charcoal { color: #1A1A1A; }
.brand-slate { color: #4D4D4D; }
.brand-light-mist { background-color: #F2F7FB; }
.brand-primary-bg { background-color: #0055B8; }
</style>
```

## Pages Successfully Fixed
- `admin_management.py`
- `notification_management.py`
- `search.py`
- `help_and_support.py`
- `application_tracking.py`
- `jobs.py`
- `job_posting.py`
- `messaging.py`

## Prevention
- Always test icon display after applying global typography changes
- Use the CSS exclusion pattern from the start when implementing brand fonts
- Include Material Icons CSS properties in your base styles
- Test with different icon types (text icons, SVG icons, font icons)

## Testing Checklist
- [ ] Icons display as symbols, not text
- [ ] Brand typography is applied to text elements
- [ ] No console errors related to fonts
- [ ] Icons maintain proper sizing and alignment
- [ ] Responsive behavior works correctly