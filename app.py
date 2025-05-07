import sys
import os
import subprocess
import webbrowser
import os
from colorama import init, Fore, Style
import json


init(autoreset=True)
red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
black = Fore.LIGHTBLACK_EX
white = Fore.LIGHTWHITE_EX
endc = Style.RESET_ALL
magenta = Fore.LIGHTMAGENTA_EX


config_search = 'config_search.json'


if not os.path.exists(config_search):
    with open(config_search, 'w') as f:
        _config = {
                'websites': {
                    'geeksforgeeks.org': True,
                    'w3schools.com': True,
                    'stackoverflow.com': True,
                    'github.com': True,
                    'reddit.com': True,
                    'youtube.com': True,
                    'medium.com': True,
                    'stackexchange.com': True
                }
            }
    
        f.write(json.dumps(_config, indent=4))
        print(f'{yellow}Config file created{endc}')

f = open(config_search, 'r')
if f.read() == '':
    with open(config_search, 'w') as f:
        _config = {
                'websites': {
                    'geeksforgeeks.org': True,
                    'w3schools.com': True,
                    'stackoverflow.com': True,
                    'github.com': True,
                    'reddit.com': True,
                    'youtube.com': True,
                    'medium.com': True,
                    'stackexchange.com': True
                }
            }
    
        f.write(json.dumps(_config, indent=4))
        # print(f'{yellow}Config file created{endc}')



"""
    for index, website in enumerate(websites):
        print(f'{index+1}. {website} : \t{green + "True" + endc if config[website] else red + "False" + endc}')
"""



# browser = '/usr/bin/google-chrome-stable %s'
browser = '/usr/bin/firefox'
url_search = 'https://www.google.com/search?q='


def filter():
    with open(config_search, 'r') as f:
        config = json.load(f)
        config = config['websites']
        websites = [website for website in config.keys() if config[website]]

    filter = ' ('
    for index, website in enumerate(websites):
      
        if index == len(websites) - 1:
            filter += f'site:{website})'
        else:
            filter += f'site:{website} OR '

    return filter


def url_filter(string):
    return f'{string}'

def operation(operation):
    if None: pass

    match operation:
        case '-c':
            while True:
                with open(config_search, 'r') as f:
                    config = json.load(f)
                    config = config['websites']
                    websites = list(config.keys())

                    for index, website in enumerate(websites):
                        print(f'{index+1}. {website} : \t{green + "True" + endc if config[website] else red + "False" + endc}')
                
                    option = input("Enter the website number to toggle (or press eny key for exit): ") 
                    try:
                        if option == 'q':
                            sys.exit()

                        option = int(option) - 1

                        with open(config_search, 'w') as f:
                            config[websites[option]] = False if config[websites[option]] else True
                            os.system('clear')
                            f.write(json.dumps({'websites': config}, indent=4))
                    except:
                        sys.exit()

        case '-h':
            print(f'{yellow}app <search query>{endc}:   to search the query')
            print(f'{yellow}app -c{endc}                to configure the search results')
            print(f'{yellow}app -h{endc}                to get help')
            sys.exit()

        case '':
            print(f'No search query provided! Use {yellow}"app -h"{endc} for help')
            sys.exit()
        case _:
            pass


try:
    operation(sys.argv[1])
except:
     pass
# print(string)

string = ' '.join(sys.argv[1:])
if string not in ['', '-c', '-h']:
    webbrowser.get(browser).open_new_tab(url_search + url_filter(string) + filter())







            




