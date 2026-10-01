"""Regras do cardápio: preços em centavos para evitar arredondamento."""


def total(preco_centavos, quantidade):
    if preco_centavos < 0 or quantidade < 0:
        raise ValueError("Preço e quantidade devem ser não negativos")
    return preco_centavos * quantidade
