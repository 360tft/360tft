# Missing CSS Classes Analysis for Game Model Page

## Classes Used in game-model.md vs Available in main.scss

### ✅ Available Classes (already in main.scss):
- `.container` - defined line 54
- `.hero` - defined line 267
- `.testimonial` - defined line 309
- `.testimonial-text` - defined line 317
- `.testimonial-author` - defined line 323
- `.card` (similar functionality to content-card)

### ❌ Missing Classes (need to be added to main.scss):

#### Hero Section Classes:
- `.sticky-cta` - floating CTA button
- `.game-model-hero` - specific hero styling
- `.hero-content` - hero content wrapper
- `.hero-badge` - product badge styling
- `.hero-subtitle` - subtitle styling
- `.hero-description` - description text
- `.hero-cta-group` - CTA button grouping
- `.hero-cta` - primary CTA button
- `.hero-cta-secondary` - secondary CTA button

#### Pricing & Product Classes:
- `.pricing-preview` - pricing preview box
- `.launch-price` - launch price styling
- `.regular-price` - regular price styling
- `.price-description` - price description text
- `.pricing` - pricing section
- `.pricing-subtitle` - pricing subtitle
- `.pricing-card` - pricing card container
- `.launch-special` - launch special section
- `.price-comparison` - price comparison area
- `.regular-price-strike` - strikethrough price
- `.launch-price-big` - large price display
- `.savings` - savings badge
- `.what-you-get` - benefits section
- `.pricing-features` - pricing features list
- `.cta-purchase` - purchase button
- `.payment-security` - security text
- `.guarantee-highlight` - guarantee section

#### Content & Layout Classes:
- `.problem-section` - problem section
- `.section-header` - section header
- `.problem-solution` - problem/solution wrapper
- `.problem-side` - problem side
- `.solution-side` - solution side
- `.problem-list` - problem list
- `.solution-list` - solution list
- `.whats-inside` - what's inside section
- `.content-grid` - content grid layout
- `.content-card` - content card
- `.content-icon` - content icons
- `.content-features` - feature lists
- `.methodology-highlight` - methodology section
- `.methodology-steps` - methodology steps
- `.method-step` - individual method step

#### Testimonials Classes:
- `.testimonials` - testimonials section (different from .testimonial)
- `.testimonials-grid` - testimonials grid layout
- `.testimonial-role` - testimonial role text

#### Upgrade & Final CTA Classes:
- `.upgrade-offer` - upgrade offer section
- `.upgrade-content` - upgrade content wrapper
- `.upgrade-subtitle` - upgrade subtitle
- `.upgrade-details` - upgrade details
- `.upgrade-math` - upgrade math calculation
- `.upgrade-item` - upgrade line items
- `.upgrade-total` - upgrade total
- `.upgrade-features` - upgrade features
- `.upgrade-feature` - individual upgrade feature
- `.upgrade-guarantee` - upgrade guarantee text
- `.upgrade-cta` - upgrade CTA button
- `.final-cta` - final CTA section
- `.final-benefits` - final benefits grid
- `.benefit-item` - benefit item
- `.benefit-icon` - benefit icons
- `.final-cta-button` - final CTA button
- `.final-guarantee` - final guarantee text

## Recommendation:
Create a game-model-specific SCSS partial that includes all these missing classes and import it into main.scss.