import os
import colorama

os.environ['UI_PATH'] = 'utilities/UI/_ui'

from .errs import *
from .ard import *
from .UI import *


def log(text, t='msg', cls=False):
    head = {
        'msg': f'{colorama.Fore.GREEN}MESSAGE:{colorama.Fore.RESET}',
        'err': f'{colorama.Fore.RED}FATAL ERROR:{colorama.Fore.RESET}',
        'wrn': f'{colorama.Fore.YELLOW}WARNING:{colorama.Fore.RESET}',
    }[t]
    if cls:
        os.environ['CONSOLE_CLS'] = '1'
        print('\r' + head + " " + text, end='')
    else:
        if os.environ.get('CONSOLE_CLS') == '1':
            print()
        os.environ['CONSOLE_CLS'] = '0'
        print(head + " " + text)


print(f"""{colorama.Fore.BLUE}
88b           d88                                             88           88               88                    
888b         d888                                             88           ""               88             ,d     
88`8b       d8'88                                             88                            88             88     
88 `8b     d8' 88   ,adPPYba,    ,adPPYba,   8b,dPPYba,       88           88   ,adPPYb,d8  88,dPPYba,   MM88MMM  
88  `8b   d8'  88  a8"     "8a  a8"     "8a  88P'   `"8a      88           88  a8"    `Y88  88P'    "8a    88     
88   `8b d8'   88  8b       d8  8b       d8  88       88      88           88  8b       88  88       88    88     
88    `888'    88  "8a,   ,a8"  "8a,   ,a8"  88       88      88           88  "8a,   ,d88  88       88    88,    
88     `8'     88   `"YbbdP"'    `"YbbdP"'   88       88      88888888888  88   `"YbbdP"Y8  88       88    "Y888  
                                                                                aa,    ,88                        
{colorama.Style.RESET_ALL}Команда "Лунный свет", 2022 год, НТО - Фотоника. Все права защищены.{colorama.Fore.BLUE}             "Y8bbdP"
""")

os.chdir(os.environ.get('PWD'))
