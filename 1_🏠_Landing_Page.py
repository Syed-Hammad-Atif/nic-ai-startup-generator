import streamlit as st

st.set_page_config(
    page_title="NIC - AI Startup Generator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💡 National Incubation Center (NIC)")
st.subheader("AI-Powered Startup Generator Platform")
st.markdown("---")

st.markdown("""
### Welcome to the NIC Startup Builder!
Transforming raw ideas, problem statements, and market gaps into structured, investment-ready startup execution plans.

#### How It Works:
1. **Navigate** to the **Startup Idea Generator** page via the left sidebar.
2. **Define Your Concept**: Select industry themes, target audience, and describe your core problem statement.
3. **Generate Plan**: Our tailored LLM engine will build a comprehensive pitch deck blueprint, operational model, revenue strategy, and MVP scope.
""")

st.info("👈 Select **Startup Idea Generator** from the left sidebar to start building your venture!")

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p style="color: #666; font-size: 14px;">Developed by Syed Hammad Atif | National Incubation Center (NIC)</p>
    </div>
    """,
    unsafe_allow_html=True
)