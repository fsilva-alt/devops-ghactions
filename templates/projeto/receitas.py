"""Livro de receitas: lê as receitas da pasta receitas/ e faz as contas da cozinha."""

from pathlib import Path

PASTA = Path(__file__).parent / "receitas"


def quantidade_para(gramas_por_receita, receitas):
    """Gramas de um ingrediente para preparar várias receitas de uma vez."""
    if gramas_por_receita < 0 or receitas < 0:
        raise ValueError("A quantidade e o número de receitas não podem ser negativos.")
    return gramas_por_receita * receitas


def listar(pasta=PASTA):
    """Nome, rendimento e arquivo de cada receita, na ordem dos arquivos."""
    receitas = []
    for arquivo in sorted(pasta.glob("*.md")):
        linhas = arquivo.read_text(encoding="utf-8").splitlines()
        nome = linhas[0].removeprefix("#").strip() if linhas else arquivo.stem
        rende = next((l.removeprefix("Rende:").strip() for l in linhas if l.startswith("Rende:")), "")
        receitas.append({"nome": nome, "rende": rende, "arquivo": arquivo})
    return receitas


if __name__ == "__main__":
    print("Livro de receitas")
    print("=================")
    for receita in listar():
        print(f"- {receita['nome']} (rende {receita['rende']})")
