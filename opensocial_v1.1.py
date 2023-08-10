import requests
import concurrent.futures

username = input('\033[31m{+} Enter username:')


#SNAPCHAT
snapchat = f'https://www.snapchat.com/add/{username}'

# INSTAGRAM
instagram = f'https://www.instagram.com/{username}'

#REDDIT
reddit = f'https://www.reddit.com/user/{username}'

# FACEBOOK
facebook = f'https://www.facebook.com/{username}'

#TWITTER
twitter = f'https://www.twitter.com/{username}'

# YOUTUBE
youtube = f'https://www.youtube.com/{username}'

# BLOGGER
blogger = f'https://{username}.blogspot.com'

# GOOGLE+
google_plus = f'https://plus.google.com/s/{username}/top'

# REDDIT
reddit = f'https://www.reddit.com/user/{username}'

# WORDPRESS
wordpress = f'https://{username}.wordpress.com'

# PINTEREST
pinterest = f'https://www.pinterest.com/{username}'

# GITHUB
github = f'https://www.github.com/{username}'

# TUMBLR
tumblr = f'https://{username}.tumblr.com'

# FLICKR
flickr = f'https://www.flickr.com/people/{username}'

# STEAM
steam = f'https://steamcommunity.com/id/{username}'

# VIMEO
vimeo = f'https://vimeo.com/{username}'

# SOUNDCLOUD
soundcloud = f'https://soundcloud.com/{username}'

# DISQUS
disqus = f'https://disqus.com/by/{username}'

# MEDIUM
medium = f'https://medium.com/@{username}'

# DEVIANTART
deviantart = f'https://{username}.deviantart.com'

# VK
vk = f'https://vk.com/{username}'

# ABOUT.ME
aboutme = f'https://about.me/{username}'

# IMGUR
imgur = f'https://imgur.com/user/{username}'

# FLIPBOARD
flipboard = f'https://flipboard.com/@{username}'

# SLIDESHARE
slideshare = f'https://slideshare.net/{username}'

# FOTOLOG
fotolog = f'https://fotolog.com/{username}'

# SPOTIFY
spotify = f'https://open.spotify.com/user/{username}'

# MIXCLOUD
mixcloud = f'https://www.mixcloud.com/{username}'

# SCRIBD
scribd = f'https://www.scribd.com/{username}'

# BADOO
badoo = f'https://www.badoo.com/en/{username}'

# PATREON
patreon = f'https://www.patreon.com/{username}'

# BITBUCKET
bitbucket = f'https://bitbucket.org/{username}'

# DAILYMOTION
dailymotion = f'https://www.dailymotion.com/{username}'

# ETSY
etsy = f'https://www.etsy.com/shop/{username}'

# CASHME
cashme = f'https://cash.me/{username}'

# BEHANCE
behance = f'https://www.behance.net/{username}'

# GOODREADS
goodreads = f'https://www.goodreads.com/{username}'

# INSTRUCTABLES
instructables = f'https://www.instructables.com/member/{username}'

# KEYBASE
keybase = f'https://keybase.io/{username}'

# KONGREGATE
kongregate = f'https://kongregate.com/accounts/{username}'

# LIVEJOURNAL
livejournal = f'https://{username}.livejournal.com'

# ANGELLIST
angellist = f'https://angel.co/{username}'

# LAST.FM
last_fm = f'https://last.fm/user/{username}'

# DRIBBBLE
dribbble = f'https://dribbble.com/{username}'

# CODECADEMY
codecademy = f'https://www.codecademy.com/{username}'

# GRAVATAR
gravatar = f'https://en.gravatar.com/{username}'

# PASTEBIN
pastebin = f'https://pastebin.com/u/{username}'

# FOURSQUARE
foursquare = f'https://foursquare.com/{username}'

# ROBLOX
roblox = f'https://www.roblox.com/user.aspx?username={username}'

# GUMROAD
gumroad = f'https://www.gumroad.com/{username}'

# NEWSGROUND
newsground = f'https://{username}.newgrounds.com'

# WATTPAD
wattpad = f'https://www.wattpad.com/user/{username}'

# CANVA
canva = f'https://www.canva.com/{username}'

# CREATIVEMARKET
creative_market = f'https://creativemarket.com/{username}'

