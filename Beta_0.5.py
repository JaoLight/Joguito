import random
import sys
import os
import time

BOLD = '\033[1m'
END = '\033[0m'
NEG = '\033[7m'
AZUL = '\033[1;36m'
VERM = '\033[1;31m'
FAMAR = '\033[1;33m'
VERD = '\033[1;32m'

invent = {
    'chaves': 'Nenhuma',
    'outro': 'Nada',
    'arma': 'Nenhuma',
    'cbc': 'Nenhum',
    'peito': 'Nenhum',
    'mao': 'Nenhuma',
    'pe': 'Nenhum'
}


def slow_print(text, delay=0.1):


    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


itens = {
    'chaves': 'Nenhuma',
    'outro': 'Nada',
    'arma': {
        'adaga_peq': {
            'atk': 2,
            'crit': 0,
            'frase': f'''Adaga Pequena
    {VERM}+2 Dano / +0 Crítico{END}'''
        },
        'esp_enf': {
            'atk': 5,
            'crit': 1,
            'frase': f'''Espada Enferrujada
    {VERM}+5 Dano / +1 Crítico{END}'''
        }
    },
    'cbc': 'Nenhum',
    'peito': 'Nenhum',
    'mao': 'Nenhuma',
    'pe': 'Nenhum'
}

quests = {
    'Primeiras': ['']
}

armad = 0
armac = 0

prof = {
    'armor': {
        'arma': 'Nada',
        'arma_eq': '',
        'cbc': 'Nada',
        'peito': 'Nada',
        'mao': 'Nada',
        'pe': 'Nada'
    },
    'status': {
            'hp': 20,
            'defe': 0,
            'atk': 2 + armad + armac,
            'crit': 2
        },
}

if prof['armor']['arma_eq'] == 'adaga':
    armad = itens['arma']['adaga_peq']['atk']
    armac = itens['arma']['adaga_peq']['crit']

if prof['armor']['arma'] == 'espada':
    armad = itens['arma']['esp_enf']['atk']
    armac = itens['arma']['esp_enf']['crit']

mons = {
    'Sapo Azul': {
        'hp': 10,
        'atk': 2,
        'sacanaji': 999
    },

    'Cobra': {
        'hp': 1,
        'atk': 18
    }
}

bixo = {
    ''
}


def sapotk():
    mtk = random.randint(mons['Sapo Azul']['atk'] - 2, mons['Sapo Azul']['atk'])
    if mtk <= 0:
        mtk = 0
    prof['status']['hp'] = prof['status']['hp'] - mtk
    return mtk


mboss = {
    'jacare': {
        'hp': 50,
        'atk': 10
    }
}


def ranmo():
    monstro = list(mons.keys())
    rmons = random.choice(monstro)
    return rmons


def rantk():
    rcrit = random.randint(0, prof['status']['crit'])
    ratk = random.randint(prof['status']['atk'] - 2, prof['status']['atk'])
    ratk = ratk + rcrit
    return ratk


input('Escuro')
input('Apenas')
input('Escuro...')
slow_print('...', delay=0.7)
while True:
    un = str(input(f'{BOLD}[Qual é meu nome mesmo?]{END} '))

    if un == '':
        input('[Eu tenho um nome...]')
        continue
    else:
        break
input(f'{un}.....')
os.system('cls' if os.name == 'nt' else 'clear')
slow_print("...", delay=0.5)
input('Não sei onde estou')
input("Preciso fazer algo...")
por = ''

while True:
    print(f'{BOLD}======================================={END}')
    print(f'{BOLD}[DEVO ME LEVANTAR?]{END}')
    print('Levantar[a] Continuar Deitado[b]')
    print(f'{BOLD}======================================={END}')
    his = input('')

    if his == 'b':
        input("[levanta vagabundo]")

    elif his == 'a':
        input('Há uma luz saindo de uma pequena janela')
        break

    else:
        input('Escolha uma opção válida')
        continue

