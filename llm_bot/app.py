import streamlit as st
from openai import OpenAI

from search import search_chunks
from config import BASE_URL, LLM_NAME

client = OpenAI(
    api_key="EMPTY",
    base_url=BASE_URL
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 RAG Chatbot")
st.caption("🔍 Поиск по базе знаний + LLM")

with st.sidebar:
    st.header("Настройки")
    if st.button("🧹 Очистить историю"):
        st.session_state.messages = []

def generate_response(query: str) -> str:
    chunks = search_chunks(query)
    context = "\n".join([f"{idx+1}. {chunk['title']}: {chunk['content']}" 
                       for idx, chunk in enumerate(chunks)])
    
    messages = [{"role": "user", "content": f"Контекст:\n{context}\n\nВопрос: {query}"}]
    
    response = client.chat.completions.create(
        model=LLM_NAME,
        messages=messages,
        stream=True
    )
    
    return response, chunks

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ваш вопрос:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            response, chunks = generate_response(prompt)
            full_response = ""
            message_placeholder = st.empty()
            
            for chunk in response:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
            with st.expander("🔍 Использованные источники"):
                for chunk in chunks:
                    st.write(f"**{chunk['title']}** (score: {chunk['score']:.2f})")
                    st.caption(chunk["content"])
                    st.divider()
                    
        except Exception as e:
            st.error(f"Ошибка генерации: {str(e)}")