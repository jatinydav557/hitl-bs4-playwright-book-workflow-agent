from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional, Dict, Any

from nodes.scraper import scrape_chapter
from nodes.rewriter import rewrite_chapter
from nodes.hitl import human_review
from nodes.rl import reward_model
from nodes.screenshot import take_screenshot
from chroma.vector_store import save_version


# 1. Define your state schema
class WorkflowState(TypedDict, total=False):
    url: str
    chapter_text: Optional[str]
    screenshot_path: Optional[str]
    rewritten_text: Optional[str]
    human_feedback: Optional[str]
    reward_score: Optional[float]
    version_id: Optional[str]
    review_status: Optional[str]
    review_metadata: Optional[Dict[str, Any]]
    enable_hitl: Optional[bool]


# 2. Build the graph
def build_graph(enable_hitl: bool = True):
    workflow = StateGraph(WorkflowState)

    workflow.add_node("scrape", scrape_chapter)
    workflow.add_node("screenshot", take_screenshot)
    workflow.add_node("rewrite", rewrite_chapter)
    workflow.add_node("review", human_review)
    workflow.add_node("reward", reward_model)
    workflow.add_node("store", save_version)

    workflow.set_entry_point("scrape")
    workflow.add_edge("scrape", "screenshot")
    workflow.add_edge("screenshot", "rewrite")
    
    # Conditional edge based on HITL setting
    if enable_hitl:
        workflow.add_edge("rewrite", "review")
        workflow.add_edge("review", "reward")
    else:
        workflow.add_edge("rewrite", "reward")
    
    workflow.add_edge("reward", "store")
    workflow.add_edge("store", END)

    return workflow.compile()
