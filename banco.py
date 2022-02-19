import py_compile


class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0 

    def ver_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):    
        self.__saldo -= valor


if __name__ == '__main__':
    c1 = Conta(1, 'Everton')