import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
token = "11111111111111111111111111"
chat_id = "111111111111111111111"

# Function to send a message to Telegram
def send_msg(text):
    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    results = requests.get(url_req)
    print(results.json())

while True:
    # Create variables for tuNgay and denNgay
    tuNgay = datetime.now().strftime('%d-%m-%Y')
    denNgay = (datetime.now() + timedelta(days=6)).strftime('%d-%m-%Y')

    # Set query parameters
    params = {
        'tuNgay': tuNgay,
        'denNgay': denNgay,
        'maKH': '1111111111111111111111111111111111111111111111',
        'ChucNang': 'MaKhachHang'
    }

    # URL address
    url = 'https://cskh.evnspc.vn/TraCuu/GetThongTinLichNgungGiamMaKhachHang'

    # Send an HTTP GET request with the specified query parameters
    response = requests.get(url, params=params)

    # Get the response content
    response_content = response.text

    # Use BeautifulSoup to remove HTML tags
    soup = BeautifulSoup(response_content, 'html.parser')
    text_without_tags = soup.get_text()

    # Split the text into lines, strip leading whitespace, and join them back
    cleaned_text = '\n'.join(line.strip() for line in text_without_tags.splitlines())

    # Check if the response contains the specific phrase
    if "Lý do mất điện" in cleaned_text:
        # Send the cleaned response content to Telegram
        send_msg(cleaned_text)
    else:
        print("Response does not contain 'Lý do mất điện'. Message not sent.")

    # Sleep for 2 hours (7200 seconds) before running the loop again
    time.sleep(7200)
