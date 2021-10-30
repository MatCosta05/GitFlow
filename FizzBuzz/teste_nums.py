"""
Funções utilizadas para TDD do app FizzBuzz
"""

from validnum import nunnatural, multipls


class TesteNums:
    """
    Criando a classe de TDD
    """
    def setup(self):
        """
        Inicio da classe TesteNums
        """


    def teste_nunnatural(self):
        """
        Testa se a entrada a respeito de número natural está funcionando
        """
        resultado = nunnatural(-2)
        resultado1 = nunnatural(0)
        resultado2 = nunnatural(3)
        resultado3 = nunnatural(5.4)

        assert resultado == "Não é um número natura"
        assert resultado1 == "É um número natural"
        assert resultado2 == "É um número natural"
        assert resultado3 == "Não é um número natural"

    def teste_multipls(self):
        """
        Testa se a entrada a respeito de número é multiplo de 3 ou 7
        """
        resultado = multipls(3)
        resultado1 = multipls(7)
        resultado2 = multipls(21)
        resultado3 = multipls(10)

        assert resultado == "Fizz!"
        assert resultado1 == "Buzz!"
        assert resultado2 == "FizzBuzz!"
        assert resultado3 == "Miss!"
