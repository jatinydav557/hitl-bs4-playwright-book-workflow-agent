import streamlit as st


def human_review(state):
    # Simple pass-through for now - no human intervention (less complexity)
    return {**state, "rewritten_text": state.get("rewritten_text", "")}