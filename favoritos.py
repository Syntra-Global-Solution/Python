import json


def perguntar_favorito() -> bool | None:
    while True:
        favorito = input("\nDeseja favoritar trajeto? (S / N)")

        match favorito:
            case "S" | "s":
                return True
            case "N" | "n":
                return False
            case _:
                print("Valor inválido!")


def salvar_favorito(origem: str, destino: str, trajeto_escolhido: dict) -> None:
    nome = input("\nNome do trajeto: ")

    caminho = []
    for etapa in trajeto_escolhido["legs"]:

        if etapa["mode"] == "REGIONAL_RAIL":

            trecho = {
                "transporte": "Trem",
                "linha": etapa["routeShortName"],
                "embarque": etapa["from"]["name"],
                "desembarque": etapa["to"]["name"],
                "sentido": etapa["headsign"]
            }
        elif etapa["mode"] == "SUBWAY":
            trecho = {
                "transporte": "Metrô",
                "linha": etapa["routeShortName"],
                "embarque": etapa["from"]["name"],
                "desembarque": etapa["to"]["name"],
                "sentido": etapa["headsign"]
            }
        elif  etapa["mode"] == "WALK":
            local = etapa["to"]["name"]

            if local == "END":
                local = destino

            trecho = {
                "transporte": "Caminhada",
                "distancia": etapa["distance"],
                "destino" : local
            }
        else:
            continue
        caminho.append(trecho)
    trajeto = {
        nome : {
        "origem" : origem,
        "destino" : destino,
        "caminho" : caminho
        }
    }
    try:
        with open("favoritos.json", "r", encoding="utf-8") as arquivo:
            trajetos_fav = json.load(arquivo)
    except FileNotFoundError:
        trajetos_fav = []

    trajetos_fav.append(trajeto)

    with open("favoritos.json", "w", encoding="utf-8") as arquivo:
        json.dump(trajetos_fav, arquivo, indent=4)


def exibir_favoritos() -> None:
    with open("favoritos.json", "r", encoding="utf-8") as arquivo:
        favoritos = json.load(arquivo)

    print("\nFAVORITADOS")
    print(50 * "-")
    for favorito in favoritos:
        for nome in favorito:
            print("Nome: ", nome)
            print("\tOrigem: ", favorito[nome]["origem"])
            print("\tDestino: ", favorito[nome]["destino"])
            print("\tCaminho:")
            numero = 1

            for trecho in favorito[nome]["caminho"]:

                if trecho["transporte"] == "Caminhada":
                    print(f"\t\t{numero}- Caminhar {trecho["distancia"]} metros até {trecho['destino']}")

                elif trecho["transporte"] == "Trem":
                    print(f"""\t\t{numero}- Pegar o trem na estação {trecho["embarque"]} 
                    pela linha {trecho["linha"]}
                    sentido {trecho["sentido"]}
                    Desembarcar na estação {trecho["desembarque"]}""")

                elif trecho["transporte"] == "Metrô":
                    print(f"""\t\t{numero}- Pegar o metrô na estação {trecho["embarque"]}
                    pela linha {trecho["linha"]} sentido {trecho["sentido"]}
                    Desembarcar na estação {trecho["desembarque"]}""")

                numero = numero + 1
            print(50 * "-")