import os
import sys
import pandas as pd
import pymysql

from xhtml2pdf import pisa
from cap import *
#from Documentos.carta import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QFileDialog,QSplashScreen,QTableWidgetItem

conn = pymysql.connect(host="satelpjceara.com", port=3306, user="satelp03_marcosh",
password="12345678", db="satelp03_db_portal")
cur = conn.cursor()

data = {'col1':['1','2','3','4','5','6','7'],
        'col2':['1','2','3','4','5','6','7'],
        'col3':['1','1','2','1','5','6','7'] }

class Cap(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.tbl_tabela.setItem(0,0,QTableWidgetItem(''))
        self.btn_add.clicked.connect(self.addItem)
        y = 0
        while y <= 10:
            self.tbl_tabela.setItem(y, 0, QTableWidgetItem(''))
            y = y + 1



    def abrirPasta(self):
        pasta, _ = QFileDialog.getExistingDirectory (
            self.centralwidget, 'Abrir Imagem',
            r'C:/Users/Administrador Satel/Desktop/'
        )
    def addItem(self):

        potModulo = self.txtPotModulo.text()
        qtdModulo = self.txtQtdModulo.text()
        fabModulo = self.txtFabModulo.text()
        areaModulo = self.txt_area.text()
        potInversor = self.txtPotInversor.text()
        fabInversor = self.txtFab_Inv.text()
        codInmetro = self.txt_codInmetro.text()

        x = 0
        vazio = False
        try:
            while vazio == False:
                print('enntrou no While')
                if self.tbl_tabela.item(x, 0).text() == '' :
                    self.tbl_tabela.setItem(x, 0, QTableWidgetItem(potModulo))
                    self.tbl_tabela.setItem(x, 1, QTableWidgetItem(qtdModulo))
                    self.tbl_tabela.setItem(x, 2, QTableWidgetItem(fabModulo))
                    self.tbl_tabela.setItem(x, 3, QTableWidgetItem(areaModulo))
                    self.tbl_tabela.setItem(x, 4, QTableWidgetItem(potInversor))
                    self.tbl_tabela.setItem(x, 5, QTableWidgetItem(fabInversor))
                    #self.tbl_tabela.setItem(x, 7, QTableWidgetItem(codInmetro))

                    vazio = True
                    print('IF')
                else:
                    x = x+1
                    print(x)
                    print('Else')

        except Exception as erro:
            print(erro)


    def buscaOrdens(self):
        ordem = self.txtOrdem.text()
        sql = f"select * from tb_gerador_gd where ordem like '{ordem}' limit 1"
        tb_gerador_gd = pd.read_sql(sql, conn)
        lista = tb_gerador_gd.values.tolist()

        id = str(lista[0][0])
        ordem = lista[0][1]
        num_carta = lista[0][2]
        responsavel_tecnico = lista[0][3]
        empresa = str(lista[0][4])
        titular = str(lista[0][5])
        uc = str(lista[0][6])
        cpfcnpj = lista[0][7]
        endereco = lista[0][8]
        cidade = str(lista[0][9])
        cep = str(lista[0][10])
        telefone = str(lista[0][11])
        classe = str(lista[0][12])
        grupo = str(lista[0][13])
        latitude = str(lista[0][14])
        longitude = str(lista[0][15])
        tipo_ligacao = str(lista[0][16])
        tensao = str(lista[0][17])
        disjuntor = str(lista[0][18])
        potenciainstalada = str(lista[0][19])
        alimentador = str(lista[0][20])
        subestacao = str(lista[0][21])
        tensaonominal = str(lista[0][22])
        ponto_conexao = str(lista[0][23])
        array_modulo_inversor = str(lista[0][24])
        fonte_geracao = str(lista[0][25])
        consumo = str(lista[0][26])
        list_uc_porc = str(lista[0][27])
        motivo_reprovacao = str(lista[0][28])
        user_update = str(lista[0][29])
        data = str(lista[0][30])
        status = str(lista[0][31])
        email = str(lista[0][32])
        art = str(lista[0][33])
        memorial = str(lista[0][34])
        diagrama = str(lista[0][35])

        self.txtCarta.setText(num_carta)
        self.txtResponsavelTec.setText(responsavel_tecnico)
        self.txtEmpresa.setText(empresa)
        self.txtEmail.setText(email)
        self.txtTitular.setText(titular)
        self.txtEndereco.setText(endereco)
        self.txtClasse.setText(classe)
        self.txtTipoLigacao.setText(tipo_ligacao)
        self.txtCidade.setText(cidade)
        self.txtGrupo.setText(grupo)
        self.txtTensao.setText(tensao)
        self.txtAlimentador.setText(alimentador)
        self.txtSubestacao.setText(subestacao)
        self.txtUc.setText(uc)
        self.txtCep.setText(cep)
        self.txtLatitude.setText(latitude)
        self.txtDisjuntor.setText(disjuntor)
        self.txtTensaoNominal.setText(tensaonominal)
        self.txtCPFCNPJ.setText(cpfcnpj)
        self.txtTel.setText(telefone)
        self.txtLongitude.setText(longitude)
        self.txtPotDisp.setText(potenciainstalada)
        self.txtPontoConexao.setText(potenciainstalada)
        self.txtPontoConexao.setText(ponto_conexao)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cap = Cap()
    cap.show()
    qt.exec_()