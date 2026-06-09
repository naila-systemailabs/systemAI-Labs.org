import os

target_files = [
    'enterprise-hr-ai-agent.html',
    'real-estate-chatbot.html',
    'SyllabusAI.html',
    'context-miner.html'
]

for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace outdated classes
        content = content.replace('btn-outline', 'btn-ghost')
        content = content.replace('btn-outline-light', 'btn-ghost')
        
        # Ensure all links pointing to global.css are closed correctly
        # Just in case
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Refactored classes in {filename}')
