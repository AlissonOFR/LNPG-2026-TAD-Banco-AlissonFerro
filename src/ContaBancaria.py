class contaBancaria:
    def __init__(self, numero,titular,banco,saldo):
        self.numero = None
        self.saldo = None
        self.titular = titular
        self.banco = banco

        if numero is not None and numero > 0:
            self.numero = numero
        
        if saldo >= 0:
            self.saldo = saldo
        else:
            self.saldo = 0.0

        if banco is not None:
            self.banco = banco
        
        if titular is not None: 
            self.titular = titular

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor

    def saque(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def validar_conta(self):
        if self.bancosaldo > 0:
            return True
        else:
            return False
    def consultarSaldo(self):
        return self.saldo
        
    def getTitular(self):
        return self.titular
        
    def getBanco(self):
        return self.banco
        
    def estaAtiva(self):
        return self > 0
        
    def getNumero(self):
        return self.numero
