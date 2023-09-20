import requests


wiki_url = "https://www.wikidata.org/w/api.php"

def fetch_pagedata(ids):
    params = {
        'action': 'wbgetentities',
        'ids': ids,
        'format': 'json',
        'languages': 'en'
    }
    try:

        data = requests.get(wiki_url, params)
        return {"status": True, "data": data.json(), "status_code": 200}
    except Exception as e:
        return {"status": False, "data": {}, "status_code": 400}
