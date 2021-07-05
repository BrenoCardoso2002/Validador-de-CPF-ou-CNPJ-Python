import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QRadioButton, QLineEdit, QPushButton
from PyQt5 import QtGui


# Classe da janela
class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()

        # Dados da tela:
        self.topo = 250
        self.esquerda = 250
        self.largura = 300
        self.altura = 250
        self.titulo = 'Validador de CPF/CNPJ'
        self.setFixedSize(300, 250)
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        # Label Tipo que quer verificar:
        label1 = QLabel(self)
        label1.setText("O que você que validar?")
        label1.move(30, 10)
        label1.resize(450, 40)
        label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:black}')

        # RadioButton CPF
        self.RadioCPF = QRadioButton(self)
        self.RadioCPF.move(60, 40)
        self.RadioCPF.setText('CPF')
        self.RadioCPF.setStyleSheet('QRadioButton {font-size:20px;color:black}')
        self.RadioCPF.clicked.connect(self.ClickCPF)

        # RadioButton CNPJ
        self.RadioCNPJ = QRadioButton(self)
        self.RadioCNPJ.move(160, 40)
        self.RadioCNPJ.setText('CNPJ')
        self.RadioCNPJ.setStyleSheet('QRadioButton {font-size:20px;color:black}')
        self.RadioCNPJ.clicked.connect(self.ClickCNPJ)

        # RadioButton Auxiliar
        self.RadioAux = QRadioButton(self)
        self.RadioAux.move(220, 170)
        self.RadioAux.setText('Auxiliar')
        self.RadioAux.setStyleSheet('QRadioButton {font-size:10px;color:black}')
        self.RadioAux.setVisible(False)

        # Caixa de texto do CPF/CNPJ
        self.EditText = QLineEdit(self)
        self.EditText.move(45, 75)
        self.EditText.resize(200, 30)
        self.EditText.setStyleSheet('QLineEdit {font-size:20px;color:black}')
        self.EditText.setPlaceholderText('Escolha CPF ou CNPJ')
        self.EditText.setEnabled(False)
        self.EditText.textChanged.connect(self.onChangText)

        # Label Status de Validação:
        label2 = QLabel(self)
        label2.setText("Status: ")
        label2.move(45, 105)
        label2.resize(450, 40)
        label2.setStyleSheet('QLabel {font:bold;font-size:20px;color:black}')

        # Label Status de Valido:
        self.label3 = QLabel(self)
        self.label3.setText("VÁLIDO!")
        self.label3.move(125, 105)
        self.label3.resize(450, 40)
        self.label3.setStyleSheet('QLabel {font:bold;font-size:20px;color:#2FFF2E}')
        self.label3.setVisible(False)

        # Label Status de Invalido:
        self.label4 = QLabel(self)
        self.label4.setText("INVÁLIDO!")
        self.label4.move(125, 105)
        self.label4.resize(450, 40)
        self.label4.setStyleSheet('QLabel {font:bold;font-size:20px;color:#FE2F2F}')
        self.label4.setVisible(False)

        # Label Status ERRO:
        self.label5 = QLabel(self)
        self.label5.setText("ERRO!")
        self.label5.move(125, 105)
        self.label5.resize(450, 40)
        self.label5.setStyleSheet('QLabel {font:bold;font-size:20px;color:#FE2E64}')
        self.label5.setVisible(False)

        # Botao validar:
        self.Validar = QPushButton('Validar', self)
        self.Validar.move(80, 145)
        self.Validar.resize(125, 40)
        self.Validar.setStyleSheet('QPushButton {background-color:#B0C4DE;font:bold;font-size:18px}')
        self.Validar.setEnabled(False)
        self.Validar.clicked.connect(self.ObtemTpCod)

        # Botão Limpar
        self.Limpar = QPushButton('Limpar', self)
        self.Limpar.move(80, 190)
        self.Limpar.resize(125, 40)
        self.Limpar.setStyleSheet('QPushButton {background-color:#B0C4DE;font:bold;font-size:18px}')
        self.Limpar.setEnabled(False)
        self.Limpar.clicked.connect(self.Limpa)

        # Abre a janela
        self.LoadJanela()

    # Função que carrega a janela
    def LoadJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.RadioAux.setChecked(True)
        self.show()

    # Função Clique RadioButton CPF
    def ClickCPF(self):
        self.EditText.setEnabled(True)
        self.EditText.setPlaceholderText('Insira o CPF:')
        self.EditText.setFocus()
        self.EditText.setInputMask("999.999.999-99")
        self.EditText.setText('')
        self.EditText.setCursorPosition(0)
        self.Validar.setEnabled(False)
        self.Limpar.setEnabled(False)
        self.label3.setVisible(False)
        self.label4.setVisible(False)
        self.label5.setVisible(False)

    # Função Clique RadioButton CPF
    def ClickCNPJ(self):
        self.EditText.setEnabled(True)
        self.EditText.setPlaceholderText('Insira o CNPJ:')
        self.EditText.setFocus()
        self.EditText.setInputMask("99.999.999/9999-99")
        self.EditText.setText('')
        self.EditText.setCursorPosition(0)
        self.Validar.setEnabled(False)
        self.Limpar.setEnabled(False)
        self.label3.setVisible(False)
        self.label4.setVisible(False)
        self.label5.setVisible(False)

    # Função que verifica se o EditText está em branco:
    def onChangText(self):
        Codigo = self.EditText.text()
        Codigo = Codigo.replace(".", "")
        Codigo = Codigo.replace("-", "")
        Codigo = Codigo.replace("/", "")
        # print(Codigo)
        if Codigo != '':
            # print('Not Vazio')
            self.Validar.setEnabled(True)
            self.Limpar.setEnabled(True)
        else:
            # print('Vazio')
            self.Validar.setEnabled(False)
            self.Limpar.setEnabled(False)
        self.label3.setVisible(False)
        self.label4.setVisible(False)
        self.label5.setVisible(False)

    # Função que limpa tudo:
    def Limpa(self):
        # print("limpa tudo")
        self.RadioCPF.setChecked(False)
        self.RadioCNPJ.setChecked(False)
        self.RadioAux.setChecked(True)
        self.Validar.setEnabled(False)
        self.Limpar.setEnabled(False)
        self.EditText.setText("")
        self.EditText.setInputMask('')
        self.EditText.setEnabled(False)
        self.EditText.setPlaceholderText('Escolha CPF ou CNPJ')
        self.label3.setVisible(False)
        self.label4.setVisible(False)
        self.label5.setVisible(False)

    # Obtem Tipo e o Codigo
    def ObtemTpCod(self):
        Codigo = self.EditText.text()
        Codigo = Codigo.replace(".", "")
        Codigo = Codigo.replace("-", "")
        Codigo = Codigo.replace("/", "")
        if self.RadioCNPJ.isChecked():
            # print('Escolha = Cnpj')
            if len(Codigo) < 14:
                # print('Codigo Inválido')
                self.EditText.setFocus()
                self.EditText.setText('')
                self.label5.setVisible(True)
                self.EditText.setCursorPosition(0)
            else:
                # print('Codigo Válido')
                self.ValidarCodigoCNPJ(Codigo)
        elif self.RadioCPF.isChecked():
            # print('Escolha = Cpf')
            if len(Codigo) < 11:
                print('Codigo Inválido')
                self.EditText.setFocus()
                self.EditText.setText('')
                self.label5.setVisible(True)
                self.EditText.setCursorPosition(0)
            else:
                # print('Codigo Válido')
                self.ValidarCodigoCPF(Codigo)

    # Função validar Codigo
    def ValidarCodigoCPF(self, Codigo):
        # print('CPF = {}'.format(Codigo))
        # print('teste = {}'.format(Codigo[0]))
        if Codigo[0] == Codigo[1] == Codigo[2] == Codigo[3] == Codigo[4] == Codigo[5] == Codigo[6] == Codigo[7] == Codigo[8] == Codigo[9] == Codigo[10]:
            # print('tudo igual')
            self.label4.setVisible(True)
        else:
            # print('há diferente')
            # Calculo digito 1:
            m = 10
            soma1 = 0
            for n in range(9):
                # print('{} * {}'.format(Codigo[n], m))
                soma1 += (int(Codigo[n]) * m)
                m -= 1
            d1 = (soma1 * 10) % 11
            # print("D1 = {}".format(d1))
            if d1 != int(Codigo[9]):
                self.label4.setVisible(True)
            else:
                # print('Ver D2')
                o = 11
                soma2 = 0
                for p in range(10):
                    # print('{} * {}'.format(Codigo[n], m))
                    soma2 += (int(Codigo[p]) * o)
                    o -= 1
                d2 = (soma2 * 10) % 11
                # print("D2 = {}".format(d2))
                if d2 != int(Codigo[10]):
                    self.label4.setVisible(True)
                else:
                    self.label3.setVisible(True)

    # Função validar Codigo
    def ValidarCodigoCNPJ(self, Codigo):
        # print('CNPJ = {}'.format(Codigo))
        Igual = False
        # Verifica se todos os campos são iguais
        for n in range(len(Codigo) - 1):
            if Codigo[n] != Codigo[n+1]:
                Igual = True
        if not Igual:
            self.label4.setVisible(True)
        else:
            # Digito 1
            Mult = 6
            Soma = 0
            for m in range(12):
                print('{} * {}'.format(Codigo[m], Mult))
                Soma += (int(Codigo[m]) * Mult)
                Mult += 1
                if Mult == 10:
                    Mult = 2
            dg1 = Soma % 11
            # print(dg1)
            # If que verifica o 1º Digito Verifivador e inicia a verificação do 2º
            if int(Codigo[12]) != dg1:
                self.label4.setVisible(True)
            else:
                # Digito 2
                Mult = 5
                Soma = 0
                for m in range(12):
                    # print('{} * {}'.format(Codigo[m], Mult))
                    Soma += (int(Codigo[m]) * Mult)
                    Mult += 1
                    if Mult == 10:
                        Mult = 2
                    Soma += dg1 * 9
                dg2 = Soma % 11
                # print(dg1)
                # If que verifica o 2º Digito Verifivador
                if int(Codigo[13]) != dg2:
                    self.label4.setVisible(True)
                else:
                    self.label3.setVisible(True)


# Inicialização da Tela
application = QApplication(sys.argv)
Window = Janela()
sys.exit(application.exec_())
