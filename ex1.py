
n = int(input("Digite o número de Pokémon: "))


pokemons = {}

for i in range(n):
    nome = input("Nome do Pokémon: ")
    tipo = input("Tipo do Pokémon: ")
    ataque = int(input("Valor de ataque do Pokémon: "))
    
    if tipo == "Fogo":
        pokemons[nome] = ataque

maior_ataque = max(pokemons, key=pokemons.get)


print("O Pokémon do tipo Fogo com maior ataque é:", maior_ataque)