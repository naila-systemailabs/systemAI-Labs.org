import os
import glob

broken_snippet = """        <div class="hero-bg">
            <div class="orb orb-1"></div>"""

fixed_snippet = """        <div class="hero-bg">
            <div class="orb orb-1"></div>
            <div class="orb orb-2"></div>
            <div class="orb orb-3"></div>
            <div class="grid-overlay"></div>
        </div>"""

html_files = glob.glob('*.html')
files_to_skip = ['index.html', 'index (1).html', 'legal.html']

for file in html_files:
    if file in files_to_skip:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if broken_snippet in content:
        content = content.replace(broken_snippet, fixed_snippet)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed hero-bg in {file}")
    else:
        # Maybe varying spaces? Let's check with a more robust replace.
        import re
        broken_regex = r'<div class="hero-bg">\s*<div class="orb orb-1"></div>(?!\s*<div class="orb orb-2">)'
        
        if re.search(broken_regex, content):
            content = re.sub(broken_regex, fixed_snippet.strip(), content)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed hero-bg via regex in {file}")