# TRAKT
trakt = f'https://www.trakt.tv/users/{username}'

# BUZZFEED
buzzfeed = f'https://buzzfeed.com/{username}'

# HUBPAGES
hubpages = f'https://{username}.hubpages.com'

# CONTENTLY
contently = f'https://{username}.contently.com'

# HOUZZ
houzz = f'https://houzz.com/user/{username}'

#BLIP.FM
blipfm = f'https://blip.fm/{username}'

# WIKIPEDIA
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

# HACKERNEWS
hackernews = f'https://news.ycombinator.com/user?id={username}'

#DEVIANTART
deviantart = f'https://www.deviantart.com/{username}'

# CODEMENTOR
codementor = f'https://www.codementor.io/{username}'

# REVERBNATION
reverb_nation = f'https://www.reverbnation.com/{username}'

# DESIGNSPIRATION
designspiration = f'https://www.designspiration.net/{username}'

# BANDCAMP
bandcamp = f'https://www.bandcamp.com/{username}'

# COLOURLOVERS
colourlovers = f'https://www.colourlovers.com/love/{username}'

# IFTTT
ifttt = f'https://www.ifttt.com/p/{username}'

# EBAY
ebay = f'https://www.ebay.com/usr/{username}'

#TWITCH
twitch = f'https://www.twitch.tv/{username}'

#QUORA
quora = f'https://www.quora.com/profile/{username}'

#LINKEDIN
linkedin = f'https://www.linkedin.com/in/{username}'

''' WEBSITE LIST - USE FOR SEARCHING OF USERNAME '''
WEBSITES = [
instagram, reddit, facebook, twitter, youtube, blogger, google_plus, reddit,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
wattpad, canva, creative_market, trakt, buzzfeed, hubpages,
contently, houzz, blipfm, wikipedia, hackernews, deviantart, reverb_nation, designspiration,
bandcamp, colourlovers, ifttt, ebay, patreon,twitch,quora,linkedin,
]


''' COLOUR PRINTING FUNCTION '''
def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function


''' COLOUR PRINTS '''
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')


''' BANNER '''
def banner():
    RED(r'''
 ________  ________  _______   ________   ________  ________  ________  ___  ________  ___          
|\   __  \|\   __  \|\  ___ \ |\   ___  \|\   ____\|\   __  \|\   ____\|\  \|\   __  \|\  \         
\ \  \|\  \ \  \|\  \ \   __/|\ \  \\ \  \ \  \___|\ \  \|\  \ \  \___|\ \  \ \  \|\  \ \  \        
 \ \  \\\  \ \   ____\ \  \_|/_\ \  \\ \  \ \_____  \ \  \\\  \ \  \    \ \  \ \   __  \ \  \       
  \ \  \\\  \ \  \___|\ \  \_|\ \ \  \\ \  \|____|\  \ \  \\\  \ \  \____\ \  \ \  \ \  \ \  \____  
   \ \_______\ \__\    \ \_______\ \__\\ \__\____\_\  \ \_______\ \_______\ \__\ \__\ \__\ \_______\
    \|_______|\|__|     \|_______|\|__| \|__|\_________\|_______|\|_______|\|__|\|__|\|__|\|_______|
                                            \|_________|                                            
  
  By SeranoxSecurity //Origin Credit: w3w3w3                                                                                                  

                                                                                                    
  ''')


def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function

GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')

def banner():
    RED(r'''
    ... (your banner art) ...
  By SeranoxSecurity //Credit: w3w3w3
    ''')

def search():
    GREEN(f'[+] Searching for username: {username}')
    GREEN(f'[+] Open Social v1.00 is working')

    count = 0
    match = True

    for url in WEBSITES:
        r = requests.get(url)

        if r.status_code == 200:
            if match:
                GREEN('[+] FOUND MATCHES')
                match = False
            YELLOW(f'\n{url} - {r.status_code} - OK')
            if username in r.text:
                GREEN(f'POSITIVE MATCH: Username:{username} - text has been detected in URL.')
            else:
                RED(f'POSITIVE MATCH: Username:{username} - text has NOT been detected in URL.')
        count += 1

    total = len(WEBSITES)
    GREEN(f'FINISHED: A total of {count} MATCHES found out of {total} websites.')

if __name__ == '__main__':
    banner()
    search()
