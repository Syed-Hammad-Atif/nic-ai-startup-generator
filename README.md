National Incubation Center (NIC) - AI Startup Generator

An AI-powered application built for founders, builders, and mentors at the National Incubation Center. Designed to take rough ideas and turn them into clear, structured, investment-ready startup execution plans using Streamlit and Groq.

---

Live Demo
Check out the live app here: [https://nic-ai-startup-generator-tvy3uzkm6wnusue7apryan.streamlit.app/](https://nic-ai-startup-generator-tvy3uzkm6wnusue7apryan.streamlit.app/))

---

What It Does

* Landing Page (1_🏠_Landing_Page.py): A quick intro to the platform, system architecture, and guidelines for founders getting started.
* Startup Idea Generator (2_🚀_Startup_Idea_Generator.py): An interactive tool where users feed in their target industry, problem statement, keywords, target market, and funding stage. The underlying LLM processes these inputs and outputs a complete, actionable startup blueprint.
* Instant Export: Download your generated execution plan straight to Markdown with one click.

---

Built With

* Framework: Streamlit (Multi-page app setup)
* AI Backend: Groq API
* Secrets Management: Streamlit Secrets (secrets.toml)

---

Running It Locally

If you want to clone this repo and run it on your machine, here is how to get set up:

1. Clone the repo:
git clone [https://github.com/Syed-Hammad-Atif/nic-ai-startup-generator.git](https://github.com/Syed-Hammad-Atif/nic-ai-startup-generator.git)
cd nic-ai-startup-generator
2. Set up a virtual environment:

# Windows

python -m venv .venv
.venv\Scripts\activate

---

Folder Structure

nic-ai-startup-generator/
├── .streamlit/
│   └── secrets.toml              # API key configuration (git-ignored)
├── pages/
│   └── 2_🚀*Startup_Idea_Generator.py  # AI generation page
├── 1*🏠_Landing_Page.py          # Main entry point
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation

---

Built By
Syed Hammad Atif
National Incubation Center (NIC)