input('Você corre ate lá e vê algo')
input('A luz machuca seus olhos')
input('Finalmente você percebe')
slow_print("...", delay=0.7)
input('[Estou preso]')

escolhas = {
    'pt': {
        'msg': 'Você vê uma porta de metal',
        'est': 'Está trancada',
        'ac': 'olhar'
    },
    'jn': {
        'msg': 'Você vê um grande gramado',
        'est': 'bloqueada',
        'ac': 'olhar'
    },
    'cd': {
        'msg': 'Tem um cadeado trancando essa porta',
        'est': 'trancado',
        'ac': 'olhar'
    },
    'caixa': {
        'msg': 'Você vê uma caixa no canto da sala',
        'est': 'Fechada',
        'ac': 'Abrir'
    },
    'cv': {
        'msg': 'Tem uma chave dentro da caixa',
        'est': 'jogada',
        'ac': 'pegar'
    }
}


def hist():
    print(f'{AZUL}======================================={END}')
    print(f'{BOLD}[O QUE FAÇO AGORA?]{END}')
    print('Olhar na janela[a] Olhar em volta[b]')
    print(f'{AZUL}======================================={END}')


def cont():
    return escolhas['pt']['est'] == 'aberta'


while not cont():

    hist()

    his = input('')

    if his == 'a':
        input(escolhas['jn']['msg'])

    elif his == 'b':
        input('Tem uma porta de metal e uma caixa em sua frente')
        while True:
            print(f'{AZUL}======================================={END}')
            print(f'{BOLD}[O QUE VAI FAZER?]{END}')
            print('Abrir a porta[a] ver a caixa[b] ignorar[c]')
            print(f'{AZUL}======================================={END}')
            por = input('')

            if por == 'a':
                if escolhas['cv']['est'] == 'pega':
                    print(f'{VERM}======================================={END}')
                    print(f'{BOLD}A sua chave se encaixa perfeitamente no cadeado{END}')
                    print(f'{VERM}======================================={END}')
                    input('')
                    escolhas['pt']['est'] = 'aberta'
                    escolhas['cv']['est'] = ''
                    break

                else:
                    input(escolhas['cd']['msg'])
                    escolhas['cd']['ac'] = 'viu'

            elif por == 'b':
                if escolhas['cv']['est'] == 'pega':
                    input('Não há nada aqui')
                else:
                    while True:
                        input(escolhas['cv']['msg'])
                        print(f'{AZUL}======================================={END}')
                        print(F'{BOLD}[O QUE DESEJA FAZER?]{END}')
                        print('Pegar a chave[a] ignorar[b]')
                        print(f'{AZUL}======================================={END}')
                        k = input('')

                        if k == 'a':
                            input('[Você pegou a chave]')
                            escolhas['cv']['est'] = 'pega'
                            if escolhas['cd']['ac'] == 'viu':
                                input('[Você se lembra de ter visto uma porta]')
                                break
                            else:
                                break

                        elif k == 'b':
                            break
                        else:
                            input('Escolha uma opção válida')
                            continue

            elif por == 'c':
                print('')
                break

            else:
                input('Escolha uma opção válida')
                print('')
                continue

    else:
        input('Escolha uma opção válida')

input('Finalmente a porta se abriu')
input('Você passou pela porta')
input('Então você vê que aquele lugar era só um quarto jogado no meio de um grande gramado')
slow_print("...", delay=0.7)
input('Há um caminho de terra no chão')
input('Você começa a seguir até chegar em uma enorme floresta')
input('A estrada de terra se dividiu em dois caminhos diferentes')
input('A árvore que está na sua frente tem algo escrito...')
print(f'{FAMAR}======================================={END}')
print('')
print(f'      [<--- Floresta x Rio --->]')
print('')
print(f'{FAMAR}======================================={END}')
input(':')


