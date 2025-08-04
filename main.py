import asyncio
import sys
import streamlit as st
from graph_builder import build_graph
import os

# Fix for Windows asyncio + Playwright subprocess issues
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

st.set_page_config(page_title="Softnerve Project", layout="centered")
st.title("📚 Automated Chapter Rewriter")

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
            
            st.success("✅ Done!")

            st.subheader("📝 Rewritten Chapter")
            rewritten_text = response.get('rewritten_text', 'No rewritten text returned.')
            if rewritten_text:
                st.write(rewritten_text)
            else:
                st.warning("⚠️ No rewritten text was generated.")

            st.subheader("📈 Reward Score")
            reward_score = response.get('reward_score', 'N/A')
            st.write(reward_score)

            st.subheader("📸 Screenshot")
            screenshot_path = response.get('screenshot_path', '')
            if screenshot_path and os.path.exists(screenshot_path):
                st.image(screenshot_path)
            else:
                st.write("No screenshot available.")

        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.info("💡 Make sure you have set up your GROQ_API_KEY environment variable.")
