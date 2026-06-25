# Você deve criar um projeto que permita inserir 10 nomes,
# cada nome ao ser imputado, deve ser salvo em um arquivo .txt,
# ao inserir o 11º deve retornar no console “banco de dados cheio”
# no projeto deve conseguir listar as posições dos nomes e o nome que está na posição,
# alterar um nome pela posição e deletar um nome pela posição.
# Se tiver 10 itens e deletar um ele pode voltar a inserir um novo nome.
# Se o usuário tentar deletar ou alterar um nome que não tem na posição, deve retornar “item não existe”.
# 1 – inserir
# 2 - consultar
# 3 – Alterar
# 4 – Deletar

# Obs: Obrigatório o uso de funções para cada ação
# FUNÇÕES
import os
def inserir(nome:str):
    with open("ListaNomes.txt", "a") as arquivo:
        arquivo.write(f"{nome}\n")
def deletar():
    with open("ListaNomes.txt", "w") as f:
        pass
def consultar(n: int, nome:str):
    n -= 1
    if lista_Nomes[n] == nome:
        print (f"nome {nome}, na posição {n+1} foi encontrado.")
    else:
        print("nome não encontrado.")
def comparar(n: int, nome:str):
    n -= 1
    if lista_Nomes[n] == nome:
        return True
    else:
        return False
def listar():
    with open("ListaNomes.txt", "r", encoding='utf-8') as arquivo:
        for i, nome in enumerate(arquivo.read().splitlines()[:10]):
            print(f"{i+1} - {nome}")

# VARIAVEIS
if not os.path.exists("ListaNomes.txt"):
    with open("ListaNomes.txt", "w") as arquivo:
        pass
with open("ListaNomes.txt", "r", encoding='utf-8') as arquivo:
    lista_Nomes = arquivo.read().splitlines()

exit = False

while exit == False:
    digit=int(input("O que deseja fazer:\n1_Inserir\n2_Consultar\n3_Alterar\n4_Deletar\n5_Ver Lista\n6_Exit\nOpção:"))
    match digit:
        case 1:
            if "" in lista_Nomes or len(lista_Nomes) < 10:
                i=int(input("em qual posição tu quer inserir?"))
                i -= 1
                if 0 <= i < 10:
                    if i >= len(lista_Nomes):
                        while len(lista_Nomes) <= i:
                            lista_Nomes.append("")
                    if lista_Nomes[i] == "":
                        nome = str(input("Qual nome deseja inserir?"))
                        lista_Nomes[i] = nome
                        deletar()
                        for nome in lista_Nomes:
                            inserir(nome)
                    else:
                        print("espaco já ocupado, tente outra posição.")
                    
                else:
                    print("limite é de 10 nomes, escolha uma posição entre 1 e 10.")
            else:
                print("banco de dados cheio")
        case 2:
            n=int(input("em qual posição tu quer consultar?"))
            Nome=str(input("Qual o nome deseja consultar?"))
            consultar(n, Nome)
            
        case 3:
            i=int(input("qual posição tu quer substituir?"))
            i -= 1
            nome = str(input("Qual nome deseja substituir?"))
            if comparar(i+1, nome) == True:
                nome_s = str(input("Qual nome deseja inserir?"))
                lista_Nomes[i] = nome_s
            else:
                print("item não existe")
            deletar()
            for nome in lista_Nomes:
                inserir(nome)
            print("nome substituido com sucesso")
            
        case 4:
            i=int(input("Qual posição tu quer deletar?"))
            i -= 1
            nome = str(input("Qual nome deseja deletar?"))
            if comparar(i+1, nome) == True:
                lista_Nomes[i] = ""
            else:
                print("item não existe")
            deletar()
            for nome in lista_Nomes:
                inserir(nome)
            print("nome deletado com sucesso na posição", i+1)
        case 5:
            if len(lista_Nomes) != 0:
                listar()
            else:
                print("banco de dados vazio")
            print(len(lista_Nomes))
        case 6:
            print("finalizando")
            exit = True
        case _:
            print("Valor invalido, tente novamente")