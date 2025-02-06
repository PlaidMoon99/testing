# st_chatbot.py
import google.generativeai as genai 
import streamlit as st

# ✅ Google Gemini API 키 설정
genai.configure(api_key="AIzaSyDgzsS6mn3ozqSYbfwwsC-21uD_BPniIpg")  # 여기에 API 키 입력

st.title("Gemini-Bot")

@st.cache_resource
def load_model():
    model = genai.GenerativeModel('gemini-pro')
    print("model loaded...")
    return model

model = load_model()

if "chat_session" not in st.session_state:    
    st.session_state["chat_session"] = model.start_chat(history=[]) 

for content in st.session_state.chat_session.history:
    with st.chat_message("ai" if content.role == "model" else "user"):
        st.markdown(content.parts[0].text)

if prompt := st.chat_input("메시지를 입력하세요."):    
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("ai"):
        try:
            response = st.session_state.chat_session.send_message(prompt)
            if response and response.text:
                st.markdown(response.text)
            else:
                st.markdown("챗봇의 응답을 받을 수 없습니다.")
        except Exception as e:
            st.markdown(f"에러 발생: {e}")

