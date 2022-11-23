
from random import randint

# variables globales
numero_adversaire = 1
nbr_vie = 20
numero_combat = 1
nbr_victoires = 0
nbr_defaites = 0


def combat(force_adversaire, lancer_de): #fonctionne qui controle les combats
    global numero_adversaire, nbr_vie, numero_combat, nbr_victoires, nbr_defaites
    print(f'''
    force du monstre:{numero_adversaire}
    force de l'adversaire:{force_adversaire}
    vies:{nbr_vie}
    combat:{numero_combat}
    score du dé:{lancer_de}
    ''')
    if lancer_de > force_adversaire:
        print('victoire')
        nbr_vie = nbr_vie + force_adversaire
        numero_adversaire = numero_adversaire + 1
        numero_combat = numero_combat + 1
        nbr_victoires = nbr_victoires + 1
        return nbr_vie, numero_combat, numero_adversaire, nbr_victoires
    else:
        print('defaite')
        nbr_vie = nbr_vie - force_adversaire
        numero_adversaire = numero_adversaire + 1
        numero_combat = numero_combat + 1
        nbr_defaites = nbr_defaites + 1
        return nbr_vie, numero_combat, numero_adversaire, nbr_defaites


def restart(): #fonction qui "reset" les variables globales lorseque le jouer perd
    global numero_adversaire, nbr_vie, numero_combat, nbr_victoires, nbr_defaites
    defaite_answer = str(input('vous avez perdue,voules vous continue o/n'))
    if defaite_answer == "o":
        numero_adversaire = 1
        nbr_vie = 20
        numero_combat = 1
        nbr_victoires = 0
        nbr_defaites = 0
    else:
        quit()

def force(): #fonctionne pour le de(nbr aleatoire) de force des montres
    adversaire = randint(1, 6) + randint(1,6)
    return adversaire

def status(): #foction pour l'affisache de le status de la parties
        print(f'''
    Vous avez maitenant {nbr_vie} vies
    numero de combat:{numero_combat}
    numero d'adversaire:{numero_adversaire}
    nbr de victoire:{nbr_victoires}
    nbr de defaites:{nbr_defaites}
    ''')


force_adversaire = force()
while True:
    # chaque fois que le jouers bat 3 monstres , un "boss" va apparaitre, celle-ci est un mostre normale avec + 3 de force  rajouter à sa force initiale
    if nbr_victoires % 3 == 2: #on commence ce mecanisme de la victoire 0, donc le premiere boss aparait à la 2
        force_adversaire = force_adversaire + 3
        if force_adversaire >= 12:
            force_adversaire = 12 #pour balancer un peut le combat contre le boss, la force maximale de celle-ci est au maximun 12

    if nbr_vie < 1:
        restart()
    lancer_de = randint(1, 6) + randint(1,6)  # variable locale
    print(f'Force:{force_adversaire}')
    answer = int(input('''   
    Que voulez-vous faire ? 
	1- Combattre cet adversaire
	2- Contourner cet adversaire et aller ouvrir une autre porte
	3- Afficher les règles du jeu
	4- Quitter la partie
    '''))

    if answer == 1:
        combat(force_adversaire,lancer_de)
        status()
        force_adversaire = force()
    elif answer == 2:
        nbr_vie = nbr_vie - 1
        status()
        force_adversaire = force()
    elif answer == 3:
        print('''Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
La partie se termine lorsque les points de vie de l’usager tombent sous 0.
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
''')
    elif answer == 4:
        print('D`accord et aurevoir...')
        quit()