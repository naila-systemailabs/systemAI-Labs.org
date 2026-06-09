import re

# Read index.html for nav and footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract Nav
nav_match = re.search(r'<nav class="nav" id="nav">.*?</nav>', index_html, re.DOTALL)
master_nav = nav_match.group(0).replace('href="#services"', 'href="index.html#services"').replace('href="#work"', 'href="index.html#work"').replace('href="#manifesto"', 'href="index.html#manifesto"').replace('href="#" class="logo"', 'href="index.html" class="logo"')

# Extract Footer
footer_match = re.search(r'<footer>.*?</footer>', index_html, re.DOTALL)
master_footer = footer_match.group(0)

new_legal_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Legal | SystemAILabs</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
    
    <script src="https://unpkg.com/feather-icons"></script>
    <link rel="stylesheet" href="global.css">
    
    <style>
        .legal-section h1 {{ font-size: 2.5rem; margin-bottom: 24px; color: var(--text); border-bottom: 1px solid var(--border); padding-bottom: 16px; }}
        .legal-section h2 {{ font-size: 1.5rem; margin-top: 40px; margin-bottom: 16px; color: var(--text); }}
        .legal-section p, .legal-section li {{ color: var(--text-muted); font-size: 1.1rem; line-height: 1.8; }}
        .legal-section {{ margin-bottom: 60px; }}
    </style>
</head>
<body>

    {master_nav}

    <header class="hero" style="padding-top: 160px; padding-bottom: 60px;">
        <div class="container text-center">
            <h1>Legal & Compliance</h1>
            <p class="hero-lead text-center" style="margin: 0 auto;">Privacy Policy and Terms of Service for SystemAILabs.org</p>
        </div>
    </header>

    <section class="section" style="padding-top: 0;">
        <div class="container" style="max-width: 800px;">

            <div id="privacy" class="legal-section">
                <h1>Privacy Policy</h1>
                <p>Last Updated: March 2026</p>
                <h2>Data Processing</h2>
                <p>At SystemAI Labs, we prioritize your professional security. Our autonomous agents and integrations process data securely within your VPC or local device where applicable. We do not store or sell your credentials or private messages.</p>
                <h2>Waitlist Information</h2>
                <p>The only personal data we collect is the email address you voluntarily provide for our waitlist, which is stored securely for communication purposes.</p>
            </div>

            <div id="terms" class="legal-section">
                <h1>Terms of Service</h1>
                <h2>Beta Usage</h2>
                <p>Certain SystemAILabs tools are provided in a controlled beta phase. This software is provided "as-is" without warranties of any kind.</p>
                <h2>User Responsibility</h2>
                <p>Users are responsible for ensuring their use of these tools complies with respective third-party terms of service. SystemAI Labs is not liable for account restrictions resulting from automated behavior.</p>
            </div>

        </div>
    </section>

    {master_footer}

    <script>
        feather.replace();
    </script>
</body>
</html>
"""

with open('legal.html', 'w', encoding='utf-8') as f:
    f.write(new_legal_html)

print("Synchronized legal.html")
