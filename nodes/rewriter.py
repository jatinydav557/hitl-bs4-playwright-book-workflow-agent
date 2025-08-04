import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def rewrite_chapter(state):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return {**state, "rewritten_text": "GROQ_API_KEY not found. Please set your API key in a .env file."}
    
    try:
        llm = ChatGroq(
            api_key=api_key,
            model='llama-3.1-8b-instant'
        )
        
        chapter_text = state.get('chapter_text', '')
        if not chapter_text or chapter_text.startswith("No text") or chapter_text.startswith("Failed"):
            return {**state, "rewritten_text": "No valid chapter text to rewrite."}
        
        prompt = f"Rewrite the following book chapter in a more engaging, modern tone while preserving the core narrative and meaning:\n\n{chapter_text}"
        rewritten = llm.invoke(prompt)
        
        return {**state, "rewritten_text": rewritten.content}
    
    except Exception as e:
        return {**state, "rewritten_text": f"Error during rewriting: {str(e)}"}
