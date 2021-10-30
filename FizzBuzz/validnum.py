"""
Função utilizadas pelo app FizzBuzz
"""
def nunnatural(auxnum):
    """
    Função utilizadas para definir se o número é natural
    """
    if auxnum >= 0:
        num = int(auxnum)
        mnum = auxnum * 10
        snum = num * 10
        if mnum == snum:
            print("É um número natural")
            return "É um número natural"
        else:
            print("Não é um número natural")
            return "Não é um número natural"
    else:
        print("Não é um número natural")
        return "Não é um número natural"

def multipls(auxnum):
    """
    Função utilizadas para ver se o número é multiplo de 3 ou 7
    """
    if auxnum%3 == 0 and auxnum%7 != 0:
        print("Fizz!")
        return "Fizz!"

    elif auxnum%3 != 0 and auxnum%7 == 0:
        print("Buzz!")
        return "Buzz!"

    elif auxnum%3 == 0 and auxnum%7 == 0:
        print("FizzBuzz!")
        return "FizzBuzz!"
    else:
        print("Miss!")
        return "Miss!"
