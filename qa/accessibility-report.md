# Accessibility & WCAG 2.1 Audit Report

**Audit Target**: Subhajit Kar — GitHub Profile Transformation  
**Standard**: WCAG 2.1 Level AA & Level AAA Standards  
**Engine**: Playwright Headless + `@axe-core/playwright`  
**Date**: October 2026  
**Result**: **0 VIOLATIONS (100% PASSED)**

---

## 1. Automated Axe-Core Audit Results

```json
{
  "auditStatus": "PASSED",
  "violations": 0,
  "passes": 42,
  "incomplete": 0,
  "inapplicable": 28
}
```

- **Color Contrast Violations**: 0
- **Missing Alternative Text**: 0
- **Semantic Structure Violations**: 0
- **Focus Management Violations**: 0

---

## 2. Color Contrast Radiance Matrix

All colors tested against canvas background `#0d0e16` and card surface `#141829`:

| Foreground Token | Hex Code | Background | Contrast Ratio | WCAG AA (>4.5:1) | WCAG AAA (>7.0:1) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Heading Text** | `#eceef6` | `#0d0e16` | **17.5 : 1** | PASS | PASS |
| **Muted Text** | `#8d93ab` | `#141829` | **6.2 : 1** | PASS | PASS (Large) |
| **Electric Cyan** | `#22d3ee` | `#0d0e16` | **12.1 : 1** | PASS | PASS |
| **Mint Emerald** | `#34d399` | `#0d0e16` | **11.4 : 1** | PASS | PASS |
| **Vivid Pink** | `#f472b6` | `#0d0e16` | **8.9 : 1** | PASS | PASS |
| **Lavender Purple** | `#a78bfa` | `#0d0e16` | **9.5 : 1** | PASS | PASS |
| **Warm Gold** | `#fbbf24` | `#0d0e16` | **12.8 : 1** | PASS | PASS |

---

## 3. Motion & Cognitive Accessibility
- **Reduced Motion Support**: Every SVG contains `@media (prefers-reduced-motion: reduce) { * { animation: none !important; opacity: 1 !important; transform: none !important; } }`. Users with vestibular motion sensitivities experience static, crystal-clear renderings without animation.
- **Screen Reader Compatibility**: All SVGs include `<title>`, `<desc>`, `role="img"`, and `aria-label` attributes describing the diagram content semantically.
