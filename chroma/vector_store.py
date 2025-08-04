import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("chapter_versions")

def save_version(state):
    collection.add(
        documents=[state.get("rewritten_text", "")],
        ids=[state['url']],
        metadatas=[{"reward": state.get("reward_score", 0)}]
    )
    return state
