import streamlit as st
from pymilvus import connections, Collection

from config import MILVUS_CONFIG

def search_chunks(query: str, top_k: int = 10) -> list:
    connections.connect(**MILVUS_CONFIG)
    results = []
    
    for collection_name in MILVUS_CONFIG["collections"]:
        try:
            collection = Collection(collection_name)
            collection.load()
            
            search_results = collection.search(
                data=[query],
                anns_field="bm25",
                param=MILVUS_CONFIG["search_params"],
                limit=top_k,
                output_fields=MILVUS_CONFIG["output_fields"]
            )
            
            for hit in search_results[0]:
                results.append({
                    "score": float(hit.score),
                    "title": hit.fields.get("title"),
                    "content": hit.fields.get("description"),
                    "source": collection_name
                })
                
        except Exception as e:
            st.error(f"Ошибка в коллекции {collection_name}: {str(e)}")
    
    return sorted(results, key=lambda x: x['score'], reverse=True)[:top_k]