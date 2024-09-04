
n = int(input("Digite o número de pessoas: "))


pessoas = {}


for _ in range(n):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    idade = int(input("Idade: "))
    

    if cpf not in pessoas:
        pessoas[cpf] = {"nome": nome, "idade": idade}


print("\nLista de pessoas (sem repetições):")
for cpf, info in pessoas.items():
    print(f"Nome: {info['nome']}, CPF: {cpf}, Idade: {info['idade']}")