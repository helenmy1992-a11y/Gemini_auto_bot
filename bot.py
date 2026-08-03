import os
from google import genai

def main():
    # Khởi tạo client, thư viện sẽ tự động nhận diện biến môi trường GEMINI_API_KEY
    client = genai.client()

    # Yêu cầu Gemini tạo nội dung (bạn có thể thay đổi câu lệnh theo ý muốn)
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents='Hãy viết một câu danh ngôn ngắn gọn truyền cảm hứng bắt đầu ngày mới.',
    )
    
    print("--- KẾT QUẢ TỪ GEMINI ---")
    print(response.text)

if __name__ == '__main__':
    main()
