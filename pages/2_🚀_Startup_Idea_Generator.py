import streamlit as st

st.set_page_config(
    page_title="Startup Generator - NIC",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Start a Startup from Scratch")
st.caption("Powered by Groq Models | Designed for NIC Founders")
st.markdown("---")

# Safe API key check with fallback explanation
try:
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
except Exception:
    GROQ_API_KEY = None

if not GROQ_API_KEY:
    st.warning("⚠️ `GROQ_API_KEY` not found in Streamlit secrets. You can still test the UI layout below, but AI generation will require the key.")

# User Input Form
with st.form("startup_input_form"):
    st.subheader("1. Define Your Venture Baseline")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        industry_themes = st.multiselect(
            "Select Target Industry / Themes",
            options=["FinTech", "EdTech", "HealthTech", "AgriTech", "E-Commerce", "SaaS", "DeepTech / AI"],
            default=["FinTech"]
        )
        
        target_audience = st.selectbox(
            "Primary Target Audience / Market Type",
            options=["B2B (Business-to-Business)", "B2C (Business-to-Consumer)", "B2B2C", "Enterprise"]
        )

    with col_b:
        keywords_input = st.text_input(
            "Enter Key Concept Keywords (Comma Separated)",
            placeholder="e.g. AI automation, micro-loans, mobile app"
        )
        
        investment_stage = st.select_slider(
            "Target Initial Funding / Scope",
            options=["Bootstrap / Lean MVP", "Pre-Seed Incubator", "Seed Capital"]
        )

    problem_statement = st.text_area(
        "Describe the Problem Statement or Opportunity (Required)",
        placeholder="e.g. Small retail shop owners struggle to manage inventory across physical and online channels.",
        height=120
    )

    submit_button = st.form_submit_button(label="Generate Complete Startup Plan ⚡", use_container_width=True)

if submit_button:
    if not problem_statement.strip():
        st.warning("⚠️ Please provide a problem statement to generate a plan.")
    else:
        master_prompt = f"""
You are a senior startup incubator mentor at the National Incubation Center (NIC).
Transform the following user inputs into a comprehensive, professional startup execution plan.

- Industry / Themes: {', '.join(industry_themes)}
- Target Audience: {target_audience}
- Concept Keywords: {keywords_input}
- Funding Target / Scope: {investment_stage}
- Problem Statement: {problem_statement}

Generate a thorough, structured startup plan formatted in Markdown with:
1. Executive Summary & Brand Concept
2. Market Analysis & Target Persona
3. Product Architecture & MVP
4. Monetization & Financial Model
5. Go-To-Market Strategy
6. NIC Incubator Pitch Highlights
"""

        with st.spinner("Analyzing market parameters and generating your startup blueprint..."):
            try:
                from groq import Groq
                client = Groq(api_key=GROQ_API_KEY)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are an expert startup advisor and incubator director."},
                        {"role": "user", "content": master_prompt}
                    ],
                    model="openai/gpt-oss-120b",  # Updated to an active model on Groq
                    temperature=0.7,
                    max_tokens=2000
                )
                output_markdown = chat_completion.choices[0].message.content
                st.success("✅ Startup Plan Generated Successfully!")
                st.markdown("---")
                st.markdown(output_markdown)
                
                st.download_button(
                    label="📥 Download Plan (.md)",
                    data=output_markdown,
                    file_name="NIC_Startup_Plan.md",
                    mime="text/markdown"
                )
            except Exception as e:
                st.error(f"API Connection Error: {str(e)}")
                st.info("💡 Tip: Make sure your `GROQ_API_KEY` is correctly placed inside `.streamlit/secrets.toml`.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p style="color: #666; font-size: 14px;">Developed by Syed Hammad Atif | National Incubation Center (NIC)</p>
    </div>
    """,
    unsafe_allow_html=True
)