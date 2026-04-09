import streamlit as st

from ingestion.loader import load_text
from ingestion.chunker import create_chunks
from ingestion.pyramid import build_pyramid
from retrieval.search import search_pyramid

# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="AI Knowledge Engine",
    page_icon="🧠",
    layout="centered"
)

# -------- STYLING --------
st.markdown("""
    <style>
    body {
        background-color: #0f172a;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
    .answer-box {
        padding: 20px;
        border-radius: 12px;
        background: linear-gradient(135deg, #1e293b, #334155);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown(
    "<h1 style='text-align: center;'>🧠 AI Knowledge Engine</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Ask questions. Extract insights. Think smarter.</p>",
    unsafe_allow_html=True
)

st.info("💡 Try: 'What is AI?' or 'machines learning'")

st.divider()

# -------- LOAD & CACHE DATA (IMPORTANT FOR DEPLOYMENT) --------
@st.cache_data
def load_pipeline():
    text = load_text("sample.txt")
    chunks = create_chunks(text, chunk_size=50, overlap=10)
    pyramid = build_pyramid(chunks)
    return pyramid

pyramid = load_pipeline()

# -------- INPUT --------
query = st.text_input("💬 Ask your question:")

# -------- OUTPUT --------
if query:
    query = query.strip()

    with st.spinner("Thinking..."):
        result = search_pyramid(pyramid, query.lower())

    if result:
        st.markdown("<div class='answer-box'>", unsafe_allow_html=True)

        st.markdown("### ✨ Answer")
        st.write(result["summary"])

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**📂 Category**")
            st.write(result["category"])

        with col2:
            st.markdown("**🔑 Keywords**")
            st.write(", ".join(result["keywords"]))

        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.warning("No relevant answer found.")

# -------- FOOTER --------
st.divider()
st.markdown(
    "<p style='text-align: center; color: gray;'>Built as part of AI System Design Assignment</p>",
    unsafe_allow_html=True
)