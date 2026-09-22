import webbrowser
import zenithConfig
def openSort(query):
    if 'youtube' in query:
        webbrowser.open_new_tab('https://www.youtube.com')
        return('Youtube Opened')
    elif 'wikipedia' in query:
        webbrowser.open_new_tab('https://wikipedia.org')
        return('Wikipedia Opened')
    elif 'reddit' in query:
        webbrowser.open_new_tab('https://www.reddit.com')
        return('Reddit Opened')
    elif 'twitter' in query:
        webbrowser.open_new_tab('https://www.twitter.com')
        return('Twitter Opened')
    elif 'github' in query:
        webbrowser.open_new_tab('https://www.github.com')
        return('Github Opened')
    elif 'instagram' in query:
        webbrowser.open_new_tab('https://www.instagram.com')
        return('Instagram Opened')
    elif 'facebook' in query:
        webbrowser.open_new_tab('https://www.facebook.com')
        return('Facebook Opened')
    elif 'spotify' in query:
        if zenithConfig.preferDesktop == False:
            webbrowser.open_new_tab('https://www.spotify.com')
            return('Spotify Opened')
        else:
            return('Not Yet Implemented')
    elif 'gmail' in query:
        webbrowser.open_new_tab('https://mail.google.com/mail/u/0')
        return('Gmail Opened')
    elif 'outlook' in query:
        webbrowser.open_new_tab('https://live.outlook.com/mail/0')
        return('Outlook Opened')
    elif 'proton mail' in query:
        webbrowser.open_new_tab('https://mail.proton.me/u/0')
        return('Proton Mail Opened')
    elif 'proton drive' in query:
        webbrowser.open_new_tab('https://drive.proton.me/u/0')
        return('Proton Drive Opened')
    elif 'proton calender' in query:
        webbrowser.open_new_tab('https://calender.proton.me/u/0')
        return('Proton Calender Opened')
    elif 'lumo' in query:
        webbrowser.open_new_tab('https://lumo.proton.me/u/0')
        return('Lumo Opened')
    elif 'chatgpt' in query:
        webbrowser.open_new_tab('https://chatgpt.com')
