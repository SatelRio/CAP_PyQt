from InterfacesGraficasPyqt.src.admOrdens import *
from datetime import datetime

hoje = (datetime.now().strftime('%d-%m-%Y'))
carta= 'Text01'
uc= 'Texto02'
endereco = 'Texto03'


listaDados = [carta,hoje,uc,endereco]
a1 = listaDados[0]
a2 = listaDados[1]

print(a1)


textoInicial = f'Rio de Janeiro, RJ – {hoje} \nCarta{carta}\nUC: {uc} ' \
               f'\n Ao cliente,\n Clienteclientecliente\nEndereço:{endereco}\n' \
               f'CIDADE-ESTADO\nCategoria: xxxxxxxxxxxxxxxx\n' \
               f'Assunto: Carta resposta a análise da sua solicitação'



aprovado = f'De acordo com as normas técnicas vigentes na ENEL Ceará,' \
           f' seu projeto encontra-se APROVADO segundo a norma CNC-OMBR-MAT-18-0xxx-EDBR.\n' \
           f' Desde já fica apto a execução de instalações a ser realizada por uma empresa' \
           f'legalmente habilitada devendo ser seguida as' \
           f' especificações técnicas contidas neste projeto. '


reprovado = 'Categoria: XXXXXXXXXXXXXXXXX\n\nPrezado (a),\nVimos por meio desta informar à V.Sa. ' \
            'que por não estar em consonância com as normas técnicas vigentes na ENEL Ceará' \
            ' (CNC-OMBR-MAT-18-0XXX-EDBR), este projeto encontra-se REPROVADO. ' \
            'Seguem os apontamentos de dissonância a seguir:'
ressalva = 'RESSALVAS:\n1:\n2:'

complemento_reprovado = 'Diante disto, após as devidas alterações solicitadas serem de fato realizadas,' \
                        ' favor encaminhar o projeto para reanálise na plataforma digital:' \
                        'http://satelpjceara.com/'





