import random
import sys
import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init()

# Text styles and colors
BOLD = Style.BRIGHT
END = Style.RESET_ALL
BLUE = Fore.CYAN
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN

# The game starter is in the end of the commands

def colored_text(text, color=Fore.WHITE, style=Style.NORMAL):
    return f"{style}{color}{text}{END}"

# Text effects
def slow_print(text, delay=0.03, end='\n'):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end=end)

def very_slow_print(text, delay=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Player
class Player:
    
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.defense = 0
        self.attack = 3
        self.crit_chance = 0
        self.equipped_weapon = None
        self.equipped_armor = None
        self.inventory = {
            'keys': [],
            'misc_items': [],
            'weapons': [],
            'armor_pieces': []
        }
        self.reputation = 0

    def calculate_damage(self):
        base_damage = random.randint(self.attack - 2, self.attack)
        crit_damage = random.randint(0, self.crit_chance)
        return base_damage + crit_damage

    def add_to_inventory(self, item_type, item_name):
        self.inventory[item_type].append(item_name)
        slow_print(f'[{BLUE}Você conseguiu: {END}{BOLD}{item_name}{END}]', delay=0.02)
        input()
        clear_screen()

    def equip_item(self, item_type, item_name):
        if item_type == 'weapons':
            if self.equipped_weapon:
                self.inventory['weapons'].append(self.equipped_weapon)
            if item_name in self.inventory['weapons']:
                self.equipped_weapon = item_name
                self.inventory['weapons'].remove(item_name)
                input(f'[Você equipou: {item_name}]')
            else:
                input('[Item não encontrado no inventário!]')

    def has_item(self, item_type, item_name):
        return item_name in self.inventory.get(item_type, [])

    def check_health(self):
        if self.health <= 0:
            slow_print(f"\n{RED}{BOLD}GAME OVER{END}", delay=0.1)
            sys.exit()
        elif self.health <= 5:
            slow_print(f"{YELLOW}Aviso: Sua saúde está crítica!{END}")

escolhas = {
    'porta': {
        'descricao': 'Porta de metal enferrujada',
        'estado': 'trancada',
        'acao': 'examinar',
        'opcao': 'a',
        'mensagem': 'Você vê uma porta de metal com um cadeado resistente',
        'requer_item': None,
        'item_necessario': None
    },
    'janela': {
        'descricao': 'Pequena janela com barras',
        'estado': 'bloqueada',
        'acao': 'olhar',
        'opcao': 'b',
        'mensagem': 'Através das barras, você vê um grande gramado lá fora',
        'requer_item': None,
        'item_necessario': None
    },

    'caixa': {
        'descricao': 'Caixa de madeira no canto',
        'estado': 'fechada',
        'acao': 'abrir',
        'opcao': 'c',
        'mensagem': 'Uma caixa de madeira empoeirada está no canto',
        'requer_item': None,
        'item_necessario': None
    }
}

def first_scene(player):
    clear_screen()
    slow_print(f'''{BLUE}======================================={END}
{BOLD}{colored_text('           [CELA DA PRISÃO]', YELLOW)}{END}
{BLUE}======================================={END}

Em sua frente, você encontra:''', delay=0.005)
    
    # Mostra opções disponíveis
    for item_id, item in escolhas.items():
        if item['estado'] not in ['removido', 'invisivel']:
            slow_print(f"- {item['descricao'].capitalize()} ({colored_text(item['opcao'], GREEN)}) [{item['estado']}]", delay=0.005)
    
    slow_print(f"\n{BLUE}======================================={END}", delay=0.005)
    slow_print(f"{RED}Sair do jogo{END} {BOLD}(q){END}")
    slow_print(f"{BLUE}======================================={END}", delay=0.005)

def first_choice(player):
    while True:
        first_scene(player)
        slow_print('\nO que você faz? ', delay=0.005, end=" ")
        escolha = input().lower().strip()
        
        if escolha == 'q':
            sys.exit()
        
        # Procura a escolha correspondente
        acao = None
        for item_id, item in escolhas.items():
            if item['opcao'] == escolha:
                acao = item_id
                break
        
        if acao:
            clear_screen()
            slow_print(f"\n{escolhas[acao]['mensagem']}", delay=0.01)
            
            # Lógica específica para cada ação
            if acao == 'caixa' and escolhas['caixa']['estado'] == 'fechada':
                input()
                slow_print("Você abre a caixa e encontra uma chave enferrujada!", delay=0.01)
                input()
                player.add_to_inventory('keys', 'Chave da cela')
                escolhas['caixa']['estado'] = 'aberta'
                escolhas['porta']['requer_item'] = 'keys'
                escolhas['porta']['item_necessario'] = 'Chave da cela'
                clear_screen()
            
            elif acao == 'porta':
                if player.has_item('keys', 'Chave da cela'):
                    input()
                    slow_print(f"[{BLUE}A chave se encaixa perfeitamente no cadeado{END}")
                    input()
                    clear_screen()
                    very_slow_print("A porta se abre com um rangido sinistro...")
                    input()
                    escolhas['porta']['estado'] = 'aberta'
                    return True  # Indica que a porta foi aberta
                else:
                    input()
                    slow_print("A porta está trancada... Você precisa de uma chave.")
            
            input()
        else:
            slow_print(f"\n{RED}Opção inválida. Tente novamente.{RED}", delay=0.08)

def game_introduction():
    clear_screen()
    slow_print(f'[{BLUE}Pressione {END}{BOLD}Enter{END}{BLUE} para continuar{END}]')
    input()
    clear_screen()
    very_slow_print('Escuro...', delay=0.22)
    input()
    very_slow_print('Apenas...', delay=0.22)
    input()
    clear_screen()
    very_slow_print('Escuro...', delay=0.5)
    input()
    clear_screen()
    slow_print("...", delay=0.7)
    
    # Get player name
    while True:
        slow_print(f'{BOLD}{GREEN}- Qual é meu nome mesmo?{END}', delay=0.02, end=' ')
        player_name = input().strip()
        if player_name:
            break
        slow_print(f'{GREEN}- Eu tenho um nome...{END}', delay=0.09)
        input()
        clear_screen()
    
    clear_screen()
    slow_print(f"{GREEN}- {player_name}...{END}", delay=0.12)
    input()
    clear_screen()
    slow_print(f"{GREEN}- Não sei onde estou...{END}")
    input()
    slow_print(f"{GREEN}- Preciso fazer algo...{END}")
    input()
    
    return player_name

def initial_scene(player):
    while True:
        clear_screen()
        menu_text = f"""
{BOLD}======================================={END}
{colored_text(f"{GREEN}- DEVO ME LEVANTAR?{END}", BOLD)}
{colored_text("1 - Levantar", GREEN)}
{colored_text("2 - Continuar deitado", RED)}
{BOLD}======================================={END}

Digite sua escolha:"""
        slow_print(menu_text, delay=0.01)
        
        choice = input().strip()\
        
        if choice == '1':
            clear_screen()
            slow_print("\nHá uma luz saindo de uma pequena janela...")
            input()
            break
        elif choice == '2':
            slow_print('\n[Levanta, vagabundo!]', delay=0.02)
            input()
            clear_screen()
        else:
            slow_print('\nEscolha uma opção válida!', delay=0.02)
            clear_screen()

    # Continue the story
    slow_print('Você corre até a luz...', delay=0.05)
    input()
    slow_print('A claridade machuca seus olhos...', delay=0.05)
    input()
    very_slow_print("...", delay=0.7)
    input()
    clear_screen()
    slow_print(f'{GREEN}- Estou preso...{END}', delay=0.1)
    input()
    clear_screen()
    slow_print(f'Você olha em volta e percebe que está preso em uma cela escura e úmida.')
    input()
    slow_print('Ao observar a sela você encontra algumas coisas...')
    input()
    
    # Inicia o sistema de escolhas interativas
    porta_aberta = False
    while not porta_aberta:
        porta_aberta = first_choice(player)
    
    # Continuação após sair da cela
    clear_screen()
    slow_print("Você sai da cela e se encontra em um corredor escuro...")
    input()

def second_scene():
    clear_screen()
    slow_print(f'''{BLUE}======================================={END}
{colored_text('            [DOIS CAMINHOS]', YELLOW)}
{BLUE}======================================={END}

Para qual lado você irá?
[1] Esquerda (Floresta Densa)
[2] Direita (Rio)''', delay=0.005)
    slow_print(f"\n{BLUE}======================================={END}", delay=0.005)
    slow_print(f"{RED}Sair do jogo{END} {BOLD}(q){END}")
    slow_print(f"{BLUE}======================================={END}", delay=0.005)

def second_choice():
    while True:
        second_scene()
        way = input('')
        if way == 'q':
            sys.exit()
        elif way == '1':
            clear_screen()
            slow_print('Você decidiu ir pelo caminho da esquerda')
            return 'left'
        elif way == '2':
            clear_screen()
            slow_print('Você decidiu ir pelo caminho da direita')
            return 'right'
        else:
            slow_print(f"\n{RED}Opção inválida. Tente novamente.{RED}", delay=0.08)
            clear_screen()

def after_ceil():
    clear_screen()
    slow_print(f'{GREEN}- Finalmente a porta se abriu{END}')
    input()
    clear_screen()
    slow_print('''Ao passar pela porta, você percebe que aquela cela era apenas
uma pequena sala no meio de um grande campo...''')
    input()
    slow_print('Você olha para o chão e percebe um caminho levando para uma grande floresta')
    input()
    slow_print('Como você não tem outra escolha, começa a seguir este caminho')
    input()
    clear_screen()
    slow_print('''Depois de uma longa caminhada seguindo a estrada, você percebe que ela
leva até uma árvore e que se divide para dois lados.''')
    input()
    slow_print('Na frente dessa árvore, você vê uma placa')
    input()
    clear_screen()
    slow_print(f'''{YELLOW}======================================={END}

      {BOLD}[<--- Floresta x Rio --->]{END}

{YELLOW}======================================={END}''', delay=0.01)
    input()
    clear_screen()
    slow_print('Qual caminho você escolherá?')
    input()
    clear_screen()

def left_way():
    slow_print('jaojdoejojedw')

def right_way():
    clear_screen()
    slow_print('[Barulho de explosão atrás de você]')
    slow_print('...', delay=0.4)

def show_status(player):
    clear_screen()
    slow_print(f'''{BLUE}====== STATUS DE {player.name.upper()} ======={END}

{GREEN}SAÚDE:{END} {BOLD}{player.health}/20{END}
{YELLOW}ATAQUE:{END} {BOLD}{player.attack}{END}
{RED}CRÍTICO:{END} {BOLD}{player.crit_chance}{END}
{BLUE}DEFESA:{END} {BOLD}{player.defense}{END}

{BLUE}=========== EQUIPAMENTOS ==========={END}

ARMA: {BOLD}{player.equipped_weapon or "Nenhuma"}{END}
ARMADURA: {BOLD}{player.equipped_armor or "Nenhuma"}{END}
{YELLOW}REPUTAÇÃO: {END}{BOLD}{player.reputation}{END}

{BLUE}===================================={END}

[{BLUE}Pressione {END}{BOLD}ENTER{END}{BLUE} para continuar{END}]

{BLUE}===================================={END}''', delay=0.005)
    input()

# Game start
def debug_mode():
    # DevMode
    player = Player("DebugPlayer")  # Create a debugger player
    player.add_to_inventory('keys', 'Chave da cela')  # Add important items to inventory
    

    while True:
        slow_print('Escolha a cena que deseja testar:')
        print('')
        slow_print('Início [1], Prisão [2], Pós Prisão [3], Mostrar Menu [4]')
        scene = input()
    
        if scene == '1':
            initial_scene(player)
            clear_screen()
        elif scene == '2':
            first_choice(player)
            clear_screen()
        elif scene == '3':
            after_ceil()
            clear_screen()
        elif scene == '4':
            show_status(player)
            clear_screen()
        else:
            slow_print('Digite uma opção válida', delay=0.08)
            clear_screen()
            
def main():
    # Game setup
    player_name = game_introduction()
    hero = Player(player_name)
    
    # Start the story
    initial_scene(hero)
    
    # Continue story...
    slow_print("Sua aventura está apenas começando...")
    input()
    after_ceil()
    game = second_choice()

    # story line
    if game == 'left':
        left_way()
    elif game == 'right':
        right_way()

if __name__ == "__main__":
    #main()

    # To enter in debug mode, comment "main()" line and uncomment "debug_mode()" line
    debug_mode()

def rio():
    def menu():
        while True:
            print(f'{BOLD}======================================={END}')
            print('')
            print(f'{BOLD}O QUE DESEJA, {Player.name}{END}?')
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
    input(f'[{BOLD}Pressione {END}{BOLD}Enter{END}{BLUE} para continuar{END}]')
    print('')

    input('Prosseguindo...')
    his = input('')
    input('Você começou a seguir o caminho que parece levar até uma extensa floresta')

    if his == 'abrir menu':
        print(menu())
        print('Ahhhhh')