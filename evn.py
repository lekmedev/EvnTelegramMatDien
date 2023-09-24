import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time

token = "laaaaaaaaaaaaaaaaaaaaaaaa"
chat_id = "laaaaaaaaaaaaaaaaaaaaaaaa"

# Function to send a message to Telegram
def send_msg(text):
    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    results = requests.get(url_req)
    print(results.json())

while True:
    # Get the current date and time
    current_datetime = datetime.now()

    # Check if it's a new day (midnight)
    if current_datetime.hour == 0 and current_datetime.minute == 0:
        # Reset the loop to check for messages again
        print("Resetting the loop to check for messages.")
        time.sleep(60)  # Sleep for 1 minute to avoid constant checks
        continue

    # Create variables for tuNgay and denNgay
    tuNgay = current_datetime.strftime('%d-%m-%Y')
    denNgay = (current_datetime + timedelta(days=6)).strftime('%d-%m-%Y')

    # Set query parameters
    params = {
        'tuNgay': tuNgay,
        'denNgay': denNgay,
        'maKH': 'laaaaaaaaaaaaaaaaaaaaaaaa',
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
        print("Message sent. Pausing the loop until the end of the day.")
        
        # Calculate the time until the end of the day (midnight)
        time_until_midnight = (current_datetime + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0) - current_datetime

        # Sleep until the end of the day
        time.sleep(time_until_midnight.total_seconds())
    else:
        print("Response does not contain 'Lý do mất điện'. Message not sent.")
        send_msg("Still Work")
    # Sleep for 2 hours (7200 seconds) before checking again
    time.sleep(7200)
