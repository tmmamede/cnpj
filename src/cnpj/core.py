import requests

def fetch_cnpj_data(cnpj):
    """Fetch CNPJ data from minhareceita.org."""
    url = f'https://minhareceita.org/{cnpj}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
