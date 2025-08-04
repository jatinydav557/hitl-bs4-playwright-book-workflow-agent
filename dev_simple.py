#!/usr/bin/env python3
"""
LangSmith tracking
Works with Python 3.10 
"""

import os
import asyncio
import sys
from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional

from nodes.scraper import scrape_chapter
from nodes.rewriter import rewrite_chapter
from nodes.rl import reward_model
from nodes.screenshot import take_screenshot

# Fix for Windows asyncio + Playwright subprocess issues
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

# Set up LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "chapter-rewriter"

# Define state schema
class WorkflowState(TypedDict, total=False):
    url: str
    chapter_text: Optional[str]
    screenshot_path: Optional[str]
    rewritten_text: Optional[str]
    reward_score: Optional[float]

# Build the graph with LangSmith tracking
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

# Create the app
app = build_graph()

def test_workflow(url: str = None):
    """Test the workflow with a sample URL"""
    if not url:
        url = "https://en.wikisource.org/wiki/Pride_and_Prejudice/Chapter_2"
    
    print(f"🚀 Testing workflow with URL: {url}")
    print("=" * 50)
    
    try:
        result = app.invoke({"url": url})
        
        print("✅ Workflow completed successfully!")
        print(f"📝 Rewritten text length: {len(result.get('rewritten_text', ''))}")
        print(f"📈 Reward score: {result.get('reward_score', 'N/A')}")
        
        # Show quality metrics
        metrics = result.get('quality_metrics', {})
        if metrics:
            print("\n📊 Quality Metrics:")
            for key, value in metrics.items():
                print(f"   {key.title()}: {value:.3f}")
        
        return result
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Chapter Rewriter Development Server")
    parser.add_argument("--url", type=str, help="URL to process")
    args = parser.parse_args()
    
    result = test_workflow(args.url)
    
    if result:
        print("\n🎉 Check your LangSmith dashboard for detailed traces!")
        print("   Visit: https://smith.langchain.com/") 