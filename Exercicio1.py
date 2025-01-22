def registrar_pedido (cliente, endereco=None, *args, **kwargs):
    """
    Registra um pedido em uma lanchonete.
    Args: 
    Cliente (str): Nome do cliente (obrigatório).
    Endereco (str, opcional): Endereço de entrega, padrão None.
    *args: Itens do pedido.
    **kargs: Detalhes adicionais do pedido, como bebidas e observações.
    Returns:
        dict: Dicionario que contém todas as informações do pedido.
    """
    pedido = {
            "Cliente": cliente,
            "Endereço": endereco,
            "Itens": args,
            "Detalhes_Adicionais": kwargs
            }
    return pedido

cliente = input ("Digite o nome do cliente: ")

endereco = input ("Digite o endereço (ou pressione Enter para deixar em branco): ") or None

itens = []
while True:
    item = input("Digite um item do pedido (ou pressione Enter para finalizar): ")
    if not item:
        break
    itens.append(item)

detalhes = {}
while True:
    chave = input("Digite o nome de um detalhe adicional: (ex: bebida, observações) ou pressione Enter para finalizar: ")
    if not chave:
        break
    valor = input(f"Digite o valor para '{chave}': ")
    detalhes[chave] = valor

pedido = registrar_pedido(cliente, endereco, *itens, **detalhes)

print("\nPedido registrado:")
for chave, valor in pedido.items():
    print(f"{chave}: {valor}")