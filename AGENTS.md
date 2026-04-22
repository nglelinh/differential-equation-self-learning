# AGENTS.md

## Project

Jekyll multilingual course: **Differential Equations and Advanced Applications** (EN/VI). Deploys to GitHub Pages via Actions.

## Course Structure

See `COURSE_STRUCTURE.md` for:
- 16 chapters: Foundations → ODEs → Systems → PDEs → Functional Analysis → ΨDOs
- Lesson ordering and reference book assignments per chapter
- File naming conventions
- Focus on vietnamese content

## Commands

```bash
bundle install           # Install Ruby dependencies
bundle exec jekyll serve # Local dev at http://127.0.0.1:4000/{baseurl}/
```

Docker alternative (uses Jekyll 4.2.0):
```bash
docker-compose up        # Port 4000
```

Restart Jekyll after editing `_config.yml`.

## Lecture Posts

Path: `contents/{lang}/chapterXX/_posts/YYYY-MM-DD-title.md`

Required front matter:
```yaml
---
layout: post
title: "Lesson Title"
chapter: '00'           # Two-digit string, must match directory
order: 1                # Integer - CRITICAL for language switching
owner: Author Name
lang: en                # 'en' or 'vi'
categories:
- chapter00             # Must match directory name exactly
lesson_type: required   # 'required' or 'optional'
---
```

**Language pairing**: EN/VI posts must have identical `chapter` + `order` values. The `{% language_switch %}` tag uses these to link translations.

## Adding a Chapter

1. Create both `contents/en/chapterXX/_posts/` and `contents/vi/chapterXX/_posts/`
2. Ensure all posts have matching `chapter`, `order`, and `categories` values across languages

## Math (MathJax)

Always use `$$...$$` for both inline and display math. Never use single `$`.

```markdown
Inline: $$\frac{dy}{dt} = ky$$

Display:
$$
\frac{\partial u}{\partial t} = \alpha^2 \frac{\partial^2 u}{\partial x^2}
$$
```

## Images

```markdown
![Alt]({{ site.imgurl }}/chapter_img/image.png)
```

## Key Files

- `_config.yml` - Site config, translations (`t.en.*`/`t.vi.*`), URLs
- `_plugins/multilang.rb` - `{% t key %}` for translations, `{% language_switch %}` tag
- `home/_posts/` - Home page content

## Deployment

Push to `main` triggers `.github/workflows/jekyll.yml`. Requires Pages source set to "GitHub Actions".

## Writing Guidelines

See `.cursor/rules/`:
- `lecture-notes-rule.mdc` - Prose style, 1500-3000 words/lecture, favor paragraphs over bullets
- `math-formula-rule.mdc` - LaTeX conventions, use `$$` not `$`
