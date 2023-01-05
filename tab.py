import os
import colorama
from colorama import init, Fore, Style
try:
    importlib.import_module('colorama')
except ImportError:
    os.system("pip install colorama")
try:
    importlib.import_module('links')
except ImportError:
    os.system("apt install links")
def menu():

    print("""
      ▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌
   ▄▄██▌█░░TabNews░░░▐  -----
▄▄▄▌▐██▌█░░░░░░░░░░░░▐ ----
███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▌ -------
▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀
========================================
Por: Jetrom
Github: Jetrom17
Version 1.1
----
🤖 Queira contribuir: https://github.com/Jetrom17/TabNews_Terminal.git
ou
Doe um tabCoin =)
----
==========================================
00. E-mail para sugestões
==========================================
1. 30 comandos básico para ser usado no Terminal Linux + [Bônus]
2. API para consulta de encomendas 📦
3. [Pitch] - TabNews Mobile - React Native
4. MAIS Extensões MARAVILHOSAS para o Vscode!
5. Me dê API
6. Brasil API
7. Me dê RSS
==========================================
   |Termux|
      ||
|8. Termux-API|
---------------
9. Deezer - Dados vazados
==========================================
z. Verificar atualização deste repositório 
x. SAIR
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("Você terá meu contato via e-mail. Meu provedor não é Google e nem Protonmail.")
        print("----------------")
        hm = input("Tem certeza que queres meu contato via e-mail? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            repo = input("Opa! Antes te dá meu e-mail, tenho que atualizar e dá upgrade em seu repositório se disponível, ok? (y,n): ")
            if repo == "y":
                print("========================================================")
                os.system("apt update -y")
                os.system("apt upgrade -y")
                os.system("clear")
                print(Fore.GREEN + "📩 Jetrom@mail2tor.com")
                print("========================================")
                print("[+] Repositórios supostamente atualizados")
                print("[+] Dado upgrade")
                print('''         
▒▒▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▒
▒▒▒▒▒▒▄▀▀▓▓▓▀█▒▒▒▒▒▒
▒▒▒▒▄▀▓▓▄██████▄▒▒▒▒
▒▒▒▄█▄█▀░░▄░▄░█▀▒▒▒▒
▒▒▄▀░██▄░░▀░▀░▀▄▒▒▒▒
▒▒▀▄░░▀░▄█▄▄░░▄█▄▒▒▒
▒▒▒▒▀█▄▄░░▀▀▀█▀▒▒▒▒▒
▒▒▒▄▀▓▓▓▀██▀▀█▄▀▀▄▒▒
▒▒█▓▓▄▀▀▀▄█▄▓▓▀█░█▒▒
▒▒▀▄█░░░░░█▀▀▄▄▀█▒▒▒
▒▒▒▄▀▀▄▄▄██▄▄█▀▓▓█▒▒
▒▒█▀▓█████████▓▓▓█▒▒
▒▒█▓▓██▀▀▀▒▒▒▀▄▄█▀▒▒
▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
''')
                print("Agora você tem estrela invencível de Mario!.")
                print("========================================")
            else:
                rmenu = input("Cancelado, voltar ao menu? (y/n): ")
                if rmenu == "y":
                    menu()
    elif what == "1":
        os.system("links https://www.tabnews.com.br/Jetrom/30-comandos-basico-para-ser-usado-no-terminal-linux-bonus")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("links https://www.tabnews.com.br/NathanFirmo/api-para-consulta-de-encomendas")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("links https://www.tabnews.com.br/danielkv/tabnews-mobile-react-native")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("links https://www.tabnews.com.br/josevictormoreno/mais-extensoes-maravilhosas-para-o-vscode")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("https://www.tabnews.com.br/api/v1/contents")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("https://brasilapi.com.br/")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        print("https://www.tabnews.com.br/recentes/rss")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg install termux-api")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "9":
        os.system("termux-open-url https://www.tabnews.com.br/Jetrom/deezer-dados-vazados")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "z":
        os.system("rm -rf TabNews_Terminal")
        os.system("git clone https://github.com/Jetrom17/TabNews_Terminal.git")
        os.system("cd TabNews_Terminal")
        os.system("python3 tab.py")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "x":
        print("Tchau!")
        break
