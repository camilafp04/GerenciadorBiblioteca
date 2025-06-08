import backend

def input_opcao(mensagem: str, opcoes_validas: list[str]) -> str:
    while True:
        entrada = input(mensagem).strip().lower()
        if entrada in opcoes_validas:
            return entrada
        print("Entrada inválida!")

def menu():
    while True:
        print("\n====================================="
        "\nGerenciamento de livros na Biblioteca "
        "\n=====================================\n")
        print("1. Inserir livro")
        print("2. Consultar livros")
        print("3. Atualizar livro")
        print("4. Deletar livro")
        print("5. Listar todos os livros")
        print("6. Encerrar")
        escolha = input("\nEscolha uma das opções acima: ").strip()

        if escolha == '1':
            livro = {
                'id': input("Insira o ID: ").strip(),
                'titulo': input("Insira o Título: ").strip(),
                'autor': input("Insira o Autor: ").strip(),
                'ano': input("Insira o Ano: ").strip()
            }
            backend.inserir_livro(livro)
            print("\nLivro inserido com sucesso!")

        elif escolha == '2':
            while True:
                chave = input("\nDeseja buscar o livro por id, titulo ou autor?: ").strip().lower()
                if chave not in ['id', 'titulo', 'autor']:
                    print("\nEntrada inválida! Tente novamente.")
                    continue
                valor = input(f"Digite o {chave}: ").strip()
                resultados = backend.consultar_livros({chave: valor})
                if resultados:
                    for livro in resultados:
                        print(f"\n {livro}")
                    break
                else:
                    print("\nNenhum livro foi encontrado com estas informações.")

        elif escolha == '3':
            id_livro = input("\nInsira o id do livro que deseja atualizar: ").strip()
            campo = input_opcao("Deseja atualizar o titulo, autor ou ano?: ", ['titulo', 'autor', 'ano'])
            novo_valor = input(f"Novo valor para {campo}: ").strip()
            sucesso = backend.atualizar_livro(id_livro, {campo: novo_valor})
            print("\nLivro atualizado com sucesso!" if sucesso else "\nLivro não encontrado.")

        elif escolha == '4':
            id_livro = input("Insira o id do livro que deseja deletar: ").strip()
            sucesso = backend.deletar_livro(id_livro)
            print("\nLivro deletado!" if sucesso else "\nLivro não encontrado!")

        elif escolha == '5':
            livros = backend.consultar_livros()
            if livros:
                for livro in livros:
                    print(f"\n {livro}")
            else:
                print("\zNenhum livro foi cadastrado!")

        elif escolha == '6':
            print("Encerrando...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == '__main__':
    menu()
