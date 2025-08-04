from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional

from nodes.scraper import scrape_chapter
from nodes.rewriter import rewrite_chapter
from nodes.rl import reward_model
from nodes.screenshot import take_screenshot


# 1. Define your state schema
class WorkflowState(TypedDict, total=False):
    url: str
    chapter_text: Optional[str]
    screenshot_path: Optional[str]
    rewritten_text: Optional[str]
    reward_score: Optional[float]


# 2. Build the graph
def build_graph():
    workflow = StateGraph(WorkflowState)

    workflow.add_node("scrape", scrape_chapter)
    workflow.add_node("screenshot", take_screenshot)
    workflow.add_node("rewrite", rewrite_chapter)
    workflow.add_node("reward", reward_model)

    workflow.set_entry_point("scrape")
    workflow.add_edge("scrape", "screenshot")
    workflow.add_edge("screenshot", "rewrite")
    workflow.add_edge("rewrite", "reward")
    workflow.add_edge("reward", END)

    return workflow.compile()
