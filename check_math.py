import os
import re

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find code blocks and remove them to avoid false positives
    content_no_code = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    content_no_code = re.sub(r'`[^`\n]+`', '', content_no_code)

    issues = []
    
    # Check for single $
    single_dollars = re.findall(r'(?<!\$)\$[^\$]+?\$(?!\$)', content_no_code)
    if single_dollars:
        issues.append(f"Single $ found: {len(single_dollars)} occurrences")
        
    # Find all $$ ... $$
    math_blocks = re.findall(r'\$\$(.*?)\$\$', content_no_code, flags=re.DOTALL)
    for block in math_blocks:
        if '|' in block:
            issues.append("Found '|' in math block")
            break
            
    # Check for extra newlines in math blocks
    # e.g. $$ \n \n or \n \n $$
    if re.search(r'\$\$\s*\n\s*\n', content_no_code):
         issues.append("Extra newlines after $$")
    if re.search(r'\n\s*\n\s*\$\$', content_no_code):
         issues.append("Extra newlines before $$")
         
    # check for single extra newlines around short formulas
    # \$\$\n\s*[^\n]{1,50}\s*\n\$\$$
    if re.search(r'\$\$\n[^\n]{1,30}\n\$\$', content_no_code):
         issues.append("Short formula on multiple lines")

    if issues:
        print(f"{filepath}: {issues}")

dirs = [
    'contents/vi/chapter15/_posts',
    'contents/en/chapter15/_posts'
]

for d in dirs:
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.endswith('.md'):
                check_file(os.path.join(d, f))
