import subalgoritmos as sub
import json
from datetime import datetime


def informar_estacao() -> str:
    estacao = input("Informe a estação: ")
    return estacao


def exibir_menu_ocorrencias() -> None:
    print(f"""
{10 * "="} RELATO DE OCORRÊNCIAS {10 * "="}

1 - Informar ocorrência
2 - Consultar ocorrências
    """)


def menu_informar() -> None:
    print(f"""
Selecione o transporte:

1 - Metrô
2 - Trem
3 - Monotrilho
    """)


def menu_trem() -> None:
    print(f"""
{10 * "="} TREM {10 * "="}

7  - Linha 7-Rubi
8  - Linha 8-Diamante
9  - Linha 9-Esmeralda
10 - Linha 10-Turquesa
11 - Linha 11-Coral
12 - Linha 12-Safira
13 - Linha 13-Jade
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


def menu_monotrilho() -> None:
    print(f"""
{10 * "="} MONOTRILHO {10 * "="}

15 - Linha 15-Prata
17 - Linha 17-Ouro
    """)


def opcao_trem() -> None:
    menu_trem()

    try:
        escolha = int(input("Escolha: "))
        match escolha:
            case 7 | 8 | 9 | 10 | 11 | 12 | 13:
                estacao = informar_estacao()
                ocorrencia = input("Descreva a ocorrência: ").strip()

                if estacao and ocorrencia:
                    salvar_ocorrencia(escolha, estacao, ocorrencia)
                else:
                    print("Ocorrência não registrada. Preencha todos os campos.")
            case _:
                print("Opção inválida!")
    except ValueError:
        sub.valueerror()
    except:
        sub.except_geral()


def opcao_metro() -> None:
    menu_metro()

    try:
        escolha = int(input("Escolha: "))
        match escolha:
            case 1 | 2 | 3 | 4 | 5 | 6:
                estacao = informar_estacao()
                ocorrencia = input("Descreva a ocorrência: ").strip()

                if estacao and ocorrencia:
                    salvar_ocorrencia(escolha, estacao, ocorrencia)
                else:
                    print("Ocorrência não registrada. Preencha todos os campos.")
            case _:
                print("Opção inválida!")
    except ValueError:
        sub.valueerror()
    except:
        sub.except_geral()


def opcao_monotrilho() -> None:
    menu_monotrilho()

    try:
        escolha = int(input("Escolha: "))
        match escolha:
            case 15 | 17:
                estacao = informar_estacao()
                ocorrencia = input("Descreva a ocorrência: ").strip()

                if estacao and ocorrencia:
                    salvar_ocorrencia(escolha, estacao, ocorrencia)
                else:
                    print("Ocorrência não registrada. Preencha todos os campos.")
            case _:
                print("Opção inválida!")
    except ValueError:
        sub.valueerror()
    except:
        sub.except_geral()


def salvar_ocorrencia(linha: int, estacao: str, descricao: str) -> None:
    data_hora = datetime.now().strftime("%d/%m/%Y às %H:%M")

    nova_ocorrencia = {
        "linha": linha,
        "estacao": estacao,
        "descricao": descricao,
        "data_hora": data_hora
    }

    try:
        with open("ocorrencias.json", "r", encoding="utf-8") as arquivo:
            ocorrencias = json.load(arquivo)

    except FileNotFoundError:
        ocorrencias = []

    ocorrencias.append(nova_ocorrencia)

    with open("ocorrencias.json", "w", encoding="utf-8") as arquivo:
        json.dump(ocorrencias, arquivo, ensure_ascii=False, indent=4)

    print("Ocorrência registrada com sucesso!")


def listar_ocorrencias(numero_linha: int) -> None:
    try:
        with open("ocorrencias.json", "r", encoding="utf-8") as arquivo:
            ocorrencias = json.load(arquivo)

    except FileNotFoundError:
        print("Nenhuma ocorrência registrada.")
        return

    encontrou = False

    for ocorrencia in ocorrencias:
        if ocorrencia["linha"] == numero_linha:
            print("\nEstação:", ocorrencia["estacao"])
            print("Relato:", ocorrencia["descricao"])
            print("Registrado em:", ocorrencia.get("data_hora", "Não informado"))
            print("----------------------")
            encontrou = True

    if not encontrou:
        print("Nenhuma ocorrência encontrada para essa linha.")