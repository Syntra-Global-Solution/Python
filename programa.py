import os
os.system("cls")

import subalgoritmos as sub
import trajetos
import favoritos
import linhas

while True:
    try:
        sub.exibir_menu()
        escolha = int(input("Escolha uma opção: "))

        match escolha:
            case 0:
                break

            case 1:
                # Trajetos
                try:
                    sub.submenu_trajetos()
                    opcao = int(input("Escolha uma opção: "))

                    match opcao:
                        case 0:
                            continue

                        case 1:
                            # Consultar trajetos
                            trajetos.consultar_trajetos()
                            sub.continuar()

                        case 2:
                            # Trajetos favoritos
                            favoritos.exibir_favoritos()
                            sub.continuar()

                except ValueError:
                    sub.valueerror()
                    sub.continuar()
                except:
                    sub.except_geral()
                    sub.continuar()
            case 2:
                # Informações de linhas
                try:
                    linhas.sub_linhas()
                    escolha_linhas = int(input("Escolha: "))

                    match escolha_linhas:
                        case 1:
                            linhas.menu_metro()

                            try:
                                escolha_metro = int(input("Escolha a linha: "))
                                linhas.consultar_informacoes(escolha_metro)
                                sub.continuar()
                            except ValueError:
                                sub.valueerror()
                                sub.continuar()
                            except:
                                sub.except_geral()
                                sub.continuar()
                        case 2:
                            linhas.menu_trem()

                            try:
                                escolha_trem = int(input("Escolha: "))
                                if escolha_trem != 0 and 7 <= escolha_trem <= 13:
                                    linhas.consultar_informacoes(escolha_trem)
                                    sub.continuar()
                            except ValueError:
                                sub.valueerror()
                                sub.continuar()
                            except:
                                sub.except_geral()
                                sub.continuar()
                        case 3:
                            linhas.menu_monotrilho()
                            try:
                                escolha_monotrilho = int(input("Escolha: "))
                                if escolha_monotrilho in (15, 17):
                                    linhas.consultar_informacoes(escolha_monotrilho)
                                    sub.continuar()
                            except ValueError:
                                sub.valueerror()
                                sub.continuar()
                            except:
                                sub.except_geral()
                                sub.continuar()
                        case _:
                            print("Digite um valor válido!")
                            sub.continuar()

                except ValueError:
                    sub.valueerror()
                    sub.continuar()
                except:
                    sub.except_geral()
                    sub.continuar()
            case 3:
                # Relato de ocorrências
                pass
                sub.continuar()
    except ValueError:
        sub.valueerror()
        sub.continuar()

    except:
        sub.except_geral()
        sub.continuar()