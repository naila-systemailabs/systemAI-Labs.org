import re
import subprocess

# Get original content
result = subprocess.run(['git', 'show', 'HEAD:enterprise-hr-ai-agent.html'], capture_output=True, text=True, encoding='utf-8')
old_html = result.stdout

style_pattern = re.compile(r'<style>(.*?)</style>', re.DOTALL)
match = style_pattern.search(old_html)

if match:
    old_css = match.group(1)
    
    # We want to extract specific blocks:
    # /* Technical Blueprint Backgrounds */ to the end
    # Or just write a regex to find all class selectors
    
    # Let's just find the block starting at /* Technical Blueprint Backgrounds */
    marker = "/* Technical Blueprint Backgrounds */"
    idx = old_css.find(marker)
    if idx != -1:
        extracted_classes = old_css[idx:]
        
        # Append to global.css
        with open('global.css', 'a', encoding='utf-8') as f:
            f.write('\n\n/* --- PRODUCT PAGE COMPONENTS --- */\n')
            f.write(extracted_classes)
        print("Appended product classes to global.css")
    else:
        print("Marker not found.")
