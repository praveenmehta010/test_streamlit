import streamlit as st

# Title
st.title("🔐 Secrets Viewer (Dev/Test Only)")

# Warning
st.warning("⚠️ Do NOT use this page in production! This is for debugging purposes only.")

# Secret keys to show
secrets = {
    "SERPAPI_API_KEY": st.secrets["API"],
}

# Display the secrets
for key, value in secrets.items():
    if value:
        with st.expander(f"{key}"):
            st.code(value, language="bash")
    else:
        st.error(f"{key} not found.")
