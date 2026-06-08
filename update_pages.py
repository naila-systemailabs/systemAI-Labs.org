import os

def update_page(filename, data):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    replacements = {
        # SEO Meta
        'content="LinkedIn Context Miner - AI-Powered Context Extraction Chrome Extension engineered by Naila Shaikh at SystemAILabs.org. Extract, analyze, and leverage B2B data instantly."': f'content="{data["desc_short"]}"',
        'content="LinkedIn Context Miner, Chrome Extension, SystemAILabs.org, Naila Shaikh, AI Engineer, Lead Generation, LLM Chrome Extension"': f'content="{data["keywords"]}"',
        'href="https://systemailabs.org/context-miner.html"': f'href="https://systemailabs.org/{filename}"',
        'content="https://systemailabs.org/context-miner.html"': f'content="https://systemailabs.org/{filename}"',
        'content="LinkedIn Context Miner | AI Extension by Naila Shaikh"': f'content="{data["title_meta"]}"',
        'content="An enterprise-grade Chrome Extension for instant B2B context extraction and analysis powered by LLMs."': f'content="{data["desc_meta"]}"',
        
        # JSON-LD
        '"name": "LinkedIn Context Miner",': f'"name": "{data["title"]}",',
        '"description": "An AI-powered Chrome extension that extracts and analyzes professional contexts directly from LinkedIn profiles, streamlining B2B outreach and research.",': f'"description": "{data["desc_short"]}",',
        '<title>LinkedIn Context Miner | SystemAILabs</title>': f'<title>{data["title"]} | SystemAILabs</title>',
        
        # Hero
        'LinkedIn Context Miner</h1>': f'{data["title"]}</h1>',
        'Extract AI-powered personality insights and career gold in one click. Stop wasting hours on manual research.': data["subtitle"],
        
        # Technical Doc
        '<strong>The Problem:</strong> Managing a large network on LinkedIn is a manual, time-consuming process. Sales professionals and recruiters spend hours scrolling through activity feeds to find the perfect icebreaker.': f'<strong>The Problem:</strong> {data["problem"]}',
        '<strong>The Solution:</strong> A lightweight, high-performance Chrome Extension that injects a bespoke UI directly into the DOM. It automatically parses experience, badges, and recent activity as the user navigates, generating AI-powered conversation hooks instantly.': f'<strong>The Solution:</strong> {data["solution"]}',
        
        # Payload
        '"architecture"</span>: <span style="color: #fbbf24;">"Manifest V3 Autonomous Agent"</span>': f'"architecture"</span>: <span style="color: #fbbf24;">"{data["payload"]["arch"]}"</span>',
        '"DOM_parsing"</span>: <span style="color: #fbbf24;">"MutationObserver + Vanilla ES6"</span>': f'"{data["payload"]["k2"]}"</span>: <span style="color: #fbbf24;">"{data["payload"]["v2"]}"</span>',
        '"isolation"</span>: <span style="color: #fbbf24;">"Shadow DOM Encapsulation"</span>': f'"{data["payload"]["k3"]}"</span>: <span style="color: #fbbf24;">"{data["payload"]["v3"]}"</span>',
        '"orchestration"</span>: <span style="color: #fbbf24;">"Serverless Apps Script Pipeline"</span>': f'"{data["payload"]["k4"]}"</span>: <span style="color: #fbbf24;">"{data["payload"]["v4"]}"</span>',
        
        # Video iframe
        'src="https://www.youtube.com/embed/_NSyXEdu2hk?rel=0"': f'src="{data["video_url"]}"',
        'title="LinkedIn Context Miner Demo"': f'title="{data["title"]} Demo"',
        
        # Waitlist / Formsubmit Subject
        'value="New Project Inquiry - Context Miner Page"': f'value="New Project Inquiry - {data["title"]} Page"'
    }

    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"Warning: Could not find '{old[:30]}...' in {filename}")

    # For SyllabusAI we might need to swap the iframe with the code block, but for now we just write the content.
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


