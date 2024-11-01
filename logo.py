from colorama import Fore, Style, init
init(autoreset=True)

def display_logo():
    logo = Fore.GREEN + """
    ░█████╗░████████╗███╗░░░███╗░█████╗░░██████╗██████╗░██╗░░██╗███████╗██████╗░███████╗██╗░░██╗
    ██╔══██╗╚══██╔══╝████╗░████║██╔══██╗██╔════╝██╔══██╗██║░░██║██╔════╝██╔══██╗██╔════╝╚██╗██╔╝
    ███████║░░░██║░░░██╔████╔██║██║░░██║╚█████╗░██████╔╝███████║█████╗░░██████╔╝█████╗░░░╚███╔╝░
    ██╔══██║░░░██║░░░██║╚██╔╝██║██║░░██║░╚═══██╗██╔═══╝░██╔══██║██╔══╝░░██╔══██╗██╔══╝░░░██╔██╗░
    ██║░░██║░░░██║░░░██║░╚═╝░██║╚█████╔╝██████╔╝██║░░░░░██║░░██║███████╗██║░░██║███████╗██╔╝╚██╗
    ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    """ + Style.RESET_ALL
    print(logo)
    print("\n")