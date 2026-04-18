# AGENTS.md

## Project

Jekyll multilingual course template. Deploys to GitHub Pages via Actions.

## Commands

```bash
bundle install           # Install Ruby dependencies
bundle exec jekyll serve # Local dev server at http://127.0.0.1:4000/{baseurl}/
```

Docker alternative:
```bash
docker-compose up        # Runs on port 4000
```

## Content Structure

### Lecture posts

All lectures go in `contents/{lang}/chapterXX/_posts/` with filename `YYYY-MM-DD-title.md`.

Required front matter:
```yaml
---
layout: post
title: "Lesson Title"
chapter: 'XX'           # Two-digit chapter number as string
order: N                # Integer ordering within chapter
owner: Author Name
lang: en                # 'en' or 'vi'
categories:
- chapterXX             # Must match chapter directory name
lesson_type: required   # 'required' or 'optional'
---
```

### Adding a new chapter

1. Create `contents/en/chapterXX/_posts/` and `contents/vi/chapterXX/_posts/`
2. Add posts with matching `chapter`, `order`, and `categories` values
3. Language switching relies on matching `chapter` + `order` across `en`/`vi`

### Home page

Edit posts in `home/_posts/`:
- `21-01-20-introduction.md` - Course intro
- `21-01-20-contents.md` - Course outline
- `21-02-03-makers.md` - Instructor info

## Math and LaTeX

Use `$$...$$` for both inline and display math. MathJax renders formulas.

```markdown
Inline: $$f(x) = x^2$$

Display block:
$$
\nabla f(x) = 0
$$
```

## Custom plugins

Located in `_plugins/`:
- `multilang.rb` - `{% t key %}` for translations, `{% language_switch %}` for lang toggle
- `redirect_generator.rb` - Handles redirects

## Configuration

Edit `_config.yml`:
- `baseurl` / `url` / `imgurl` - Required for proper asset paths
- `t.en.*` / `t.vi.*` - Translation strings
- `author` - Course author info

After changing `_config.yml`, restart Jekyll.

## Images

Place in `img/chapter_img/`, reference with:
```markdown
![Alt]({{ site.imgurl }}/chapter_img/image.png)
```

## Deployment

Push to `main` branch. GitHub Actions workflow (`.github/workflows/jekyll.yml`) builds and deploys to Pages.

Settings > Pages must be set to "GitHub Actions" source.

## Existing cursor rules

See `.cursor/rules/` for lecture writing guidelines:
- `lecture-notes-rule.mdc` - Detailed lecture structure, prose style, 1500-3000 words/lecture
- `math-formula-rule.mdc` - LaTeX formula conventions, use `$$` not `$`
