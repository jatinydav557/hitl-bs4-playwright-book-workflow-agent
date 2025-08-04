import re
from typing import Dict

def calculate_text_quality_metrics(text: str) -> Dict[str, float]:
    """Calculate quality metrics for text"""
    if not text:
        return {"length": 0, "readability": 0, "diversity": 0, "coherence": 0}
    
    # Length score (normalized)
    length_score = min(len(text) / 2000.0, 1.0)
    
    # Readability score
    words = text.split()
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    readability_score = max(0, 1 - abs(avg_word_length - 5) / 5)
    
    # Diversity score
    unique_words = len(set(words))
    total_words = len(words)
    diversity_score = unique_words / total_words if total_words > 0 else 0
    
    # Coherence score
    sentences = re.split(r'[.!?]+', text)
    avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
    coherence_score = max(0, 1 - abs(avg_sentence_length - 15) / 15)
    
    return {
        "length": length_score,
        "readability": readability_score,
        "diversity": diversity_score,
        "coherence": coherence_score
    }

def reward_model(state):
    """Simple reward model based on quality metrics"""
    final_text = state.get("rewritten_text", "")
    
    if not final_text:
        return {**state, "reward_score": 0.0, "quality_metrics": {}}
    
    # Calculate quality metrics
    metrics = calculate_text_quality_metrics(final_text)
    
    # Simple average reward
    final_reward = sum(metrics.values()) / len(metrics)
    
    return {
        **state, 
        "reward_score": final_reward,
        "quality_metrics": metrics
    }

