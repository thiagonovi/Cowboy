prompt = "> "

print("Qual o seu nome, cowboy?")
nome = input(prompt)

def passado_menu():
    print(f"""Qual o seu passado, {nome}?
    1. Um fazendeiro pobre, buscando dinheiro para salvar sua fazenda.
    2. Um pistoleiro, procurando alguém que precise de seus serviços.
    3. Um delegado, em busca de um criminoso perigoso que acaba de fugir da prisão.""")
    passado = input(prompt)


    if passado == "1":
        arma, balas, carreira = "arco e flecha", 30, "fazendeiro"
        conclusao_passado(arma, balas, carreira)
    elif passado == "2":
        arma, balas, carreira = "colt", 45, "pistoleiro"
        conclusao_passado(arma, balas, carreira)
    elif passado == "3":
        arma, balas, carreira = "winchester", 40, "delegado"
        conclusao_passado(arma, balas, carreira)
    else:
        print("Escolha um passado válido! \n")
        passado_menu()
    return arma, balas, carreira

def conclusao_passado(arma, balas, carreira):
    print(f"Você é {nome}, um {carreira}. Seu equipamento é um {arma} com {balas} munições.")
    print("Está satisfeito com seu passado? [Y/N]")
    resposta_passado = input(prompt)
    if (resposta_passado == 'N') or (resposta_passado == 'n'):
        passado_menu()
    elif (resposta_passado != 'Y') and (resposta_passado != 'y'):
        print("Resposta inválida!\n")
        conclusao_passado(arma, balas, carreira)


arma, balas, carreira = passado_menu()


print(f"\nSua aventura está prestes a começar!")
