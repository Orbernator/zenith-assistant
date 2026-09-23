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
        if zenithConfig.noSocialMedia == False:
            webbrowser.open_new_tab('https://www.reddit.com')
            return('Reddit Opened')
        else:
            return('Social Media has been disabled, please check your config.')
    elif 'twitter' in query:
        if zenithConfig.noSocialMedia == False:
            webbrowser.open_new_tab('https://www.twitter.com')
            return('Twitter Opened')
        else:
            return('Social Media has been disabled, please check your config.')
    elif 'github' in query:
        webbrowser.open_new_tab('https://www.github.com')
        return('Github Opened')
    elif 'instagram' in query:
        if zenithConfig.noSocialMedia == False:
            webbrowser.open_new_tab('https://www.instagram.com')
            return('Instagram Opened')
        else:
            return('Social Media has been disabled, please check your config.')
    elif 'facebook' in query:
        if zenithConfig.noSocialMedia == False:
            webbrowser.open_new_tab('https://www.facebook.com')
            return('Facebook Opened')
        else:
            return('Social Media has been disabled, please check your config.')
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
        if zenithConfig.noAI == False:
            webbrowser.open_new_tab('https://lumo.proton.me/u/0')
            return('Lumo Opened')
        else:
            return('AI has been disabled, please check your config.')
    elif 'chatgpt' in query:
        if zenithConfig.noAI == False:
            webbrowser.open_new_tab('https://chatgpt.com')
            return('ChatGPT Opened')
        else:
            return('AI has been disabled, please check your config.')
    elif 'claude' in query:
        if zenithConfig.noAI == False:
            webbrowser.open_new_tab('https://claude.ai/')
            return('Claude Opened')
        else:
            return('AI has been disabled, please check your config.')
    elif 'gemini' in query:
        if zenithConfig.noAI == False:
            webbrowser.open_new_tab('https://gemini.google.com/app')
            return('Gemini Opened')
        else:
            return('AI has been disabled, please check your config.'),
    elif 'openrouter' in query:
        if zenithConfig.noAI == False:
            webbrowser.open_new_tab('https://openrouter.ai/')
            return('OpenRouter Opened')
        else:
            return('AI has been disabled, please check your config.'),
    elif 'modrinth' in query:
        if zenithConfig.preferDesktop == False:
            webbrowser.open_new_tab('https://modrinth.com/')
            return('Modrinth Opened')
        else:
            return('Desktop App Opening, is not yet implemented')
    elif 'curseforge' in query:
        if zenithConfig.preferDesktop == False:
            webbrowser.open_new_tab('https://curseforge.com/')
            return('Curseforge Opened')
        else:
            return('Desktop App Opening, is not yet implemented')
    elif 'google' in query:
        webbrowser.open_new_tab('https://www.google.com')
        return('Google Opened')
    elif 'brave' in query:
        if zenithConfig.preferDesktop == False:
            webbrowser.open_new_tab('https://search.brave.com/')
            return('Brave Opened')
        else:
            return('Desktop App Opening, is not yet implemented')
    elif 'bing' in query:
        if zenithConfig.sureBing == False:
            webbrowser.open_new_tab('https://www.google.com')
            return('Google Opened, trust me, I am saving you pain')
        else:
            webbrowser.open_new_tab('https://www.bing.com')
            return('Bing Opened')
    elif 'duckduckgo' in query:
        webbrowser.open_new_tab('https://www.duckduckgo.com')
        return('DuckDuckGo Opened')
    elif 'ecosia' in query:
        webbrowser.open_new_tab('https://www.ecosia.org/')
        return('Ecosia Opened')
    elif 'mojeek' in query:
        webbrowser.open_new_tab('https://www.mojeek.com/')
        return('Mojeek Opened')
    elif 'qwant' in query:
        webbrowser.open_new_tab('https://www.qwant.com/')
        return('Qwant Opened')
    elif 'yandex' in query:
        webbrowser.open_new_tab('https://www.yandex.com/')
        return('Yandex Opened')
    elif 'yahoo' in query:
        webbrowser.open_new_tab('https://www.yahoo.com/')
        return('Yahoo Opened')
    elif 'canva' in query:
        if zenithConfig.preferDesktop == False:
            webbrowser.open_new_tab('https://canva.com/')
            return('Canva Opened')
        else:
            return('Desktop App Opening, is not yet implemented')
    elif 'makerworld' in query:
        webbrowser.open_new_tab('https://makerworld.com/')
        return('MakerWord Opened')
    elif 'google maps' in query:
        webbrowser.open_new_tab('https://maps.google.com/')
        return('Google Maps Opened')
    elif 'printables' in query:
        webbrowser.open_new_tab('https://printables.com')
        return('Printables Opened')
    elif 'thingiverse' in query:
        webbrowser.open_new_tab('https://thingiverse.com/')
        return('Thingiverse Opened')
    elif 'proton meet' in query:
        webbrowser.open_new_tab('https://meet.proton.me/')
        return('Proton Meet Opened')
    elif 'selfhost' in query:
        webbrowser.open_new_tab('https://selfh.st/')
        return('Selfh.st Opened')
    elif 'desmos' in query:
        webbrowser.open_new_tab('https://desmos.com/')
        return('Desmos Opened')
    elif 'todoist' in query:
        webbrowser.open_new_tab('https://app.todoist.com/')
        return('Todoist Opened')
    elif 'steam' in query:
        if zenithConfig.preferDesktop == False:
            webbrowser.open_new_tab('https://store.steampowered.com/')
            return('Steam Opened')
        else:
            return('Desktop App Opening, is not yet implemented')
    elif 'epic games' in query:
        if zenithConfig.preferDesktop == False:
            webbrowser.open_new_tab('https://store.epicgames.com/')
            return('Epic Games Opened')
        else:
            return('Desktop App Opening, is not yet implemented')
    elif 'itch io' in query:
        webbrowser.open_new_tab('https://www.itch.io')
        return('Itch Io Opened')
    elif 'gog' or 'gee oh gee' or 'gog.com' or 'gee oh gee dot com' in query:
        webbrowser.open_new_tab('https://www.gog.com/')
        return('GOG Opened')
    elif 'discord' in query:
        if zenithConfig.preferDesktop == False:
            webbrowser.open_new_tab('https://discord.com/channels/@me')
            return('Discord Opened')
        else:
            return('Desktop App Opening, is not yet implemented')
    elif 'mastodon' in query:
        if zenithConfig.noSocialMedia == False:
            webbrowser.open_new_tab('https://mastodon.social')
            return('Mastodon Opened')
        else:
            return('Social Media is disabled, please check your config.')
    elif 'bluesky' or 'bsky' in query:
        if zenithConfig.noSocialMedia == False:
            webbrowser.open_new_tab('https://bsky.app')
            return('Bluesky Opened')
        else:
            return('Social Media is disabled, please check your config.')
    elif 'snapchat' in query:
        if zenithConfig.noSocialMedia == False:
            webbrowser.open_new_tab('https://snapchat.com/web')
            return('SnapChat Opened')
        else:
            return('Social Media is disabled, please check your config.')
    elif 'chess' in query:
        webbrowser.open_new_tab('https://chess.com')
        return('Chess Opened')
    elif 'open front' in query:
        webbrowser.open_new_tab('https://openfront.io')
        return('OpenFront Opened')
    elif 'kizi' in query:
        webbrowser.open_new_tab('https://kizi.com')
        return('Kizi Opened')
    elif 'poki' in query:
        webbrowser.open_new_tab('https://poki.com')
        return('Poki Opened')
    elif 'cool math games' in query:
        webbrowser.open_new_tab('https://coolmathgames.com')
        return('CoolMath Games Opened')
    elif 'crazy games' in query:
        webbrowser.open_new_tab('https://crazygames.com')
        return('CrazyGames Opened')
    elif 'nine news' or '9 news' in query:
        webbrowser.open_new_tab('https://www.nine.com.au')
        return('Nine News Opened')
    elif 'nine now' or '9 now' in query:
        webbrowser.open_new_tab('https://9now.com.au')
        return('Nine Now Opened')
    elif 'seven news' or '7 news' in query:
        webbrowser.open_new_tab('https://7news.com.au')
        return('Seven News Opened')
    elif 'seven plus' or '7 plus' in query:
        webbrowser.open_new_tab('https://7plus.com.au')
        return('Seven Plus Opened')
    elif 'ten news' or '10 news' in query:
        webbrowser.open_new_tab('https://10.com.au')
        return('Ten News Opened')
    elif 'abc news' in query:
        webbrowser.open_new_tab('https://www.abc.net.au')
        return('ABC News Opened')
    elif 'abc ivew' in query:
        webbrowser.open_new_tab('https://ivew.abc.net.au')
        return('ABC Ivew Opened')
    elif 'sbs news' in query:
        webbrowser.open_new_tab('https://www.sbs.com.au')
        return('SBS News Opened')
    elif 'sbs on demand' in query:
        webbrowser.open_new_tab('https://www.sbs.com.au/ondemand')
        return('SBS On Demand Opened')
    elif 'netflix' in query:
        webbrowser.open_new_tab('https://www.netflix.com')
        return('Netflix Opened')
    elif 'stan' in query:
        webbrowser.open_new_tab('https://www.stan.com.au')
        return('Stan Opened')
    elif 'prime video' or 'amazon prime' or 'amazon prime video' in query:
        webbrowser.open_new_tab('https://primevideo.com')
        return('Prime Video Opened')
    elif 'tubi' or 'tubi tv' or 'tubi.tv' in query:
        webbrowser.open_new_tab('https://www.tubitv.com')
        return('Tubi Opened')
    elif 'paramount plus' or 'paramount +' or 'paramountplus' in query:
        webbrowser.open_new_tab('https://www.paramountplus.com')
        return('Paramount Plus Opened')
    elif 'disney plus' or 'disney +' or 'disneyplus' in query:
        webbrowser.open_new_tab('https://www.disneyplus.com')
        return('Disney Plus Opened')
    elif 'hbo max' in query:
        webbrowser.open_new_tab('https://www.hbomax.com')
        return('HBO Max Opened')
    elif 'apple tv' in query:
        webbrowser.open_new_tab('https://tv.apple.com')
        return('Apple TV Opened')
    elif 'crunchyroll' in query:
        webbrowser.open_new_tab('https://crunchyroll.com')
        return('Crunchyroll Opened')
    elif 'dazn' in query:
        webbrowser.open_new_tab('https://dazn.com')
        return('DAZN Opened')
    elif 'jellyfin' in query:
        if zenithConfig.jellyfinAddress == 'NULL':
            return('Jellyfin is not configured')
        else:
            webbrowser.open_new_tab(zenithConfig.jellyfinAddress)
            return('JellyFin Opened')
    elif 'emby' in query:
        if zenithConfig.embyURL == 'NULL':
            return('Emby is not configured')
        else:
            webbrowser.open_new_tab(zenithConfig.embyURL)
            return('Emby Opened')
    elif 'britbox' or 'brit box' in query:
        webbrowser.open_new_tab('https://britbox.com/')
        return('Britbox Opened')
    elif 'kayo' or 'kayo sports' in query:
        webbrowser.open_new_tab('https://kayosports.com.au')
        return('Kayo Opened')
    elif 'binge' in query:
        webbrowser.open_new_tab('https://binge.com.au')
        return('Binge Opened')
    elif 'hayu' in query:
        webbrowser.open_new_tab('https://hayu.com')
        return('Hayu Opened')
    elif 'acorn' or 'acorn tv' in query:
        webbrowser.open_new_tab('https://acorn.tv')
        return('Acorn TV Opened')
    elif 'shudder' in query:
        webbrowser.open_new_tab('https://shudder.com')
        return('Shudder Opened')
    elif 'dropout' or 'dropout tv' in query:
        webbrowser.open_new_tab('https://dropout.tv')
        return('Dropout Opened')
    elif 'nebula' or 'nebula tv' in query:
        webbrowser.open_new_tab('https://nebula.tv')
        return('Nebula Opened')
    elif 'amc' or 'amc plus' or 'amc +' in query:
        webbrowser.open_new_tab('https://amcplus.com')
        return('AMC Plus Opened')
    elif 'plex' in query:
        if zenithConfig.plexURL =='NULL':
            webbrowser.open_new_tab('https://watch.plex.tv')
            return('Plex Opened')
        else:
            webbrowser.open_new_tab(zenithConfig.plexURL)
            return('Plex Opened')
    elif 'deezer' in query:
        webbrowser.open_new_tab('https://deezer.com')
        return('Deezer Opened')
    elif 'apple music' in query:
        webbrowser.open_new_tab('https://music.apple.com')
        return('Apple Music Opened')
    elif 'bandcamp' in query:
        webbrowser.open_new_tab('https://bandcamp.com')
        return('Bandcamp Opened')
    elif 'i heart radio' in query:
        webbrowser.open_new_tab('https://iheart.com')
        return('I heart Radio Opened')
    elif 'pandora' in query:
        webbrowser.open_new_tab('https://pandora.com')
        return('Pandora Opened')
    elif 'qobuz' in query:
        webbrowser.open_new_tab('https://qobuz.com')
        return('Qobuz Opened')
    elif 'SiriusXM' in query:
        webbrowser.open_new_tab('https://siriusxm.com')
        return('SiriusXM Opened')
    elif 'SoundCloud' in query:
        webbrowser.open_new_tab('https://soundcloud.com')
        return('SoundCloud Opened')
    elif 'music.stingray.com' in query:
        webbrowser.open_new_tab('https://music.stingray.com')
        return('Stingray Opened')
    elif 'tidal' in query:
        webbrowser.open_new_tab('https://tidal.com')
        return('Tidal Opened')
    elif 'tunein' or 'tune in' in query:
        webbrowser.open_new_tab('https://tunein.com')
        return('Tunein Opened')
    elif 'youtube music' or 'yt music' in query:
        webbrowser.open_new_tab('https://music.youtube.com')
        return('Youtube Music Opened')
    elif 'xbox' in query:
        if zenithConfig.preferDesktop == False:
            webbrowser.open_new_tab('https://xbox.com')
            return('Xbox Opened')
        else:
            return('Desktop App Opening, not yet supported')
    elif 'playstation' or 'playstation store' in query:
        webbrowser.open_new_tab('https://playstation.com')
        return('Playstation Store Opened')
    elif 'meta quest store' or 'meta quest' in query:
        webbrowser.open_new_tab('https://meta.com/en-gb/experiences')
        return('Meta Quest Store Opened')
    elif 'patreon' in query:
        webbrowser.open_new_tab('https://www.patreon.com/')
        return('Patreon Opened')
    elif 'amazon' in query:
        webbrowser.open_new_tab('https://amazon.com')
        return('Amazon Opened')
    elif 'grokipedia' in query:
        webbrowser.open_new_tab('https://grokipedia.com')
        return('Grokipedia Opened')
    elif 'protected text' in query:
        webbrowser.open_new_tab('https://protectedtext.com/' + zenithConfig.protextedTextURL)
        return('Protected Text Opened')
    else:
        return('Command not Found')
