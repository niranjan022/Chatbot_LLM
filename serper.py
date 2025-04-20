import requests

SERPER_API_KEY = "921e8336bd6bd6273840af552c80e6053439f8ce"

def get_data(query):

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "q": query,
        "gl": "in", 
        "hl": "en"  
    }

    response = requests.post("https://google.serper.dev/search", headers=headers, json=data)

    if response.status_code == 200:
        search_results = response.json()
        
        return search_results
    else:
        print("Search failed:", response.status_code, response.text)    
