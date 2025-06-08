from typing import Optional, List, Dict
import database

def inserir_livro(livro: Dict[str, str]):
    livros = database.carregar_livros()
    livros.append(livro)
    database.salvar_livros(livros)

def consultar_livros(filtro: Optional[Dict[str, str]] = None) -> List[Dict[str, str]]:
    livros = database.carregar_livros()
    if filtro:
        chave, valor = list(filtro.items())[0]
        return [
            livro for livro in livros
            if livro.get(chave, '').lower() == valor.lower()
        ]
    return livros

def atualizar_livro(id_livro: str, novos_dados: Dict[str, str]) -> bool:
    livros = database.carregar_livros()
    for livro in livros:
        if livro['id'] == id_livro:
            livro.update(novos_dados)
            database.salvar_livros(livros)
            return True
    return False

def deletar_livro(id_livro: str) -> bool:
    livros = database.carregar_livros()
    novos_livros = [livro for livro in livros if livro['id'] != id_livro]
    if len(novos_livros) == len(livros):
        return False
    database.salvar_livros(novos_livros)
    return True
