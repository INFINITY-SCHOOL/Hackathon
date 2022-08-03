from Doador import Doador
from Instituicao import Instituicao
from Gerente import Gerente


#LISTAS
Doadores = []
Instituicoes = []
Gerentes = []



#MENU PRINCIPAL
while True:
    print('##### SISTEMA DOAÇÕES #####')
    print('1 ► Cadastrar')
    print('2 ► Listar')
    print('3 ► Consultar')
    print('0 ► Sair')
    menu = int(input('Oque você deseja realizar?\n>> '))



##### 1 ► CADASTRAR #####
    if menu == 1:
        while True:
            print('##### CADASTRAR #####')
            print('1 ► Instituição')
            print('2 ► Doador')
            print('0 ► Voltar')
            menu_cadastrar = int(input('>> '))

        #CADASTRAR NOVA INSTITUIÇÃO
            if menu_cadastrar == 1:
                while True:
                    print('#~@~# CADASTRAR INSTITUIÇÃO #~@~#')
                    nome_instituicao = input('Digite o nome da instituição\n>> ')
                    nome_gerente = input('Digite o nome do gerente\n>> ')
                    cpf_gerente = input('Digite o CPF do gerente\n>> ')

                    gerente = Gerente(nome_gerente, cpf_gerente)
                    Gerentes.append(gerente)
                    instituicao = Instituicao(nome_instituicao, gerente)
                    Instituicoes.append(instituicao)

                    continuar = input('Dejesa adiconar mais uma instituição? (s/n)\n>> ')
                    if continuar == 'n':
                        break

        #CADASTRAR NOVO DOADOR
            if menu_cadastrar == 2: 
                while True:
                    print('#~@~# CADASTRAR DOADOR #~@~#')
                    nome_doador = input('Digite o nome\n>> ')
                    cpf_doador = input('Digite o CPF\n>> ')
                    produto_doado = input('Digite o nome do produto que deseja doar\n>> ')
                    qtd_produto = int(input(f'Digite a quantidade de {produto_doado} que deseja doar\n>> '))
                    doador = Doador(nome_doador, cpf_doador, produto_doado, qtd_produto)


                    print(f'{nome_doador}! Você deseja doar para qual instituição?')
                    for ins in Instituicoes:
                        print(f'COD {Instituicoes.index(ins)} - NOME: {ins.nome}')
                    instituicao_doador = int(input(f'{nome_doador}! Digite o COD da instituicão que você deseja doar!\n>> '))
                    Doadores.append(doador)
                    Instituicoes[instituicao_doador].AdicionarDoador(doador)

                    continuar = input('Dejesa cadastrar mais um doador? (s/n)\n>> ')
                    if continuar == 'n':
                        break

        #VOLTAR PARA O MENU PRINCIPAL
            if menu_cadastrar == 0: 
                break



##### 2 ► LISTAR #####
    elif menu == 2:
        while True:
            print('##### LISTAR #####')
            print('1 ► Instituições')
            print('2 ► Doadores')
            print('0 ► Voltar')
            menu_listar = int(input('>> '))

        #LISTAR INSTITUIÇÕES
            if menu_listar == 1:
                for ins in Instituicoes:
                    print(f'COD {Instituicoes.index(ins)} - NOME: {ins.nome} - GERENTE: {ins.gerente.nome} - DOADORES: {len(ins.doadores)}')

        #LISTAR DOADORES
            if menu_listar == 2:
                for doa in Doadores:
                    print(f'DOADOR: {doa.nome} - CPF: {doa.cpf} - PRODUTO: {doa.produto_doado} - QAUNTIDADE: {doa.qtd_produto}')

        #VOLTAR PARA O MENU PRINCIPAL
            if menu_listar == 0:
                break

 

##### 3 ► CONSULTAR #####
    elif menu == 3:
        while True:
            print('##### CONSULTAR #####')
            print('1 ► Gerentes')
            print('0 ► Voltar')
            menu_consultar = int(input('\n>> '))

        #CONSULTAR DADOS DOS GERENTES    
            if menu_consultar == 1:
                for ins in Instituicoes:
                    print(f'COD {Instituicoes.index(ins)} - NOME: {ins.nome} - GERENTE: {ins.gerente.nome} - DOADORES: {len(ins.doadores)}')
                print('Digite o COD da instituição você deseja consultar o gerente')
                instituicao_selecionada = int(input('\n>> '))

                print(f'DADOS DO GERENTE DE {Instituicoes[instituicao_selecionada].nome}!')
                print(f'NOME: {Instituicoes[instituicao_selecionada].gerente.nome}')
                print(f'CPF: {Instituicoes[instituicao_selecionada].gerente.cpf}')

        #VOLTAR PARA O MENU PRINCIPAL
            if menu_consultar == 0:
                break               



##### 5 ► ENCERRAR PROGRAMA  #####              
    if menu == 0:
        break
#MSG DE SUCESSO!!!
print('DEU CERTO!')