def rio():
    def menu():
        while True:
            print(f'{BOLD}======================================={END}')
            print('')
            print(f'{BOLD}O QUE DESEJA, {un}{END}?')
            print('')
            print('Continuar[a]')
            print('Ver seu perfil[b]')
            print('Abrir o inventário[c]')
            print('Ver missões[d]')
            print('')
            print(f'{BOLD}======================================={END}')
            mm = input(':')

            def perfil():
                while True:
                    print(f'{VERD}======================================={END}')
                    print(f'{BOLD}PERFIL DE {un}:{END}')
                    print('')
                    print('HP:', prof['status']['hp'])
                    print('Defesa:', prof['status']['defe'])
                    print('Ataque:', prof['status']['atk'])
                    print(f'Dano Crítico: {prof["status"]["crit"]}')
                    print('')
                    print(f'{BOLD}-----//-----//-----//-----//-----//----{END}')
                    print('')
                    print(f'{BOLD}ARMADURA:{END}')
                    print('')
                    print('Cabeça:', prof['armor']['cbc'])
                    print('Peito:', prof['armor']['peito'])
                    print('Pés:', prof['armor']['pe'])
                    print('Mão:', prof['armor']['mao'])
                    print('Arma:', prof['armor']['arma'])
                    print('')
                    print('[sair[a]]')
                    print(f'{VERD}======================================={END}')
                    nn = input(':')

                    if nn == 'a':
                        break
                    else:
                        print('Digite uma opção válida')
                        continue

            def quest():
                while True:
                    print(f'{VERD}======================================={END}')
                    print('')
                    print(BOLD, 'MISSÕES ATIVAS:', END)
                    print(list(quests))
                    print('')
                    print('[sair[a]]')
                    print(f'{VERD}======================================={END}')
                    qq = input('')

                    match qq:
                        case 'a':
                            break
                        case _:
                            print('Digite uma opção válida')

            def inv():
                while True:
                    print(f'{VERD}======================================={END}')
                    print('')
                    print(f'{BOLD}ITENS{END}')
                    print('')
                    print('Chaves:')
                    print(invent['chaves'])
                    print('')
                    print('Outros Itens:')
                    print(invent['outro'])
                    print('')
                    print(f'{BOLD}-----//-----//-----//-----//-----//----{END}')
                    print('')
                    print(f'{BOLD}ARMAS E ARMADURAS:{END}')
                    print('')
                    print('Cabeça:', invent['cbc'])
                    print('Peito:', invent['peito'])
                    print('Pés:', invent['pe'])
                    print('Mão:', invent['mao'])
                    print('Arma:', invent['arma'])
                    print('')
                    print('[sair[a]]')
                    print(f'{VERD}======================================={END}')
                    bb = input(':')

                    if bb == 'a':
                        break
                    else:
                        print('Digite uma opção válida')

            if mm == 'a':
                break

            elif mm == 'b':
                print(perfil())

            elif mm == 'c':
                print(inv())

            elif mm == 'd':
                print(quest())

            else:
                print('Digite uma opção válida')
                continue

    print('')
    print(f'{AZUL}======================================={END}')
    print('')
    print('[Você escolheu o caminho da direita.]')
    print('É agora que sua jornada realmente começa...')
    print('')
    print(f'{AZUL}======================================={END}')
    print('')
    input(':')
    print(menu())

    input('Prosseguindo...')
    input('Você começou a seguir o caminho que a placa apontou dizendo que tem um rio')
    input('Mas não é possível ver rio nenhum')
    input('Ao invés disso só tem uma grande quantidade de árvores cobrindo toda a visão')
    input('Tudo o que dá pra ver alem das árvores é o caminho que está quase apagado')
    slow_print("...", delay=0.7)

    if prof['status']['hp'] <= 0:
        input(f'{VERM}VOCÊ MORREU{END}')
        sys.exit(0)
    input('[Tem algo se mechendo no mato]')
    input('...')
    input('[Era um sapo azul...]')
    print('...')
    input('Decepcionante...')
    while True:
        print(f'{VERM}======================================={END}')
        print(f'{BOLD}[VAI FAZER ALGO COM O SAPO?]{END}')
        print('Bater[a] Pegar[b] Ignorar[c] Abrir o Menu[d]')
        print(f'{VERM}======================================={END}')
        his = input('')

        if mons['Sapo Azul']['hp'] <= 0:
            input(f'{BOLD}[Você derrotou o sapo...]{END}')
            break

        if prof['status']['hp'] <= 0:
            input(f'{VERM}VOCÊ MORREU{END}')
            sys.exit(0)

        match his:
            case 'a':
                input(f'{BOLD}[Você bateu no sapo]{END}')
                matak = rantk()
                atak = sapotk()
                print(f'{VERM}======================================={END}')
                input(f'{BOLD}O sapo perdeu {matak} de {mons["Sapo Azul"]["hp"]} pontos de vida{END}')
                input(f'{BOLD}Você perdeu {atak} de {prof["status"]["hp"]} pontos de vida{END}')
                print(f'{VERM}======================================={END}')
                mons['Sapo Azul']['hp'] = mons['Sapo Azul']['hp'] - matak
                prof['status']['hp'] = prof['status']['hp'] - atak

            case 'b':
                input(f'{BOLD}[Você pegou o sapo]{END}')
                input('...')
                input('[Ele jogou a língua em sua testa]')
                print(f'{VERM}======================================={END}')
                input(f'{BOLD}{mons["Sapo Azul"]["sacanaji"]} de dano{END}')
                input(f'{BOLD}Você morreu...{END}')
                print(f'{VERM}======================================={END}')
                sys.exit(0)

            case 'c':
                input('[Você ignorou o sapo e passou direto]')
                slow_print("...", delay=0.7)
                input('Ele foi embora')
                slow_print("...", delay=0.7)
                break

            case 'd':
                print(menu())
                continue

            case _:
                input('Escolha uma opção válida')
                continue

    input('...')
    input('Ok né')
    input('Continuando...')
    input('Você continua seguindo a estrada')
    input('[Um barulho de água correndo]')
    input('[Parece que o rio já está perto]')
    input('Tem uma luz mais forte saindo do meio de duas árvores')
    input('Quando você passa por elas...')
    input('Tem uma bela nascente cercada de pedras')
    input('A nascente vai até uma parede com um moinho que só dá passagem para a água')
    input('Parece ser perigoso demais pra tentar passar')
    input('Mas ao lado da parede, tem uma pequena e simples cabana')
    input('Suas únicas opções são entrar ou esperar até apodrecer')
    input('Então você resolve ir até a cabana')
    input('[Tem um pequeno sino como campainha]')
    slow_print("...", delay=0.7)
    input('[O sino foi tocado]')
    input('[Mas ninguém veio]')
    slow_print("...", delay=0.7)
    input('Quando você se prepara pra tocar novamente, a porta se abre')
    input('[É um senhorzinho]')
    input(f'{FAMAR}- O que o traz aqui rapaz?{END}')
    input('...[Você conta toda a história]...')
    input(f'{FAMAR}- Entendi... você foi mais um...{END}')
    input('[Como assim mais um?]')
    input(f'{FAMAR}- Enfim, preciso saber se você está preparado para prosseguir.{END}')
    input(f'{FAMAR}- Te darei uma missão simples{END}')
    input(f'{FAMAR}- Se completar, ganhará uma boa recompensa{END}')
    input(f'{FAMAR}- Tome, você vai precisar...{END}')
    input(f'{AZUL}[Você recebeu uma adaga]{END}')
    prof['armor']['arma'] = f'''Adaga Pequena
    {VERM}+2 Dano / +1 Crítico{END}'''
    while True:
        global histo
        print(f'{BOLD}======================================={END}')
        print(f'{BOLD}[Deseja abrir o menu?]{END}')
        print(f'{BOLD}Sim[a] Não[b]{END}')
        print(f'{BOLD}======================================={END}')
        histo = input('')

        match histo:
            case 'a':
                print(menu())
                histo = 0
                break
            case 'b':
                break
            case _:
                input('Escolha uma opção válida')
                continue



