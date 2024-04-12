import requests
from requests.exceptions import RequestException

# URL of the application to check
APP_URL = 'https://www.w3schools.com/'

def check_app_health(url):
    """Check the health of the application by sending an HTTP request of w3and evaluating the status code."""
    try:
        response = requests.get(url, timeout=10)  # 10 seconds timeout
        
        if 200 <= response.status_code < 300:
            return "up"
        else:
            return "down"
    except RequestException as e:
        
        print(f"Error when trying to reach {url}: {e}")
        return "down"

if __name__ == "__main__":
    status = check_app_health(APP_URL)
    print(f"The application status is: {status}")
