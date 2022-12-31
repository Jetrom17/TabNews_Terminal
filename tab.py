import os
from colorama import init, Fore, Style
os.system("pip install colorama")
def menu():

    print("""
      ▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌
   ▄▄██▌█░░TabNews░░░▐
▄▄▄▌▐██▌█░░░░░░░░░░░░▐
███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▌
▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀
========================================
Por: Jetrom
Github: Jetrom17
Version 1.1
----
🤖 Queira contribuir: https://github.com/Jetrom17/TabNews_Terminal.git
----
==========================================
00. E-mail para sugestões
==========================================
1. + de 15 alternativas ao Heroku - mas nem todas grátis!
2. CHAT GPT: COMO FUNCIONA A PLATAFORMA de I.A
3. Pitch: App TabNews em Flutter
4. MAIS Extensões MARAVILHOSAS para o Vscode!
5. 🔧 14 ferramentas essenciais para aumentar sua produtividade em 10x
6. Sobre Tabcoins no TabNews
7. Me dê RSS
8. Me dê API
999. Baixar ferramenta "links"
==========================================
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
            repo = input("Opa! Antes te dá meu e-mail, posso atualizar e dá upgrade em seu repositório, se disponível? (y,n): ")
            if repo == "y":
                print("========================================================")
                os.system("apt update -y")
                os.system("apt upgrade -y")
                os.system("clear")
                print(Fore.GREEN + "📩 Jetrom@mail2tor.com")
                print("========================================")
                print("[+] Repositórios supostamente atualizados")
                print("[+] Dado upgrade")
                print('''         ,     ,
            (\____/)
             (_oo_)
               (O)
              __||__    \)
           []/______\[] /
           / \______/ \/
          /    /__\
         (\   /____\

''')
                print("Agora você tem poderes de uma vaca!")
                print("========================================")
            else:
                rmenu = input("Cancelado, voltar ao menu? (y/n): ")
                if rmenu == "y":
                    menu()
    elif what == "1":
        os.system("links https://www.tabnews.com.br/uriel/de-15-alternativas-ao-heroku-mas-nem-todas-gratis")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("links https://www.tabnews.com.br/LucasEd/chat-gpt-como-funciona-a-plataforma-capaz-de-escrever-artigos-e-roteiros")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("links https://www.tabnews.com.br/adlerluiz/pitch-app-tabnews-em-flutter")
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
        os.system("links https://www.tabnews.com.br/jaswdr/14-ferramentas-essenciais-para-aumentar-sua-produtividade-em-10x")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("links https://www.tabnews.com.br/filipedeschamps/nova-melhoria-tabcoins-tabcash-e-melhorias-no-layout")
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
        print("https://www.tabnews.com.br/api/v1/contents")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "999":
        os.system("apt install links -y")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "x":
        print("Tchau!")
        break