hr_data = {
    "title": "Enterprise HR AI Agent",
    "title_meta": "Enterprise HR AI Agent | SystemAILabs",
    "desc_short": "A production-grade autonomous agent designed to streamline human resource workflows, capable of reasoning through complex employee queries.",
    "desc_meta": "Secure LLM deployments for automated candidate screening and internal knowledge base RAG integration.",
    "keywords": "Enterprise HR AI Agent, AI Automation, SystemAILabs.org, Naila Shaikh, RAG, LLM Deployment, Candidate Screening",
    "subtitle": "Streamline human resource workflows with secure, private LLM deployments and automated candidate screening.",
    "problem": "Traditional HR departments spend thousands of hours manually screening resumes and answering repetitive employee policy questions.",
    "solution": "A robust, scalable autonomous agent deployed securely within your VPC. Utilizing Retrieval-Augmented Generation (RAG), it instantly answers policy questions and screens candidates with zero hallucinations.",
    "payload": {
        "arch": "Private VPC LLM Deployment",
        "k2": "framework", "v2": "LangChain + LlamaIndex",
        "k3": "vector_store", "v3": "Pinecone / Milvus",
        "k4": "security", "v4": "Zero-trust SOC2 compliant"
    },
    "video_url": "https://www.youtube.com/embed/9LMq3V6YwIs?rel=0"
}

re_data = {
    "title": "Real Estate AI Chatbot",
    "title_meta": "Real Estate AI Chatbot | SystemAILabs",
    "desc_short": "A custom lead-generation chatbot trained specifically on proprietary real estate data to handle client inquiries 24/7.",
    "desc_meta": "Instant lead capture and accurate property matching via an autonomous AI Chatbot built for real estate agencies.",
    "keywords": "Real Estate AI Chatbot, Lead Generation, SystemAILabs.org, Naila Shaikh, Chatbot, Tidio, Real Estate Automation",
    "subtitle": "Capture leads instantly 24/7. An intelligent agent trained exclusively on your agency's property data.",
    "problem": "Real estate agents lose leads outside of business hours because potential buyers demand instant answers to complex property questions.",
    "solution": "An intelligent, always-on chatbot embedded directly into your website. Trained on your specific MLS data and PDFs, it acts as a virtual agent that schedules viewings and qualifies buyers.",
    "payload": {
        "arch": "RAG-Powered Lead Capture",
        "k2": "integration", "v2": "Tidio + OpenAI API",
        "k3": "data_source", "v3": "MLS API + Custom PDFs",
        "k4": "conversion", "v4": "Automated CRM routing"
    },
    "video_url": "https://www.youtube.com/embed/-fZu_noaBlM?rel=0"
}

syl_data = {
    "title": "SyllabusAI",
    "title_meta": "SyllabusAI | SystemAILabs",
    "desc_short": "An intelligent educational tool that instantly parses complex course syllabi into actionable study plans and timelines.",
    "desc_meta": "AI-powered parsing of educational documents to create automated learning roadmaps.",
    "keywords": "SyllabusAI, Education Tech, SystemAILabs.org, Naila Shaikh, PDF Parsing, AI Study Planner",
    "subtitle": "Transform static syllabus PDFs into dynamic, actionable study timelines in seconds.",
    "problem": "Students struggle to manually extract dates, assignments, and grading rubrics from complex, unstructured 15-page syllabus PDFs.",
    "solution": "A highly-optimized pipeline that extracts text from PDFs and leverages LLMs to semantically parse academic requirements, generating calendar events and structured task lists instantly.",
    "payload": {
        "arch": "Document Intelligence Pipeline",
        "k2": "parsing", "v2": "OCR + Semantic Extraction",
        "k3": "model", "v3": "GPT-4o Document Vision",
        "k4": "output", "v4": "Structured JSON + iCal"
    },
    "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ?rel=0" # placeholder, will replace with terminal visual
}

update_page('enterprise-hr-ai-agent.html', hr_data)
update_page('real-estate-chatbot.html', re_data)
update_page('SyllabusAI.html', syl_data)

print("Pages updated.")
