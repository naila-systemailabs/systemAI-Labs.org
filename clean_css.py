import re

with open('global.css', 'r', encoding='utf-8') as f:
    content = f.read()

parts = content.split('/* --- PRODUCT PAGE COMPONENTS --- */')
if len(parts) == 2:
    master_css = parts[0]
    product_css = parts[1]
    
    # We want to keep only specific classes from product_css
    # We can just write them directly
    clean_product_css = """
/* Technical Blueprint Backgrounds */
.blueprint-bg {
    background-color: var(--bg-elevated);
    background-image: 
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    background-position: center center;
    color: var(--text);
}
.blueprint-bg-dark {
    background-color: var(--bg);
    background-image: 
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    background-position: center center;
    color: white;
}

/* Layout */
.grid-3 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 32px;
}
.grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
}
@media (max-width: 768px) {
    .grid-2 { grid-template-columns: 1fr; }
}
.align-center { align-items: center; }
.gap-60 { gap: 60px; }
.text-center { text-align: center; }

/* Badges & Cards */
.badge-dark {
    display: inline-block;
    padding: 6px 16px;
    background: rgba(255,255,255,0.1);
    color: white;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 24px;
}

/* Features & Icons */
.icon-accent {
    color: var(--accent);
    width: 32px;
    height: 32px;
    margin-bottom: 20px;
}
.icon-box {
    width: 48px; height: 48px;
    border-radius: 12px;
    background: rgba(167, 139, 250, 0.1);
    color: var(--accent);
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Forms */
.form-card {
    background: var(--bg-elevated);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    border: 1px solid var(--border);
}
.form-group {
    margin-bottom: 24px;
}
.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    font-size: 0.95rem;
}
.form-group input, .form-group textarea {
    width: 100%;
    padding: 14px 16px;
    border: 1px solid var(--border);
    background: var(--bg);
    color: var(--text);
    border-radius: 8px;
    font-family: inherit;
    font-size: 1rem;
    transition: border-color 0.2s;
}
.form-group input:focus, .form-group textarea:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}
"""
    
    with open('global.css', 'w', encoding='utf-8') as f:
        f.write(master_css)
        f.write('\n/* --- PRODUCT PAGE COMPONENTS --- */\n')
        f.write(clean_product_css)
    print("Cleaned global.css")
else:
    print("Marker not found.")
