def reward_model(state):
    final_text = state.get("rewritten_text", "")
    if final_text:
        # Simple reward based on text length and quality indicators
        reward_score = min(len(final_text) / 1000.0, 1.0)  # Normalize to 0-1
    else:
        reward_score = 0.0
    
    return {**state, "reward_score": reward_score, "final_text": final_text}

