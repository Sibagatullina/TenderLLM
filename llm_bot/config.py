BASE_URL = "your_llm_url"

LLM_NAME = "your_llm_name"

MILVUS_CONFIG = {
    "host": "your_host",
    "port": 27370,
    "collections": ["FAQ_tender_bm25"],
    "search_params": {"metric_type": "BM25", "params": {"k": 10}},
    "output_fields": ["title", "description"]
}
