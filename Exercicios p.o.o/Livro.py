import os

os.system("cls || clear")


class Livro:
    def __init__(self, titulo: str, autor: str, numPag: int, preco: float) -> None:
        self.titulo = titulo
        self.autor = autor
        self.numPag = numPag
        self.preco = preco

    def exibir_dados(self) -> str:
        return f"Titulo: {self.titulo} \nAutor: {self.autor} \nNumero de Paginas: {self.numPag} \nPreço: {self.preco}"
    
livro = Livro("Bosta", "Merda", 12312, 45)
livro2 = Livro("seila", "asda", 1212, 23)
print(livro.exibir_dados())
print(livro2.exibir_dados())