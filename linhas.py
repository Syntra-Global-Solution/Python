from integracoes import buscar_partidas_estacao, buscar_estacao_api, buscar_status_linhas
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import os

#  Submenu das linhas
def sub_linhas() -> None:
    print(f"""
{10 * "="} INFORMAÇÕES DE LINHAS {10 * "="}

1 - Metrô
2 - Trem
3 - Monotrilho
    """)

def menu_metro() -> None:
    print(f"""
{10 * "="} METRÔ {10 * "="}
1 - Linha 1-Azul
2 - Linha 2-Verde
3 - Linha 3-Vermelha
4 - Linha 4-Amarela
5 - Linha 5-Lilás
6 - Linha 6-Laranja
        """)

def menu_trem() -> None:
    print(f"""
{10 * "="} TREM {10 * "="}
7 - Linha 7-Rubi
8 - Linha 8-Diamante
9 - Linha 9-Esmeralda
10 - Linha 10-Turquesa
11 - Linha 11-Coral
12 - Linha 12-Safira
13 - Linha 13-Jade
        """)

def menu_monotrilho() -> None:
    print(f"""
{10 * "="} MONOTRILHO {10 * "="}
15 - Linha 15-Prata
17 - Linha 17-Ouro
            """)

def consultar_informacoes(numero_linha: int) -> None:
    nome_estacao = input("Digite sua estação: ").strip()

    resultados = buscar_estacao_api(nome_estacao)

    if not resultados:
        print("Estação não encontrada.")
        return

    estacao_escolhida = None
    dados = None

    for resultado in resultados:

        if resultado.get("type") != "STOP":
            continue

        nome_api = resultado["name"].split(",")[0].strip()

        if nome_api.lower() != nome_estacao.lower():
            continue

        codigo_estacao = resultado["id"]
        consulta = buscar_partidas_estacao(codigo_estacao)

        if consulta is None:
            continue

        for partida in consulta["stopTimes"]:

            linha_api = partida["routeShortName"]

            if str(numero_linha) == linha_api.split("L")[-1]:
                estacao_escolhida = resultado
                dados = consulta
                break

        if estacao_escolhida is not None:
            break

    if estacao_escolhida is None:
        print("\nHorários indisponíveis na fonte consultada.")
        exibir_status_linha(numero_linha)
        return

    nome_limpo = estacao_escolhida["name"].split(",")[0].strip()
    print("\nEstação encontrada:", nome_limpo)

    sentido = escolher_sentido(dados, numero_linha)

    if sentido is not None:
        print("\nSentido selecionado:", sentido)

        exibir_partidas(dados, numero_linha, sentido)
        exibir_status_linha(numero_linha)

def escolher_sentido(dados: dict, numero_linha: int) -> str | None:
    sentidos = []

    for partida in dados["stopTimes"]:
        linha_api = partida["routeShortName"]

        if str(numero_linha) == linha_api.split("L")[-1]:
            sentido = partida["headsign"]

            if sentido not in sentidos:
                sentidos.append(sentido)

    if not sentidos:
        print("Nenhum sentido encontrado para essa linha.")
        return None

    print("\n========== SENTIDOS DISPONÍVEIS ==========")

    for numero, sentido in enumerate(sentidos, start=1):
        print(numero, "-", sentido)

    while True:
        try:
            escolha = int(input("Escolha o sentido: "))

            if 1 <= escolha <= len(sentidos):
                return sentidos[escolha - 1]

            print("Escolha uma opção válida.")

        except ValueError:
            print("Digite um número válido.")

def exibir_partidas(dados: dict, numero_linha: int, sentido: str) -> None:
    partidas = []
    agora = datetime.now(timezone.utc)

    for partida in dados["stopTimes"]:
        linha_api = partida["routeShortName"]

        if str(numero_linha) != linha_api.split("L")[-1]:
            continue

        if partida["headsign"] != sentido:
            continue

        if partida.get("cancelled") or partida.get("tripCancelled"):
            continue

        horario_api = partida["place"]["departure"]
        horario = datetime.fromisoformat(horario_api)

        if horario > agora:
            partidas.append((horario, partida["realTime"]))

    partidas.sort()

    print(f"\n{10 * "="} PRÓXIMAS PARTIDAS {10 * "="}")

    if not partidas:
        print("Nenhuma partida encontrada.")
        return

    for horario, tempo_real in partidas[:3]:
        horario_sp = horario.astimezone(timezone(timedelta(hours=-3)))
        minutos = max(0, int((horario - agora).total_seconds() / 60))

        print("\nHorário:", horario_sp.strftime("%H:%M"))
        print("Faltam aproximadamente:", minutos, "minutos")

def exibir_status_linha(numero_linha: int) -> None:
    dados_status = buscar_status_linhas()

    if dados_status is None:
        print("Não foi possível consultar o status.")
        return

    for linha in dados_status['lines']:
        if linha["linha"] == numero_linha:
            print(f"\n{10 * "="} STATUS DA LINHA {10 * "="}")
            print("\nLinha:", linha["rotulo"])
            print("Status:", linha["status"])

            return
    print("Não foram encontradas informações dessa linha.")