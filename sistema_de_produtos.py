def ler_produtos():
    produtos = []
    while True:
        print("Digite os dados do produto e pressione Enter. Pressione apenas Enter para sair.")
        entrada = input().strip()
        if not entrada:
            break
        codigo, descricao, quantidade, preco = entrada.split('#')
        produto = {'codigo': codigo, 'descricao': descricao, 'quantidade': int(quantidade), 'preco': float(preco)}
        produtos.append(produto)
    return produtos

def buscar_produto(codigo, produtos):
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto
    return None

def main():
    produtos = ler_produtos()
    while True:
        codigo = input("Digite o código do produto (ou nada para sair): ").strip()
        if not codigo:
            break
        produto = buscar_produto(codigo, produtos)
        if produto is None:
            print(f"Produto com código {codigo} não encontrado.")
        else:
            print(f"Produto Localizado: ('{produto['codigo']}', '{produto['descricao']}', '{produto['quantidade']}', '{produto['preco']:.2f}') ")
    print("Obrigado por utilizar nosso sistema!!!")


main()