def floresta():
    his = ''

    def menu():
        while True:
            print(f'{VERM}======================================={END}')
            print('')
            print(f'{BOLD}O que deseja, {un}{END}?')
            print('')
            print('Continuar[a]')
            print('Ver seu perfil[b]')
            print('Abrir o inventário[c]')
            print('Ver missões[d]')
            print('')
            print(f'{VERM}======================================={END}')
            mm = input(':')

            def perfil():
                while True:
                    print(f'{VERD}======================================={END}')
                    print(f'{BOLD}PERFIL DE {un}:{END}')
                    print('')
                    print('HP:', prof['status']['hp'])
                    print('Defesa:', prof['status']['defe'])
                    print('Ataque:', prof['status']['atk'])
                    print('')
                    print(f'{BOLD}-----//-----//-----//-----//-----//----{END}')
                    print('')
                    print(f'{BOLD}ARMADURA:{END}')
                    print('')
                    print('Cabeça:', prof['armor']['cbc'])
                    print('Peito:', prof['armor']['peito'])
                    print('Pés:', prof['armor']['pe'])
                    print('Mão:', prof['armor']['mao'])
                    print('Arma:', prof['armor']['arma'])
                    print('')
                    print('[sair[a]]')
                    print(f'{VERD}======================================={END}')
                    nn = input(':')

                    if nn == 'a':
                        break
                    else:
                        print('Digite uma opção válida')
                        continue

            def inv():
                while True:
                    print(f'{FAMAR}======================================={END}')
                    print('')
                    print(f'{BOLD}ITENS{END}')
                    print('')
                    print('Chaves:')
                    print(invent['chaves'])
                    print('')
                    print('Outros Itens:')
                    print(invent['outro'])
                    print('')
                    print(f'{BOLD}-----//-----//-----//-----//-----//----{END}')
                    print('')
                    print(f'{BOLD}ARMAS E ARMADURAS:{END}')
                    print('')
                    print('Cabeça:', invent['cbc'])
                    print('Peito:', invent['peito'])
                    print('Pés:', invent['pe'])
                    print('Mão:', invent['mao'])
                    print('Arma:', invent['arma'])
                    print('')
                    print('[sair[a]]')
                    print(f'{FAMAR}======================================={END}')
                    bb = input(':')

                    if bb == 'a':
                        break
                    else:
                        print('Digite uma opção válida')

            if mm == 'a':
                break

            elif mm == 'b':
                print(perfil())

            elif mm == 'c':
                print(inv())

            else:
                print('Digite uma opção válida')
                continue

    if his == 'abrir menu':
        print('menu()')

    print('')
    print(f'{VERD}======================================={END}')
    print('')
    print('[Você escolheu o caminho da esquerda.]')
    print('É agora que sua jornada realmente começa...')
    print('')
    print(f'{VERD}======================================={END}')
    print('')
    input(':')
    print(menu())

    print(f'{BOLD}======================================={END}')
    print('')
    print('Digite "abrir menu" para abrir o Menu novamente')
    print('')
    print(f'{BOLD}======================================={END}')
    print('')
    input(f'{BOLD}[Pressione Enter para continuar]{END}')
    print('')

    input('Prosseguindo...')
    his = input('')
    input('Você começou a seguir o caminho que parece levar até uma extensa floresta')

    if his == 'abrir menu':
        print(menu())
        print('Ahhhhh')


while True:
    print(f'{VERM}======================================={END}')
    print(f'{BOLD}ESCOLHA UM DOS DOIS LADOS:{END}')
    print('Esquerda[a] Direita[b]')
    print(f'{VERM}======================================={END}')
    his = input(':')

    if his == 'a':
        print(floresta())
    elif his == 'b':
        print(rio())
    else:
        input('ESCOLHA UMA OPÇÃO VÁLIDA')
        continue
