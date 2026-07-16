import requests

def get_match(match_id):

    url = f"https://api.opendota.com/api/matches/8872864614"


# def get_match(match_id):

#     

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return None

def get_heroes():

    url = "https://api.opendota.com/api/heroes" # tujuan dapatkan data untuk mapping heroes

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return None

### TUJUAN : DISPLAY PLAYER + HERO + STATS

def get_items():

    url = "https://api.opendota.com/api/constants/items" # tujuan dapatkan data untuk mapping items
    
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return None