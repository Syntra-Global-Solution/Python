#  Funções básicas
def continuar() -> None:
    input("Pressione ENTER para continuar ...")

def valueerror() -> None:
    print(f"""
{30 * "-"}
Digite um número!
{30 * "-"}
""")

def except_geral() -> None:
    print(f"""
{30 * "-"}
Ocorreu um erro! Tente novamente
{30 * "-"}
""")

# Menus e Submenus

def exibir_menu() -> None:
    print(f"""
{30 * "="}
    MENU PRINCIPAL
{30 * "="}
0 - SAIR
1 - Trajetos
2 - Informações de linhas
3 - Relato de ocorrências
    """)

def submenu_trajetos() -> None:
    print(f"""
{10 * "="} TRAJETOS {10 * "="}\n
0 - Voltar ao menu principal
1 - Consultar trajetos
2 - Trajetos favoritos
    """)

# Solicitação de informações

def solicitar_local(mensagem: str) -> str:
    while True:
        local = input(mensagem).strip()

        if not local:
            print("O local não pode estar vazio.")
        elif local.isdigit():
            print("Digite um endereço ou nome de local válido.")
        elif len(local) < 3:
            print("O local deve conter pelo menos 3 caracteres.")
        else:
            return local
