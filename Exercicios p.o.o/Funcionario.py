import os
from abc import ABC, abstractmethod
from enum import Enum

os.system("cls || clear")
class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    

class Funcionario:
    def __init__(self, id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
    
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nID: {self.id}"
                f"\nSalario: {self.salario}"
                f"\nSetor: {self.setor.value}"
                f"\nSexo: {self.sexo.value}"
                )
    
funcionario_1 = Funcionario(11,"Caio", 18,6000.0,Setor.MARKETING,Sexo.MASCULINO)

print(funcionario_1)

