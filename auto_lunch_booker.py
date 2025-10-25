import requests
from datetime import datetime, timedelta

# ---- Configuration ----
EMP_ID = "250205"
LOCATION_TIC = "77337997"  # Your TIC building code
URL = "https://www.ulka.autos/booking/apis/book-lunch-token/"

# Your CSRF token and cookies (you may need to refresh this periodically)
CSRF_TOKEN = "zsnuBhp6ta8BG4bOnGLHOfIQiA9TMSxJ"
COOKIES = {
    "csrftoken": CSRF_TOKEN,
    "g_state": '{"i_l":0,"i_ll":1761153721276}'
}

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Origin": "https://www.ulka.autos",
    "Referer": "https://www.ulka.autos/lunch-booking",
    "X-CSRFToken": CSRF_TOKEN,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# ---- Logic ----
def get_next_day():
    """Return next weekday (Sunday to Thursday)"""
    today = datetime.now()
    next_day = today + timedelta(days=1)
    # Skip Friday or Saturday
    if next_day.weekday() == 4:  # Friday
        next_day += timedelta(days=2)
    elif next_day.weekday() == 5:  # Saturday
        next_day += timedelta(days=1)
    return next_day.strftime("%A")

def book_lunch():
    payload = {
        "empid": EMP_ID,
        "location": LOCATION_TIC
    }

    response = requests.post(URL, headers=HEADERS, cookies=COOKIES, json=payload)
    
    if response.status_code == 200:
        print(f"✅ Lunch booked for {get_next_day()} at TIC building!")
    else:
        print(f"❌ Booking failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    book_lunch()
