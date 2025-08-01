# Orphaned CSS Files to Delete

These CSS files are no longer needed since they've been converted to SCSS partials:

## Base Files (converted to _sass/base/):
- `assets/css/base/reset.css` → DELETE (now `_sass/base/_reset.scss`)
- `assets/css/base/typography.css` → DELETE (now `_sass/base/_typography.scss`)
- `assets/css/base/variables.css` → DELETE (now in `_sass/_variables.scss`)

## Component Files (converted to _sass/components/):
- `assets/css/components/buttons.css` → DELETE (now `_sass/components/_buttons.scss`)
- `assets/css/components/header.css` → DELETE (now `_sass/components/_header.scss`)
- `assets/css/components/footer.css` → DELETE (now `_sass/components/_footer.scss`)
- `assets/css/components/cards.css` → NEEDS CONVERSION
- `assets/css/components/forms.css` → NEEDS CONVERSION
- `assets/css/components/testimonials.css` → NEEDS CONVERSION
- `assets/css/components/images.css` → NEEDS CONVERSION
- `assets/css/components/authority-section.css` → NEEDS CONVERSION
- `assets/css/components/game-model-feature.css` → NEEDS CONVERSION

## Layout Files (need conversion):
- `assets/css/layout/grid.css` → NEEDS CONVERSION

## Page Files (need conversion):
- `assets/css/pages/sessions.css` → NEEDS CONVERSION
- `assets/css/pages/complete-system.css` → NEEDS CONVERSION

## Other orphaned files:
- `assets/css/360tft-styles.css` → CHECK IF STILL NEEDED
- `assets/css/academy-specific.css` → CHECK IF STILL NEEDED
- `assets/css/compass-specific.css` → CHECK IF STILL NEEDED
- `assets/css/free-product.css` → CHECK IF STILL NEEDED
- `assets/css/game-model-complete.css` → DELETE (replaced by _sass/pages/_game-model.scss)
- `assets/css/homepage-animations.css` → CHECK IF STILL NEEDED
- `assets/css/homepage-problem-solving.css` → CHECK IF STILL NEEDED
- `assets/css/main-consolidated.css` → DELETE (redundant)
- `assets/css/main-new.css` → DELETE (redundant)
- `assets/css/main-optimized.css` → DELETE (redundant)
- `assets/css/product-pages.css` → CHECK IF STILL NEEDED
- `assets/css/testimonials.css` → DELETE (redundant with components/testimonials)

## Status:
- ✅ CONVERTED: base files, header, footer, buttons
- 🔄 IN PROGRESS: Other component files
- ❌ TO DELETE: Files listed above once conversion is complete