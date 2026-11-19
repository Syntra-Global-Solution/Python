import os
os.system("cls")

import subalgoritmos as sub
import trajetos
import favoritos
import linhas
import ocorrencias


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
                ocorrencias.exibir_menu_ocorrencias()

                try:
                    opcao_ocorrencias = int(input("Escolha: "))

                    match opcao_ocorrencias:
                        case 1:
                            ocorrencias.menu_informar()

                            try:
                                opcao_ocorrencia = int(input("Escolha: "))

                                if opcao_ocorrencia == 1:
                                    ocorrencias.opcao_metro()

                                elif opcao_ocorrencia == 2:
                                    ocorrencias.opcao_trem()

                                elif opcao_ocorrencia == 3:
                                    ocorrencias.opcao_monotrilho()

                                else:
                                    print("Digite um valor válido!")

                            except ValueError:
                                sub.valueerror()
                            except:
                                sub.except_geral()

                        case 2:
                            ocorrencias.menu_informar()

                            try:
                                opcao_ocorrencia = int(input("Escolha: "))

                                if opcao_ocorrencia == 1:
                                    ocorrencias.menu_metro()

                                    try:
                                        escolha = int(input("Escolha: "))
                                        ocorrencias.listar_ocorrencias(escolha)

                                    except ValueError:
                                        sub.valueerror()
                                    except:
                                        sub.except_geral()

                                elif opcao_ocorrencia == 2:
                                    ocorrencias.menu_trem()

                                    try:
                                        escolha = int(input("Escolha: "))
                                        ocorrencias.listar_ocorrencias(escolha)

                                    except ValueError:
                                        sub.valueerror()
                                    except:
                                        sub.except_geral()

                                elif opcao_ocorrencia == 3:
                                    ocorrencias.menu_monotrilho()

                                    try:
                                        escolha = int(input("Escolha: "))
                                        ocorrencias.listar_ocorrencias(escolha)

                                    except ValueError:
                                        sub.valueerror()
                                    except:
                                        sub.except_geral()

                                else:
                                    print("Digite um valor válido!")

                            except ValueError:
                                sub.valueerror()
                            except:
                                sub.except_geral()

                        case _:
                            print("Opção inválida!")

                except ValueError:
                    sub.valueerror()
                except:
                    sub.except_geral()

                sub.continuar()

    except ValueError:
        sub.valueerror()
        sub.continuar()

    except:
        sub.except_geral()
        sub.continuar()
