import requests

def fetch_pypi_package(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)

    if response.status_code != 200:
        return None
    
    return response.json()