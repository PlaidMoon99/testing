import google.generativeai as genai


google_api_key = "AIzaSyDgzsS6mn3ozqSYbfwwsC-21uD_BPniIpg"

genai.configure(api_key=google_api_key)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("요즘 인스타에서 유행하는 여행지 있어?")

print(response.text)
