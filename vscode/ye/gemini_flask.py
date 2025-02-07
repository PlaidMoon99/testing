from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import re

app = Flask(__name__)
CORS(app)

# Gemini API 설정
genai.configure(api_key="AIzaSyDgzsS6mn3ozqSYbfwwsC-21uD_BPniIpg")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

@app.route('/', methods=['POST'])
def chat_response():
    if request.method == 'POST':
        try:
            data = request.get_json()
            user_message = data.get('message')
            
            if not user_message:
                return jsonify({"error": "메시지가 없습니다"}), 400
                
            response = chat.send_message(user_message)
            return jsonify({"response": response.text})
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
# def format_response(text):
#     """
#     Gemini 응답을 보기 좋게 변환
#     """
#     text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)  # **텍스트** → 텍스트 (굵은 글씨 제거)
#     text = text.replace("\n", "<br>")  # 개행을 <br> 태그로 변환
#     text = re.sub(r"- (.+)", r"• \1", text)  # 리스트(- item)를 점 리스트(• item)로 변환

#     return text


if __name__ == '__main__':
    app.run(port=8501, debug=True)