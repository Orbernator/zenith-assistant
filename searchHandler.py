import wikipediaapi
from wikipediaapi._wikipedia import wikipedia

import zenithConfig
wiki_config = wikipediaapi.Wikipedia(user_agent='ZenithAssistant/1.0 (https://github.com/orbernator/zenith-assistant) Wikipedia-API 0.16.0')

def sortSearch(query):
    if 'wikipedia' in query:
        call_page = wiki_config.page('query')
        return wikipedia.summary(call_page, sentences=2)
    else:
        if zenithConfig.searchEngine == 'google':
            print('Search not yet implemented')
        return None