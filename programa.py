import os
os.system("cls")

import subalgoritmos as sub
import trajetos

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
                            pass

                except ValueError:
                    sub.valueerror()
                    sub.continuar()
                except:
                    sub.except_geral()
                    sub.continuar()
            case 2:
                # Informações de linhas
                pass
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