import requests

def get_data_from_google_sheets_api():
    url = "https://script.google.com/macros/s/AKfycbzMESx_2wn9d9NWjfK80Y3IdQLP_r1xoB2kC6mHibeDsx2ds3lHzQdzILjqOFOzi1pLBA/exec"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Falha ao acessar a API:", response.status_code)
            return None
    except Exception as e:
        print("Erro ao acessar a API:", str(e))
        return None