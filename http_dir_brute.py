import requests

def brute_force_dirs(base_url, wordlist):
    found = []
    for word in wordlist:
        url = f"{base_url}/{word.strip()}"
        response = requests.get(url)
        if response.status_code == 200:
            found.append(url)
            print(f"[+] Found: {url}")
    return found
