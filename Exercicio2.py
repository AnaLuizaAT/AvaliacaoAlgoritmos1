def criar_perfil (usuario, email=None, *args, **kwargs):
    """
    Registra um perfil de usuário.
    Args: 
    Usuário (str): Nome do usuário (obrigatório).
    E-mail (str, opcional): Endereço de email, padrão None.
    *args: Habilidades.
    **kargs: Detalhes adicionais do usuário.
    Returns:
        dict: Dicionario que contém todas as informações do perfil.
    """
    perfil = {
            "Usuário": usuario,
            "E-mail": email,
            "Habilidades": args,
            "Detalhes_Adicionais": kwargs
            }
    return perfil

usuario = input ("Digite o nome do usuário: ")

email = input ("Digite o e-mail (ou pressione Enter para deixar em branco): ") or None

habilidades = []
while True:
    habilidade = input("Digite uma habilidade do usuário (ou pressione Enter para finalizar): ")
    if not habilidade:
        break
    habilidades.append(habilidade)

detalhes = {}
while True:
    chave = input("Digite o nome de um detalhe adicional (ou pressione Enter para finalizar): ")
    if not chave:
        break
    valor = input(f"Digite o valor para '{chave}': ")
    detalhes[chave] = valor

perfil = criar_perfil(usuario, email, *habilidades, **detalhes)

print("\nUsuário registrado: ")
for chave, valor in perfil.items():
    print(f"{chave}: {valor}")