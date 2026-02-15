# Release Notes — Fantasy Software

## Version 1.4.0 - 2026-02-10

### 🚀 Major Features
- **Story Mode**: A guided onboarding flow with sample projects and checkpoints.
- **Magic Sync**: Offline-first sync with conflict resolution.
- **Plugin Marketplace**: Install community extensions directly from settings.

### 🔧 Improvements
1. Reduced cold start time by 35%.
2. Improved keyboard shortcuts discoverability.
3. Updated export pipeline to preserve headings and tables.

### 📝 Notes (EN / ไทย / 日本語)
- **EN**: Release notes are now grouped by category with better scanning.
- **ไทย**: เพิ่มความเร็วในการค้นหา และปรับปรุงประสบการณ์การพิมพ์ให้สวยขึ้น
- **日本語**: 印刷用レイアウトを改善しました（A4 と余白の調整）

### 📊 Compatibility Matrix

| Component | Minimum | Recommended | Notes |
|---|---:|---:|---|
| macOS | 12.0 | 14+ | Apple Silicon supported |
| Windows | 11 | 11 | ARM64 experimental |
| Linux | Ubuntu 22.04 | Ubuntu 24.04 | Wayland recommended |
| Node.js (optional) | 18 | 20 | For integrations |

### ⚠️ Breaking Changes
- Configuration key `sync.mode=legacy` has been removed. Use `sync.strategy=offline-first`.

---

## Version 1.3.2 - 2026-01-28

### 🐛 Bug Fixes
- Fixed an issue where PDFs could render blank pages when a document started with a table.
- Resolved a crash when importing markdown files containing mixed RTL/LTR punctuation.

### 📝 Notes
- **ไทย**: แก้ปัญหาแสดงผล PDF หน้าว่างในบางกรณี
- **日本語**: 一部の環境で発生していたクラッシュを修正しました

---

## Version 1.3.0 - 2026-01-10

### ✨ New Features
- **Release Diff View**: Compare two versions side-by-side.
- **Smart Changelog Sections**: Auto-detect `Features`, `Fixes`, `Breaking Changes` headings.

### 🔧 Improvements
- Improved markdown rendering for nested lists:
  - Better indentation
  - More consistent spacing
  - Cleaner page breaks when printing

### 📋 Migration Checklist
1. Back up your `fantasy.config.json`.
2. Re-open the app to trigger config upgrade.
3. Verify your export templates.

---

## Version 1.2.5 - 2025-12-20

### 🐛 Bug Fixes
- Fixed duplicate entries in the activity timeline.
- Corrected timezone offsets for scheduled exports.

### 🧪 Test Notes
- Verified on A4 and Letter.
- Tested mixed-language paragraphs: English + ไทย + 日本語.

---

## Version 1.2.0 - 2025-11-30

### ✨ New Features
- **Print Profiles**: Save and reuse print settings (A4, margins, header/footer).
- **Template Variables**: Use placeholders like `{repo_name}` and `{repo_url}` in exports.

### 📝 Example Template Variables
- `{repo_name}` → `Fantasy Software`
- `{repo_url}` → `https://github.com/example/fantasy-software`

---

## Version 1.1.1 - 2025-10-18

### 🐛 Bug Fixes
- Fixed a regression in `Export to PDF` where emojis could overlap line height.

### 📝 Notes
- **EN**: Emoji rendering is now normalized across platforms.
- **日本語**: 絵文字の行間問題を修正しました

---

## Version 1.1.0 - 2025-10-01

### ✨ New Features
- **Changelog Linter**: Detect missing headings and inconsistent version formats.
- **One-click PDF Export**: Export the current release notes to PDF.

### 🔧 Improvements
- Better GitHub-flavored markdown support:
  - Task lists
  - Tables
  - Strikethrough

### ✅ Task List Example
- [x] Render tables correctly
- [x] Support emoji in headings
- [ ] Add more sample datasets

---

## Version 1.0.3 - 2025-09-12

### 🐛 Bug Fixes
- Fixed a bug where long code blocks could push content outside page margins.

### 🔎 Security
- Updated dependencies to address a minor vulnerability in the HTTP client.

---

## Version 1.0.0 - 2025-09-01

### 🎉 Initial Release
Fantasy Software is an imaginary tool for generating and printing high-quality release notes.

### ✨ Highlights
- GitHub-style markdown release notes
- A4 print formatting
- Consistent headings and sectioning

### 📝 Multilingual Message
- **ไทย**: เปิดตัวเวอร์ชันแรก! ขอบคุณที่ทดลองใช้งาน 🙏
- **日本語**: 初回リリースです。ご利用ありがとうございます！
