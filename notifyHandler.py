import requests
import zenithConfig
def notifySort(query):
    if 'ntfy' in query:
        query = query.replace("ntfy", "")
        requests.post("https://ntfy.sh/"+ zenithConfig.ntfyURL, data=query.encode('utf-8'))