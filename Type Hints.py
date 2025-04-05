# Exercício 1: Funções com Type Hints básicos
# Crie uma função que receba dois números e retorne sua soma, usando type hints adequados.

def soma(a: float, b: float) -> float:
    return a + b
x=2.2
h=3
print(soma(x,h))

# Exercício 2: Usando tipos de coleções
# Crie uma função que receba uma lista de strings e retorne a string mais longa.

from typing import List
def string_mais_longa(strings: list[str]) -> str:
    if not strings:
        return ""
    return max(strings, key=len)