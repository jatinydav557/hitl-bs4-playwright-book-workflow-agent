import asyncio
import sys
import streamlit as st
from graph_builder import build_graph
import os

# Fix for Windows asyncio + Playwright subprocess issues
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

st.set_page_config(page_title="Chapter Rewriter", layout="wide")
st.title("📚 Chapter Rewriter")

# Initialize session state
if "workflow_state" not in st.session_state:
    st.session_state.workflow_state = None

url = st.text_input(
    "Enter Chapter URL",
    "https://en.wikisource.org/wiki/Pride_and_Prejudice/Chapter_1"
)

run = st.button("Start Processing")

if run:
    with st.spinner("Processing..."):
        try:
            graph = build_graph()
            response = graph.invoke({"url": url})
            st.session_state.workflow_state = response
            st.success("✅ Processing complete!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.info("💡 Make sure you have set up your GROQ_API_KEY environment variable.")

# Display results
if st.session_state.workflow_state:
    response = st.session_state.workflow_state
    
    st.subheader("📝 Rewritten Chapter")
    rewritten_text = response.get('rewritten_text', 'No rewritten text returned.')
    if rewritten_text:
        st.write(rewritten_text)
    else:
        st.warning("⚠️ No rewritten text was generated.")

    # Quality Metrics
    quality_metrics = response.get('quality_metrics', {})
    if quality_metrics:
        st.subheader("📊 Quality Metrics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Length", f"{quality_metrics.get('length', 0):.2f}")
        with col2:
            st.metric("Readability", f"{quality_metrics.get('readability', 0):.2f}")
        with col3:
            st.metric("Diversity", f"{quality_metrics.get('diversity', 0):.2f}")
        with col4:
            st.metric("Coherence", f"{quality_metrics.get('coherence', 0):.2f}")

    st.subheader("📈 Reward Score")
    reward_score = response.get('reward_score', 'N/A')
    st.metric("Reward Score", f"{reward_score:.3f}" if isinstance(reward_score, (int, float)) else reward_score)

    st.subheader("📸 Screenshot")
    screenshot_path = response.get('screenshot_path', '')
    if screenshot_path and os.path.exists(screenshot_path):
        st.image(screenshot_path)
    else:
        st.write("No screenshot available.")
