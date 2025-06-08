import csv
from typing import List, Dict, Optional

BANCODEDADOS_CSV = 'DadosLivros.csv'
CAMPOS = ['id', 'titulo', 'autor', 'ano']

def carregar_livros() -> List[Dict[str, str]]:
    try:
        with open(BANCODEDADOS_CSV, mode='r', newline='', encoding='utf-8') as f:
            return [dict(zip(CAMPOS, row)) for row in csv.reader(f)]
    except FileNotFoundError:
        return []

def salvar_livros(livros: List[Dict[str, str]]):
    with open(BANCODEDADOS_CSV, mode='w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        for livro in livros:
            escritor.writerow([livro[campo] for campo in CAMPOS])
