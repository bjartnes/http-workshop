from urllib3.util.retry import Retry
import requests
from requests.adapters import HTTPAdapter

def retry_session(retries, session=None, backoff_factor=3, backoff_max=3):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        backoff_max = backoff_max
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

retry3 = retry_session(3)

response = retry3.get("http://localhost:3000/timeout", timeout=10)
print(response)
