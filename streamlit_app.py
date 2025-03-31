import streamlit as st
import openai
import os

# Set your OpenAI key (use env var in real deployment)
openai.api_key = os.getenv("OPENAI_API_KEY")

# UI
st.set_page_config(page_title="AI Client Diagnostic", layout="centered")
st.title("🔍 AI-Powered Client Diagnostic")
st.subheader("Smarter Conversations. Faster Conversions.")
st.markdown("Answer a few questions and get a tailored insight report instantly.")

with st.form("client_diagnostic"):
    role = st.selectbox("What’s your role?", ["CXO", "Business Lead", "IT Lead", "Product Owner", "Other"])
    challenge = st.selectbox("Key business challenge?", ["Operational Efficiency", "Scaling AI", "New Market Entry", "Customer Experience"])
    focus = st.selectbox("Your current focus area:", ["Strategy", "Operations", "Digital/Tech", "Transformation"])
    maturity = st.selectbox("How mature is your current solution?", ["Early exploration", "MVP/POC done", "Scaling in progress", "Mature but evolving"])
    timeline = st.selectbox("Timeline for intervention:", ["< 3 months", "3–6 months", "6–12 months", "> 12 months"])
    partner = st.radio("Worked with external partners before?", ["Yes", "No"])
    blocker = st.text_input("Biggest blocker today:")
    submitted = st.form_submit_button("Generate My Diagnostic")

if submitted:
    with st.spinner("Analyzing responses..."):
        prompt = f"""
        The client is a {role} focused on {focus} with a key challenge: {challenge}.
        Their current maturity level is: {maturity}, and their intervention timeline is: {timeline}.
        External partners used before: {partner}.
        Their biggest blocker is: {blocker}.

        Based on this, write a diagnostic report that includes:
        1. Maturity Stage
        2. Recommended Offerings
        3. Similar Case Studies
        4. Quick Wins
        5. Suggested Next Step

        Be clear, professional, and consultative in tone.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        result = response['choices'][0]['message']['content']
        st.success("Here’s your tailored diagnostic:")
        st.markdown(result)

