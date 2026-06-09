import re
import os

# 1. Extract CSS from index.html and update it
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

style_pattern = re.compile(r'<style>(.*?)</style>', re.DOTALL)
match = style_pattern.search(html)

if match:
    css_content = match.group(1)
    # Write to global.css
    with open('global.css', 'w', encoding='utf-8') as f:
        f.write(css_content.strip() + '\n')
    
    # Replace style block in index.html
    new_html = html[:match.start()] + '<link rel="stylesheet" href="global.css">' + html[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('Extracted global.css and updated index.html')
else:
    print('Style block not found in index.html')

# 2. Update other HTML files
target_files = [
    'enterprise-hr-ai-agent.html',
    'real-estate-chatbot.html',
    'SyllabusAI.html',
    'context-miner.html'
]

font_target = r'<link href="https://fonts.googleapis.com/css2\?family=Inter:wght@300;400;500;600;700;800&family=JetBrains\+Mono:wght@400;700&display=swap" rel="stylesheet">'
font_replacement = r'''<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">'''

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace inline styles
        content = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="global.css">', content, flags=re.DOTALL)
        
        # Replace fonts
        content = re.sub(font_target, font_replacement, content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {filename}')
    else:
        print(f'File {filename} not found.')
