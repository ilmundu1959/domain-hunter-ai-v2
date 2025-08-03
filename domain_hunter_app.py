import streamlit as st

st.set_page_config(page_title="Domain Hunter AI", layout="centered", page_icon="🌐")

st.markdown("""
<style>
body {
    background-color: #1e1e2f;
    color: #ffffff;
}
div.stButton > button {
    background-color: #00bfa6;
    color: white;
    border-radius: 10px;
    padding: 0.6em 1em;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🌐 Domain Hunter AI")
st.subheader("Find valuable, low-cost domains you can flip for profit")

niche = st.text_input("💡 What niche or name style do you want?", placeholder="e.g. 4-letter tech, pet brands, luxury")

min_price = st.number_input("🔽 Minimum price (€)", min_value=0.0, value=1.0, step=0.5)
max_price = st.number_input("🔼 Maximum price (€)", min_value=1.0, value=10.0, step=0.5)

four_letter = st.toggle("🔤 Only show 4-letter names?")
check_trademark = st.toggle("🛡️ Check for trademarks (Malta & International)")
show_valuation = st.toggle("📈 Show resale estimate")

if st.button("🚀 Find Domains"):
    st.info("Searching marketplaces and AI suggestions...")

    # Placeholder sample output
    st.markdown("### 🔎 Suggestions:")
    results = [
        {"domain": "zexa.com", "price": 7.99, "valuation": 320, "risk": "Low"},
        {"domain": "vupi.io", "price": 3.49, "valuation": 150, "risk": "Safe"},
        {"domain": "golt.net", "price": 4.99, "valuation": 200, "risk": "Check Malta TM"},
    ]

    for res in results:
        st.markdown(f"""
        **🌍 {res['domain']}**  
        💶 Price: €{res['price']}  
        📈 Estimated Resale: €{res['valuation']}  
        🛡️ Risk Level: {res['risk']}  
        ---
        """)

    st.success("✅ Search complete — more features coming soon!")
