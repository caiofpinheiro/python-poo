from abc import ABC, abstractmethod
import os

os.system("cls || clear")

class Funcionario(ABC):

    # Construtor.

    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario
    
    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.2 # 20%
        salario_final = self.salario * BONIFICACAO
        return salario_final

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh
    def calcular_salario(self) -> float:
        BONIFICACAO = 2.5 # 150%
        salario_final = self.salario * BONIFICACAO
        return salario_final


# Instanciar classes.

#funcionario1 = Funcionario("Jose", 15, 1500.0)
#print(f"Nome: {funcionario1.nome}")
gerente1 = Gerente("Caio", 18, 1000.00)
print(f"Nome: {gerente1.nome}")
print(f"Salario: {gerente1.calcular_salario()}")

motoboy1 = Motoboy("José", 23, 1000.00, "000-1")
print(f"Nome: {motoboy1.nome}")
print(f"Salario: {motoboy1.calcular_salario()}")

