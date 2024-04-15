import os
from time import sleep

def menu():
    while True:
        print('''
============== Aplicativo Contatos ==============

    1 • Ligar
    2 • Listar Contatos
    3 • Adicionar Contato
    4 • Editar Contato
    5 • Excluir Contato
    6 • Sair

=================================================
''')
        
        try:
            operacao = int(input("Escolha uma opção: "))
            if operacao == 1:
                limpar_tela()
                ligar()
            elif operacao == 2:
                limpar_tela()
                listarcontatos()
            elif operacao == 3: 
                limpar_tela()   
                add_contato()
            elif operacao == 4:
                limpar_tela()
                editarcontato()
            elif operacao == 5:
                limpar_tela()
                excluircontato()
            else:
                limpar_tela()
                break

        except:
            print("Escolha uma opção valida!")

def add_contato():
    while True:
        print('''
      • Adicionar Contato
''')
        try:
            nome = input("Nome: ")
            numero = int(input("Numero: "))
            try:
                dados = f"{nome} - {numero}\n"
                with open("agenda.txt", "a") as agenda:
                    agenda.write(dados)
                break
            except:
                print("Ocorreu um erro, cancelando operação")
        except:
            print("Ocorreu um erro, cancelando operação")
            input("Aperte enter para voltar ")
            limpar_tela()
            break

def listarcontatos():
    try:
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.read()
            limpar_tela()
            print(f"• Seus contatos\n{contatos}")
            input("Aperte enter para voltar ")
            limpar_tela()
    except:
        print("Ocorreu um erro, cancelando operação")
        input("Aperte enter para voltar ")
        limpar_tela()
           
def editarcontato():
        try:
            with open("agenda.txt", "r") as agenda:
                contatos = agenda.read()
                print(contatos)
            
            with open('agenda.txt', 'r') as agenda:
                linhas = agenda.readlines()
            
            numero_linha = int(input("Digite a linha que deseja alterar: "))
            
            if numero_linha > 0 and numero_linha <= len(linhas):
                nome_edit = input("Digite o nome: ")
                numero_edit = int(input("Digite o numero: "))               
               
                linhas[numero_linha - 1] = f"{nome_edit} - {numero_edit}\n"

                
                with open('agenda.txt', 'w') as agenda:
                    agenda.writelines(linhas)
        except:
            print("Ocorreu um erro, cancelando operação")
            input("Aperte enter para voltar ")
            limpar_tela()
            
def excluircontato():
    try:
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.read()
            print(contatos)
            
        with open('agenda.txt', 'r') as agenda:
            linhas = agenda.readlines()
            
        numero_linha = int(input("Digite a linha que deseja exluir: "))
            
        if numero_linha > 0 and numero_linha <= len(linhas):
            del linhas[numero_linha - 1]
 
        with open('agenda.txt', 'w') as agenda:
            agenda.writelines(linhas)
    except:
        print("Ocorreu um erro, cancelando operação")
        input("Aperte enter para voltar ")
        limpar_tela()

def ligar():
    try:
        num = int(input("Disque o telefone: "))
        for i in range(1,4,1):
            print(f"Ligando para {num}")
            sleep(2)
        print(f"{num} Não atendeu a chamada")
        input("Aperte enter para voltar ")
        limpar_tela()

    except:
        print("Ocorreu um erro, cancelando operação")
        input("Aperte enter para voltar ")
        limpar_tela()
 
def limpar_tela(): #Limpa o terminal
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

menu()