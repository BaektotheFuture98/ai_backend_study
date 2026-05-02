import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
v_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=v_api_key)
model = 'models/gemini-embedding-001'

result = genai.embed_content(
    model = model,
    content = "안녕하세요 AI 백엔드 개발자 백선민입니다.",
    task_type = "retrieval_document"
)   


print(result['embedding'])
print(f"임베딩 벡터의 차원 수: {len(result['embedding'])}")