from subalgoritmos import solicitar_local
from integracoes import buscar_local_api, calcular_trajeto_api
from favoritos import perguntar_favorito, salvar_favorito


def consultar_trajetos():
    print("\n===== CONSULTAR TRAJETOS =====")

    origem = solicitar_local("Origem: ")
    while True:
        destino = solicitar_local("Destino: ")

        if destino.lower() == origem.lower():
            print("A origem e o destino devem ser diferentes")
        else:
            break

    resultado_origem = buscar_local_api(origem)
    resultado_destino = buscar_local_api(destino)

    if resultado_origem is None or resultado_destino is None:
        print("\nNão foi possível consultar os locais.")
    elif not resultado_origem:
        print("\nOrigem não encontrada.")
    elif not resultado_destino:
        print("\nDestino não encontrado.")
    else:
        print("\nOrigem e destino encontrados!")
        print(f"""
\nOrigem: {origem}
Destino: {destino}
        """)

    if resultado_origem and resultado_destino:
        local_origem = resultado_origem[0]
        local_destino = resultado_destino[0]

        trajetos = calcular_trajeto_api(local_origem, local_destino)
        if trajetos is None:
            print("\nNão foi possível consultar os trajetos.")
        else:
            print("\nConsulta realizada!\n")

            trajeto_escolhido = escolher_trajeto(trajetos)
            exibir_trajeto(trajeto_escolhido, destino)

            if perguntar_favorito():
                salvar_favorito(origem, destino, trajeto_escolhido)


def escolher_trajeto(trajetos: list) -> dict:
    numero = 1

    for trajeto in trajetos["itineraries"]:
        duracao = trajeto["duration"]
        horas = duracao // 3600
        minutos = (duracao % 3600) // 60
        print(f"""{numero} - Duração: {horas}h {minutos}min | Baldeações: {trajeto["transfers"]}""")

        numero = numero + 1

    trajeto_escolhido = int(input("Escolha um trajeto: "))
    indice = trajeto_escolhido - 1
    return trajetos["itineraries"][indice]


def exibir_trajeto(trajeto: dict, destino: str) -> None:
    print("\n======== PASSO A PASSO ========")

    numero = 1

    for etapa in trajeto["legs"]:

        if etapa["mode"] == "WALK":
            distancia = etapa["distance"]

            if etapa["to"]["name"] == "END":
                print(numero, "- Caminhar", distancia, "metros até", destino)
            else:
                print(numero, "- Caminhar", distancia, "metros até", etapa["to"]["name"])

        elif etapa["mode"] == "REGIONAL_RAIL":
            print(numero, "- Pegar o trem na estação",
            etapa["from"]["name"],
            "pela linha",
            etapa["routeShortName"],
            "sentido",
            etapa["headsign"])
            print("Desembarcar na estação", etapa["to"]["name"])

        elif etapa["mode"] == "SUBWAY":
            print(numero, "- Pegar o metrô na estação",
            etapa["from"]["name"],
            "pela linha",
            etapa["routeShortName"],
            "sentido",
            etapa["headsign"])
            print("Desembarcar na estação", etapa["to"]["name"])

        numero = numero + 1