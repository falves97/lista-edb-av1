class CpfTad:
    cpf = []

    def lerCpf(self, cpfString):
        if len(cpfString) != 11:
            return False

        for i in range(11):
            self.cpf.append(int(cpfString[i]))

    def isCpfValido(self):
        firstDigit = 0
        secondDigit = 0
        if len(self.cpf) != 11:
            return False

        sm = 0
        for i in range(10, 1, -1):
            index = 10 - i
            sm += self.cpf[index] * i

        sm = 11 - (sm % 11)
        if sm == 11 or sm == 10:
            firstDigit = 0
        else:
            firstDigit = sm

        sm = 0
        for i in range(11, 1, -1):
            index = 11 - i
            sm += self.cpf[index] * i

        sm = 11 - (sm % 11)
        if sm == 11 or sm == 10:
            secondDigit = 0
        else:
            secondDigit = sm

        return firstDigit == self.cpf[9] and secondDigit == self.cpf[10]
