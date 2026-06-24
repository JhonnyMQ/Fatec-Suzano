nome: str
idade: int
cor_fav: str

nome=input("Qual seu nome:" )
idade=input("Qual sua idade:" )
cor_fav=input("Qual sua cor favorita:" )

if (idade >= "20") and cor_fav == "azul":
    print(f"seja bem vindo {nome}")
else:
    print("infelizmente não entrarais")