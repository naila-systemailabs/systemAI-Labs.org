import re
import os
import glob

# 1. Read index.html for nav, hero_bg, and footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract Nav
nav_match = re.search(r'<nav class="nav" id="nav">.*?</nav>', index_html, re.DOTALL)
master_nav = nav_match.group(0).replace('href="#services"', 'href="index.html#services"').replace('href="#work"', 'href="index.html#work"').replace('href="#manifesto"', 'href="index.html#manifesto"').replace('href="#" class="logo"', 'href="index.html" class="logo"')

# Extract Hero BG
hero_bg_match = re.search(r'<div class="hero-bg">.*?</div>', index_html, re.DOTALL)
hero_bg = hero_bg_match.group(0)

# Extract Footer
footer_match = re.search(r'<footer>.*?</footer>', index_html, re.DOTALL)
master_footer = footer_match.group(0)

# Update Footer to point to support.html instead of mailto
updated_master_footer = master_footer.replace('href="mailto:support@systemailabs.org">Contact Support', 'href="support.html">Contact Support')

# 2. Build support.html
support_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Support & Help Center | SystemAILabs</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
    
    <script src="https://unpkg.com/feather-icons"></script>
    <link rel="stylesheet" href="global.css">
    
    <style>
        .faq-item {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
        }}
        .faq-item h3 {{
            font-size: 1.25rem;
            color: var(--text);
            margin-bottom: 12px;
        }}
        .faq-item p {{
            color: var(--text-muted);
            margin: 0;
            line-height: 1.6;
        }}
    </style>
</head>
<body>

    {master_nav}

    <header class="hero" style="padding-top: 160px; padding-bottom: 60px;">
        {hero_bg}
        <div class="container text-center">
            <div class="badge-dark reveal">Help Center</div>
            <h1 class="reveal" style="font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 24px;">Support</h1>
            <p class="hero-lead text-center reveal" style="margin: 0 auto;">We're here to help you deploy, scale, and debug your AI infrastructure.</p>
        </div>
    </header>

    <section class="section">
        <div class="container">
            <div class="contact-grid">
                
                <!-- FAQ and SLA -->
                <div class="contact-info reveal">
                    <h2 style="font-size: 2rem; margin-bottom: 24px;">Frequently Asked Questions</h2>
                    
                    <div class="faq-item">
                        <h3>What is your typical response time?</h3>
                        <p>Enterprise clients on an active SLA receive priority support with a guaranteed 4-hour response time. Standard beta users can expect a response within 24-48 business hours.</p>
                    </div>
                    
                    <div class="faq-item">
                        <h3>Do you offer live technical debugging?</h3>
                        <p>Yes. If an issue requires deep technical intervention (such as an LLM hallucination loop or vector DB indexing issue), we can schedule a secure Zoom or Google Meet session to pair program and debug.</p>
                    </div>

                    <div class="faq-item">
                        <h3>I forgot my API keys, how can I reset them?</h3>
                        <p>Please submit a ticket using the form on the right. For security purposes, we do not send API keys over email; we will provision a new key in your secure client portal.</p>
                    </div>

                    <div class="email-block" style="margin-top: 40px;">
                        <div class="bento-icon" style="margin:0;width:44px;height:44px;">
                            <i data-feather="life-buoy"></i>
                        </div>
                        <div>
                            <div style="font-size:0.85rem;color:var(--text-muted);">Direct email support</div>
                            <a href="mailto:support@systemailabs.org">support@systemailabs.org</a>
                        </div>
                    </div>
                </div>

                <!-- Support Ticket Form -->
                <div class="form-panel reveal">
                    <h3 style="font-size: 1.5rem; margin-bottom: 24px; color: var(--text);">Submit a Ticket</h3>
                    <form id="supportForm" action="https://formsubmit.co/support@systemailabs.org" method="POST">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="hidden" name="_subject" value="Support Ticket - SystemAILabs">
                        
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input type="text" id="name" name="name" placeholder="John Doe" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="email">Account Email</label>
                            <input type="email" id="email" name="email" placeholder="john@company.com" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="product">Product or Integration</label>
                            <select id="product" name="product" required style="width: 100%; padding: 16px; background: var(--bg); border: 1px solid var(--border); border-radius: 8px; color: var(--text); font-family: inherit;">
                                <option value="" disabled selected>Select an option...</option>
                                <option value="Enterprise HR AI Agent">Enterprise HR AI Agent</option>
                                <option value="Real Estate Chatbot">Real Estate Chatbot</option>
                                <option value="ContextMiner">ContextMiner</option>
                                <option value="SyllabusAI">SyllabusAI</option>
                                <option value="Custom Development">Custom Development</option>
                                <option value="Billing / Account">Billing / Account</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="message">Issue Description</label>
                            <textarea id="message" name="message" rows="5"
                                placeholder="Please describe the issue you are experiencing in detail. Include any error codes if applicable." required></textarea>
                        </div>
                        
                        <button type="submit" class="btn btn-primary w-100">
                            Submit Ticket
                        </button>
                    </form>
                </div>
                
            </div>
        </div>
    </section>

    {updated_master_footer}

    <script>
        feather.replace();
    </script>
</body>
</html>
"""

with open('support.html', 'w', encoding='utf-8') as f:
    f.write(support_html)
print("Created support.html")

# 3. Update all existing html files to use updated_master_footer and update their old footer links
html_files = glob.glob('*.html')
for html_file in html_files:
    if html_file == 'support.html':
        continue
        
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We can just do a string replace of the specific footer line for safety.
    content = content.replace('href="mailto:support@systemailabs.org">Contact Support', 'href="support.html">Contact Support')
    
    # Just in case some have the new updated_master_footer format, we just replace the link.
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated footer in {html_file}")
