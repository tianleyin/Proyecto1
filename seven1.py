import random


def capcelera():
    s1 = (
        "   _|_|_|                                                                          _|      _|    _|            _|      _|_|")
    s2 = (
        "_|          _|_|    _|      _|    _|_|    _|_|_|          _|_|_|  _|_|_|      _|_|_|      _|    _|    _|_|_|  _|    _|      ")
    s3 = (
        "  _|_|    _|_|_|_|  _|      _|  _|_|_|_|  _|    _|      _|    _|  _|    _|  _|    _|      _|_|_|_|  _|    _|  _|  _|_|_|_|  ")
    s4 = (
        "      _|  _|          _|  _|    _|        _|    _|      _|    _|  _|    _|  _|    _|      _|    _|  _|    _|  _|    _|      ")
    s5 = (
        "_|_|_|      _|_|_|      _|        _|_|_|  _|    _|        _|_|_|  _|    _|    _|_|_|      _|    _|    _|_|_|  _|    _|      ")
    s6 = ("")
    print(s1, "\n", s2, "\n", s3, "\n", s4, "\n", s5, "\n", s6)
    print("-" * 124)


capcelera()
menu_cards = "\n" + "*" * 10 + "Card deck's" + "*" * 10 + "1)Baraja Española\n2)Baraja Pocker\n3)More information about Card Deck's\n4)Go Back"
menu00 = "1)Add/Remove/Show Players\n2)Settings\n3)Play Game\n4)Ranking\n5)Reports\n6)Exit"
menu01 = "\n" + "*" * 10 + "Add/Remove/Show" + "*" * 10 + "\n" + "1)Add Players\n2)Remove players\n3)Show Players\n4)Go Back"
menu02 = "\n" + "*" * 10 + "Setting" + "*" * 10 + "\n" + "1)Set Game Players\n2)Set Card's Deck\n3)Set Max Rounds\n4)Go Back"
cartas = {"Baraja Española": {
    "O01": {"literal": "As de Oros", "value": 1, "priority": 4, "realValue": 1},
    "O02": {"literal": "Dos de Oros", "value": 2, "priority": 4, "realValue": 2},
    "O03": {"literal": "Tres de Oros", "value": 3, "priority": 4, "realValue": 3},
    "O04": {"literal": "Cuatro de Oros", "value": 4, "priority": 4, "realValue": 4},
    "O05": {"literal": "Cinco de Oros", "value": 5, "priority": 4, "realValue": 5},
    "O06": {"literal": "Seis de Oros", "value": 6, "priority": 4, "realValue": 6},
    "O07": {"literal": "Siete de Oros", "value": 7, "priority": 4, "realValue": 7},
    "O10": {"literal": "Sota de Oros", "value": 10, "priority": 4, "realValue": 0.5},
    "O11": {"literal": "Caballo de Oros", "value": 11, "priority": 4, "realValue": 0.5},
    "O12": {"literal": "Rey de Oros", "value": 12, "priority": 4, "realValue": 0.5},
    "C01": {"literal": "As de Copas", "value": 1, "priority": 3, "realValue": 1},
    "C02": {"literal": "Dos de Copas", "value": 2, "priority": 3, "realValue": 2},
    "C03": {"literal": "Tres de Copas", "value": 3, "priority": 3, "realValue": 3},
    "C04": {"literal": "Cuatro de Copas", "value": 4, "priority": 3, "realValue": 4},
    "C05": {"literal": "Cinco de Copas", "value": 5, "priority": 3, "realValue": 5},
    "C06": {"literal": "Seis de Copas", "value": 6, "priority": 3, "realValue": 6},
    "C07": {"literal": "Siete de Copas", "value": 7, "priority": 3, "realValue": 7},
    "C10": {"literal": "Sota de Copas", "value": 10, "priority": 3, "realValue": 0.5},
    "C11": {"literal": "Caballo de Copas", "value": 11, "priority": 3, "realValue": 0.5},
    "C12": {"literal": "Rey de Copas", "value": 12, "priority": 3, "realValue": 0.5},
    "E01": {"literal": "As de Espadas", "value": 1, "priority": 2, "realValue": 1},
    "E02": {"literal": "Dos de Espadas", "value": 2, "priority": 2, "realValue": 2},
    "E03": {"literal": "Tres de Espadas", "value": 3, "priority": 2, "realValue": 3},
    "E04": {"literal": "Cuatro de Espadas", "value": 4, "priority": 2, "realValue": 4},
    "E05": {"literal": "Cinco de Espadas", "value": 5, "priority": 2, "realValue": 5},
    "E06": {"literal": "Seis de Espadas", "value": 6, "priority": 2, "realValue": 6},
    "E07": {"literal": "Siete de Espadas", "value": 7, "priority": 2, "realValue": 7},
    "E10": {"literal": "Sota de Espadas", "value": 10, "priority": 2, "realValue": 0.5},
    "E11": {"literal": "Caballo de Espadas", "value": 11, "priority": 2, "realValue": 0.5},
    "E12": {"literal": "Rey de Espadas", "value": 12, "priority": 2, "realValue": 0.5},
    "B01": {"literal": "As de Bastos", "value": 1, "priority": 1, "realValue": 1},
    "B02": {"literal": "Dos de Bastos", "value": 2, "priority": 1, "realValue": 2},
    "B03": {"literal": "Tres de Bastos", "value": 3, "priority": 1, "realValue": 3},
    "B04": {"literal": "Cuatro de Bastos", "value": 4, "priority": 1, "realValue": 4},
    "B05": {"literal": "Cinco de Bastos", "value": 5, "priority": 1, "realValue": 5},
    "B06": {"literal": "Seis de Bastos", "value": 6, "priority": 1, "realValue": 6},
    "B07": {"literal": "Siete de Bastos", "value": 7, "priority": 1, "realValue": 7},
    "B10": {"literal": "Sota de Bastos", "value": 10, "priority": 1, "realValue": 0.5},
    "B11": {"literal": "Caballo de Bastos", "value": 11, "priority": 1, "realValue": 0.5},
    "B12": {"literal": "Rey de Bastos", "value": 12, "priority": 1, "realValue": 0.5},
},
    "Baraja de Poker": {
        "C01": {"literal": "As de Corazones", "value": 1, "priority": 4, "realValue": 1},
        "C02": {"literal": "Dos de Corazones", "value": 2, "priority": 4, "realValue": 2},
        "C03": {"literal": "Tres de Corazones", "value": 3, "priority": 4, "realValue": 3},
        "C04": {"literal": "Cuatro de Corazones", "value": 4, "priority": 4, "realValue": 4},
        "C05": {"literal": "Cinco de Corazones", "value": 5, "priority": 4, "realValue": 5},
        "C06": {"literal": "Seis de Corazones", "value": 6, "priority": 4, "realValue": 6},
        "C07": {"literal": "Siete de Corazones", "value": 7, "priority": 4, "realValue": 7},
        "C08": {"literal": "Ocho de Corazones", "value": 8, "priority": 4, "realValue": 0.5},
        "C09": {"literal": "Nueve de Corazones", "value": 9, "priority": 4, "realValue": 0.5},
        "C10": {"literal": "Diez de Corazones", "value": 10, "priority": 4, "realValue": 0.5},
        "C11": {"literal": "Jota de Corazones", "value": 11, "priority": 4, "realValue": 0.5},
        "C12": {"literal": "Reina de Corazones", "value": 12, "priority": 4, "realValue": 0.5},
        "C13": {"literal": "Rey de Corazones", "value": 13, "priority": 4, "realValue": 0.5},
        "P01": {"literal": "As de Picas", "value": 1, "priority": 3, "realValue": 1},
        "P02": {"literal": "Dos de Picas", "value": 2, "priority": 3, "realValue": 2},
        "P03": {"literal": "Tres de Picas", "value": 3, "priority": 3, "realValue": 3},
        "P04": {"literal": "Cuatro de Picas", "value": 4, "priority": 3, "realValue": 4},
        "P05": {"literal": "Cinco de Picas", "value": 5, "priority": 3, "realValue": 5},
        "P06": {"literal": "Seis de Picas", "value": 6, "priority": 3, "realValue": 6},
        "P07": {"literal": "Siete de Picas", "value": 7, "priority": 3, "realValue": 7},
        "P08": {"literal": "Ocho de Picas", "value": 8, "priority": 3, "realValue": 0.5},
        "P09": {"literal": "Nueve de Picas", "value": 9, "priority": 3, "realValue": 0.5},
        "P10": {"literal": "Diez de Picas", "value": 10, "priority": 3, "realValue": 0.5},
        "P11": {"literal": "Jota de Picas", "value": 11, "priority": 3, "realValue": 0.5},
        "P12": {"literal": "Reina de Picas", "value": 12, "priority": 3, "realValue": 0.5},
        "P13": {"literal": "Rey de Picas", "value": 13, "priority": 3, "realValue": 0.5},
        "T01": {"literal": "As de Treboles", "value": 1, "priority": 2, "realValue": 1},
        "T02": {"literal": "Dos de Treboles", "value": 2, "priority": 2, "realValue": 2},
        "T03": {"literal": "Tres de Treboles", "value": 3, "priority": 2, "realValue": 3},
        "T04": {"literal": "Cuatro de Treboles", "value": 4, "priority": 2, "realValue": 4},
        "T05": {"literal": "Cinco de Treboles", "value": 5, "priority": 2, "realValue": 5},
        "T06": {"literal": "Seis de Treboles", "value": 6, "priority": 2, "realValue": 6},
        "T07": {"literal": "Siete de Treboles", "value": 7, "priority": 2, "realValue": 7},
        "T08": {"literal": "Ocho de Treboles", "value": 8, "priority": 2, "realValue": 0.5},
        "T09": {"literal": "Nueve de Treboles", "value": 9, "priority": 2, "realValue": 0.5},
        "T10": {"literal": "Diez de Treboles", "value": 10, "priority": 2, "realValue": 0.5},
        "T10": {"literal": "Jota de Treboles", "value": 11, "priority": 2, "realValue": 0.5},
        "T11": {"literal": "Reina de Treboles", "value": 12, "priority": 2, "realValue": 0.5},
        "T12": {"literal": "Rey de Treboles", "value": 13, "priority": 2, "realValue": 0.5},
        "N01": {"literal": "As de Naipes", "value": 1, "priority": 1, "realValue": 1},
        "N02": {"literal": "Dos de Naipes", "value": 2, "priority": 1, "realValue": 2},
        "N03": {"literal": "Tres de Naipes", "value": 3, "priority": 1, "realValue": 3},
        "N04": {"literal": "Cuatro de Naipes", "value": 4, "priority": 1, "realValue": 4},
        "N05": {"literal": "Cinco de Naipes", "value": 5, "priority": 1, "realValue": 5},
        "N06": {"literal": "Seis de Naipes", "value": 6, "priority": 1, "realValue": 6},
        "N07": {"literal": "Siete de Naipes", "value": 7, "priority": 1, "realValue": 7},
        "N08": {"literal": "Ocho de Naipes", "value": 8, "priority": 1, "realValue": 0.5},
        "N09": {"literal": "Nueve de Naipes", "value": 9, "priority": 1, "realValue": 0.5},
        "N10": {"literal": "Diez de Naipes", "value": 10, "priority": 1, "realValue": 0.5},
        "N11": {"literal": "Jota de Naipes", "value": 11, "priority": 1, "realValue": 0.5},
        "N12": {"literal": "Reina de Naipes", "value": 12, "priority": 1, "realValue": 0.5},
        "N13": {"literal": "Rey de Naipes", "value": 13, "priority": 1, "realValue": 0.5},
    }
}
cartas_real = {"Baraja Española": {
    "O01": {"literal": "As de Oros", "value": 1, "priority": 4, "realValue": 1},
    "O02": {"literal": "Dos de Oros", "value": 2, "priority": 4, "realValue": 2},
    "O03": {"literal": "Tres de Oros", "value": 3, "priority": 4, "realValue": 3},
    "O04": {"literal": "Cuatro de Oros", "value": 4, "priority": 4, "realValue": 4},
    "O05": {"literal": "Cinco de Oros", "value": 5, "priority": 4, "realValue": 5},
    "O06": {"literal": "Seis de Oros", "value": 6, "priority": 4, "realValue": 6},
    "O07": {"literal": "Siete de Oros", "value": 7, "priority": 4, "realValue": 7},
    "O10": {"literal": "Sota de Oros", "value": 10, "priority": 4, "realValue": 0.5},
    "O11": {"literal": "Caballo de Oros", "value": 11, "priority": 4, "realValue": 0.5},
    "O12": {"literal": "Rey de Oros", "value": 12, "priority": 4, "realValue": 0.5},
    "C01": {"literal": "As de Copas", "value": 1, "priority": 3, "realValue": 1},
    "C02": {"literal": "Dos de Copas", "value": 2, "priority": 3, "realValue": 2},
    "C03": {"literal": "Tres de Copas", "value": 3, "priority": 3, "realValue": 3},
    "C04": {"literal": "Cuatro de Copas", "value": 4, "priority": 3, "realValue": 4},
    "C05": {"literal": "Cinco de Copas", "value": 5, "priority": 3, "realValue": 5},
    "C06": {"literal": "Seis de Copas", "value": 6, "priority": 3, "realValue": 6},
    "C07": {"literal": "Siete de Copas", "value": 7, "priority": 3, "realValue": 7},
    "C10": {"literal": "Sota de Copas", "value": 10, "priority": 3, "realValue": 0.5},
    "C11": {"literal": "Caballo de Copas", "value": 11, "priority": 3, "realValue": 0.5},
    "C12": {"literal": "Rey de Copas", "value": 12, "priority": 3, "realValue": 0.5},
    "E01": {"literal": "As de Espadas", "value": 1, "priority": 2, "realValue": 1},
    "E02": {"literal": "Dos de Espadas", "value": 2, "priority": 2, "realValue": 2},
    "E03": {"literal": "Tres de Espadas", "value": 3, "priority": 2, "realValue": 3},
    "E04": {"literal": "Cuatro de Espadas", "value": 4, "priority": 2, "realValue": 4},
    "E05": {"literal": "Cinco de Espadas", "value": 5, "priority": 2, "realValue": 5},
    "E06": {"literal": "Seis de Espadas", "value": 6, "priority": 2, "realValue": 6},
    "E07": {"literal": "Siete de Espadas", "value": 7, "priority": 2, "realValue": 7},
    "E10": {"literal": "Sota de Espadas", "value": 10, "priority": 2, "realValue": 0.5},
    "E11": {"literal": "Caballo de Espadas", "value": 11, "priority": 2, "realValue": 0.5},
    "E12": {"literal": "Rey de Espadas", "value": 12, "priority": 2, "realValue": 0.5},
    "B01": {"literal": "As de Bastos", "value": 1, "priority": 1, "realValue": 1},
    "B02": {"literal": "Dos de Bastos", "value": 2, "priority": 1, "realValue": 2},
    "B03": {"literal": "Tres de Bastos", "value": 3, "priority": 1, "realValue": 3},
    "B04": {"literal": "Cuatro de Bastos", "value": 4, "priority": 1, "realValue": 4},
    "B05": {"literal": "Cinco de Bastos", "value": 5, "priority": 1, "realValue": 5},
    "B06": {"literal": "Seis de Bastos", "value": 6, "priority": 1, "realValue": 6},
    "B07": {"literal": "Siete de Bastos", "value": 7, "priority": 1, "realValue": 7},
    "B10": {"literal": "Sota de Bastos", "value": 10, "priority": 1, "realValue": 0.5},
    "B11": {"literal": "Caballo de Bastos", "value": 11, "priority": 1, "realValue": 0.5},
    "B12": {"literal": "Rey de Bastos", "value": 12, "priority": 1, "realValue": 0.5},
},
    "Baraja de Poker": {
        "C01": {"literal": "As de Corazones", "value": 1, "priority": 4, "realValue": 1},
        "C02": {"literal": "Dos de Corazones", "value": 2, "priority": 4, "realValue": 2},
        "C03": {"literal": "Tres de Corazones", "value": 3, "priority": 4, "realValue": 3},
        "C04": {"literal": "Cuatro de Corazones", "value": 4, "priority": 4, "realValue": 4},
        "C05": {"literal": "Cinco de Corazones", "value": 5, "priority": 4, "realValue": 5},
        "C06": {"literal": "Seis de Corazones", "value": 6, "priority": 4, "realValue": 6},
        "C07": {"literal": "Siete de Corazones", "value": 7, "priority": 4, "realValue": 7},
        "C08": {"literal": "Ocho de Corazones", "value": 8, "priority": 4, "realValue": 0.5},
        "C09": {"literal": "Nueve de Corazones", "value": 9, "priority": 4, "realValue": 0.5},
        "C10": {"literal": "Diez de Corazones", "value": 10, "priority": 4, "realValue": 0.5},
        "C11": {"literal": "Jota de Corazones", "value": 11, "priority": 4, "realValue": 0.5},
        "C12": {"literal": "Reina de Corazones", "value": 12, "priority": 4, "realValue": 0.5},
        "C13": {"literal": "Rey de Corazones", "value": 13, "priority": 4, "realValue": 0.5},
        "P01": {"literal": "As de Picas", "value": 1, "priority": 3, "realValue": 1},
        "P02": {"literal": "Dos de Picas", "value": 2, "priority": 3, "realValue": 2},
        "P03": {"literal": "Tres de Picas", "value": 3, "priority": 3, "realValue": 3},
        "P04": {"literal": "Cuatro de Picas", "value": 4, "priority": 3, "realValue": 4},
        "P05": {"literal": "Cinco de Picas", "value": 5, "priority": 3, "realValue": 5},
        "P06": {"literal": "Seis de Picas", "value": 6, "priority": 3, "realValue": 6},
        "P07": {"literal": "Siete de Picas", "value": 7, "priority": 3, "realValue": 7},
        "P08": {"literal": "Ocho de Picas", "value": 8, "priority": 3, "realValue": 0.5},
        "P09": {"literal": "Nueve de Picas", "value": 9, "priority": 3, "realValue": 0.5},
        "P10": {"literal": "Diez de Picas", "value": 10, "priority": 3, "realValue": 0.5},
        "P11": {"literal": "Jota de Picas", "value": 11, "priority": 3, "realValue": 0.5},
        "P12": {"literal": "Reina de Picas", "value": 12, "priority": 3, "realValue": 0.5},
        "P13": {"literal": "Rey de Picas", "value": 13, "priority": 3, "realValue": 0.5},
        "T01": {"literal": "As de Treboles", "value": 1, "priority": 2, "realValue": 1},
        "T02": {"literal": "Dos de Treboles", "value": 2, "priority": 2, "realValue": 2},
        "T03": {"literal": "Tres de Treboles", "value": 3, "priority": 2, "realValue": 3},
        "T04": {"literal": "Cuatro de Treboles", "value": 4, "priority": 2, "realValue": 4},
        "T05": {"literal": "Cinco de Treboles", "value": 5, "priority": 2, "realValue": 5},
        "T06": {"literal": "Seis de Treboles", "value": 6, "priority": 2, "realValue": 6},
        "T07": {"literal": "Siete de Treboles", "value": 7, "priority": 2, "realValue": 7},
        "T08": {"literal": "Ocho de Treboles", "value": 8, "priority": 2, "realValue": 0.5},
        "T09": {"literal": "Nueve de Treboles", "value": 9, "priority": 2, "realValue": 0.5},
        "T10": {"literal": "Diez de Treboles", "value": 10, "priority": 2, "realValue": 0.5},
        "T10": {"literal": "Jota de Treboles", "value": 11, "priority": 2, "realValue": 0.5},
        "T11": {"literal": "Reina de Treboles", "value": 12, "priority": 2, "realValue": 0.5},
        "T12": {"literal": "Rey de Treboles", "value": 13, "priority": 2, "realValue": 0.5},
        "N01": {"literal": "As de Naipes", "value": 1, "priority": 1, "realValue": 1},
        "N02": {"literal": "Dos de Naipes", "value": 2, "priority": 1, "realValue": 2},
        "N03": {"literal": "Tres de Naipes", "value": 3, "priority": 1, "realValue": 3},
        "N04": {"literal": "Cuatro de Naipes", "value": 4, "priority": 1, "realValue": 4},
        "N05": {"literal": "Cinco de Naipes", "value": 5, "priority": 1, "realValue": 5},
        "N06": {"literal": "Seis de Naipes", "value": 6, "priority": 1, "realValue": 6},
        "N07": {"literal": "Siete de Naipes", "value": 7, "priority": 1, "realValue": 7},
        "N08": {"literal": "Ocho de Naipes", "value": 8, "priority": 1, "realValue": 0.5},
        "N09": {"literal": "Nueve de Naipes", "value": 9, "priority": 1, "realValue": 0.5},
        "N10": {"literal": "Diez de Naipes", "value": 10, "priority": 1, "realValue": 0.5},
        "N11": {"literal": "Jota de Naipes", "value": 11, "priority": 1, "realValue": 0.5},
        "N12": {"literal": "Reina de Naipes", "value": 12, "priority": 1, "realValue": 0.5},
        "N13": {"literal": "Rey de Naipes", "value": 13, "priority": 1, "realValue": 0.5},
    }
}
players = {
    "11115555A": {"name": "Mario", "human": True, "bank": False, "initialCard": "", "priority": 0
        , "type": 40, "bet": 4, "points": 20, "cards": [], "roundPoints": 0},
    "22225555A": {"name": "Pedro", "human": True, "bank": False, "initialCard": "", "priority": 0
        , "type": 40, "bet": 4, "points": 20, "cards": [], "roundPoints": 0},
}
game = [  # SE AÑADIRAN LOS NIF DE LOS JUGADORES QUE JUEGUEN EN EL MOMENTO
]
mazo = [  # ID DE LAS CARTAS QUE COMPONEN EL MAZO DEL MOMENTO
]
context_game = {"round": 0  # SE PUEDEN AÑADIR DATOS DE CONTEXTO COMO round= 2
                }
rounds = [5]
count_rounds = [0]
results_bet = {}


# DICCIONARIOS PARA ACTUALIZAR DATOS DE LA BBDD
# cardgame = {'cardgame_id': id de partida, 'players': Numero de jugadores,
# 'start_hour':Hora de inicio de artida ( datetime), 'rounds': Número de rondas, 'end_hour':
# hora final de partida ( datetime) }
#
# player_game = {id_game:{id_player_1:{initial_card_id:”card id”, starting_points:”puntos al
# inicio”, ending_points:”puntos al final de partida},...,id_player_n:{initial_card_id:”card id”,
# starting_points:”puntos al inicio”, ending_points:”puntos al final de partida}}”
#
# player_game_round = {round:{id_player_1:{is_bank:”0 ó 1”,bet_points:”apuesta en la
# ronda”,starting_round_points:”puntos al inicio de la partida,cards_value:”puntos
# obtenido en la actual ronda”,endind_round_points:”puntos al final de la
# ronda”},...,{id_player_n:{is_bank:”0 ó 1”,bet_points:”apuesta en la
# ronda”,starting_round_points:”puntos al inicio de la partida,cards_value:”puntos
# obtenido en la actual ronda”,endind_round_points:”puntos al final de la ronda”}


def menu_principal():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        opcion_ok = False
        opc = ''
        while not opcion_ok:
            print(menu00)
            opc = input(">Opcion: ")
            if not opc.isdigit():
                print("== Opcion Incorrecta!!! ===")
            elif int(opc) < 1 or int(opc) > 6:
                print("== Opcion Incorrecta!!! ===")
            else:
                opcion_ok = True
                opc = int(opc)
        if opc == 1:
            return menu_01()
        elif opc == 2:
            return menu_02()
        elif opc == 3:
            return play_game()
        elif opc == 4:
            menu_02()
        elif opc == 5:
            return reports()
        elif opc == 6:
            dejar_este_nivel = True


def menu_01():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        opcion_ok = False
        opc = ''
        while not opcion_ok:
            print(menu01)
            opc = input(">Opcion: ")
            if not opc.isdigit():
                print("== Opcion Incorrecta!!! ===")
            elif int(opc) < 1 or int(opc) > 4:
                print("== Opcion Incorrecta!!! ===")
            else:
                opcion_ok = True
                opc = int(opc)
        if opc == 1:
            return add_players()
        elif opc == 2:
            show_players()
            return remove_players()
        elif opc == 3:
            show_players()
            input("Press any key to continue:")
            return menu_01()
        elif opc == 4:
            menu_principal()


def add_players():
    type = add_players_type()
    name = add_players_name()
    NIF = add_players_nif(type)
    players[NIF] = {"name": name, "human": type, "bank": False, "initialCard": "", "priority": 0
        , "type": 40, "bet": 4, "points": 20, "cards": [], "roundPoints": 0}
    print("Player saved!")
    return menu_01()


def add_players_type():
    try:
        type = input("You want to add a real player? [y/n]")
        if type != "y" and type != "n":
            msj = "Write a correct option!"
            raise ValueError
    except ValueError:
        print(msj)
        return add_players_type()
    else:
        if type == "n":
            return False
        else:
            return True


def add_players_name():
    try:
        name = input("Player's name:")
        if not name or name.isspace():
            msj = "The name is null!"
            raise ValueError
    except ValueError:
        print(msj)
        return add_players_name()
    else:
        return name


def add_players_nif(type):
    if type is False:
        return create_nif()
    else:
        return import_nif()
        # Poner la funcion de comprobar el dni


def create_nif():
    number = random.randint(0, 100)
    NIF = "boot" + str(number)
    NIF = NIF.upper()
    if NIF in players:
        return create_nif()
    else:
        return NIF


def reports():
    a = input("Write your report here:")
    return logToFile(a)


def logToFile(text):
    f = open("logfileSevenAndHalf.txt", "a")
    f.write(text)
    f.close()
    print("Thanks for your report!")
    return menu_principal()


def import_nif():
    try:
        NIF = input("NIF of the player:")
        if len(NIF) != 9:
            msj = "Incorrect format!"
            raise ValueError
        if not NIF[:8].isdigit():
            msj = "The first 8 characters have to be numbers!"
            raise ValueError
        if NIF[8:].isdigit():
            msj = "The last character have to be a letter!"
            raise ValueError
        NIF = NIF.upper()
        d = int(NIF[:8])
        verificador = d % 23
        listadni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q",
                    "V", "H", "L",
                    "C", "K", "E"]
        if NIF[8:] != listadni[verificador]:
            msj = "Incorrect letter!"
            raise ValueError
    except ValueError:
        print(msj)
        return import_nif()
    else:
        return NIF


def remove_players():
    try:
        Remplay = input("NIF of the player to remove:")
        Remplay = Remplay.upper()
        if len(Remplay) == 0:
            raise AttributeError
        if Remplay not in players:
            msj = "INCORRECT NIF\nIf you don't want to eliminate any player press ENTER"
            raise ValueError
    except ValueError:
        print(msj)
        return remove_players()
    except AttributeError:
        return menu_01()
    else:
        players.pop(Remplay)
        print("Player removed!")
        return menu_01()


def show_players():
    cont = 0
    for i in players:
        cont = cont + 1
        print(" " * 16, f"Player {cont}", " " * 16)
        print("NIF".ljust(20), str(i).rjust(20))
        print("Name".ljust(20), str(players[i]["name"]).rjust(20))
        print("-" * 41)


def menu_02():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        opcion_ok = False
        opc = ''
        while not opcion_ok:
            print(menu02)
            opc = input(">Opcion: ")
            if not opc.isdigit():
                print("== Opcion Incorrecta!!! ===")
            elif int(opc) < 1 or int(opc) > 4:
                print("== Opcion Incorrecta!!! ===")
            else:
                opcion_ok = True
                opc = int(opc)
        if opc == 1:
            return set_game_players()
        elif opc == 2:
            return set_cards_deck()
        elif opc == 3:
            return set_max_rounds()
        elif opc == 4:
            menu_principal()


def set_game_players():
    if len(game) > 0:
        print("*" * 13, "Actual Players", "*" * 12)
        show_actual_players_real()
        try:
            opc = input("You want to add someone or eliminate any actual player?[a/e]\nPress ENTER to exit")
            if opc != "a" and opc != "e" and opc != "":
                msj = "Write a correct option!"
                raise ValueError
            if not opc:
                raise AssertionError
        except ValueError:
            print(msj)
            return set_game_players()
        except AssertionError:
            return menu_02()
        else:
            if opc == "a":
                return add_actual_players()
            if opc == "e":
                return eliminate_actual_player()
            else:
                return menu_02()
    else:
        print(f"There's  no player's. You have to add someone")
        return add_actual_players()


def add_actual_players():
    show_actual_players()
    if len(game) == 6:
        print("You can't add another player. The maximum is 6 players!")
        input("Press any key to continue:")
        return set_game_players()
    else:
        try:
            pl = input("NIF of the player that want to play:").upper()
            if pl not in players:
                msj = "Incorrect NIF!"
                raise ValueError
            if pl in game:
                msj = "That player is a actually player!"
                raise ValueError
        except ValueError:
            print(msj)
            return add_actual_players()
        else:
            game.append(pl)
            print("Player saved!")
            return question_another()


def question_another():
    try:
        opt = input("You want to add another?[y/n]")
        if opt != "y" and opt != "n":
            msj = "Incorrect option"
            raise ValueError
    except ValueError:
        print(msj)
        return question_another()
    else:
        if opt == "y":
            return add_actual_players()
        if opt == "n":
            return menu_principal()


def show_actual_players():
    actual_players = players.copy()
    for i in game:
        if i in actual_players:
            actual_players.pop(i)
    cont = 0
    if len(actual_players) == 0:
        print("There's no more players to add!")
        input("Press any key to continue:")
        return menu_principal()
    else:
        cont = 0
        for i in actual_players:
            cont = cont + 1
            print(" " * 16, f"Player {cont}", " " * 16)
            print("NIF".ljust(20), str(i).rjust(20))
            print("Name".ljust(20), str(players[i]["name"]).rjust(20))
            print("-" * 41)


def show_actual_players_real():
    cont = 0
    for i in game:
        cont = cont + 1
        print(" " * 16, f"Player {cont}", " " * 16)
        print("NIF".ljust(20), str(i).rjust(20))
        print("Name".ljust(20), str(players[i]["name"]).rjust(20))
        print("-" * 41)


def eliminate_actual_player():
    try:
        nif = input("NIF of the player that you want to eliminate:").upper()
        if nif not in game:
            msj = f"{nif} doesn't exist"
            raise ValueError
    except ValueError:
        print(msj)
        return eliminate_actual_player()
    else:
        game.pop(game.index(nif))
        print("Player eliminated!")
        if len(game) == 0:
            return menu_02()
        else:
            return question_another_eli()


def question_another_eli():
    try:
        opt = input("You want to eliminate another?[y/n]")
        if opt != "y" and opt != "n":
            msj = "Incorrect option"
            raise ValueError
    except ValueError:
        print(msj)
        return question_another()
    else:
        if opt == "y":
            return eliminate_actual_player()
        if opt == "n":
            return menu_02()


def set_max_rounds():
    print(f"Max Rounds: {rounds[0]}")
    try:
        op = input("Do you want to modificate?[y/n]")
        if op != "y" and op != "n":
            msj = "Incorrect Option"
            raise ValueError
    except ValueError:
        print(msj)
        return set_max_rounds()
    else:
        if op == "y":
            return modifycate_rounds()
        if op == "n":
            return menu_02()


def modifycate_rounds():
    try:
        round = input("Introduce the new maximun round:")
        if not round.isdigit():
            msj = "Only numbers!"
            raise ValueError
        round = int(round)
        if round <= 0:
            msj = "Introduce a valid number!"
            raise ValueError
    except ValueError:
        print(msj)
        return modifycate_rounds()
    else:
        print("Max Rounds modificate!")
        rounds.pop(0)
        rounds.append(round)
        return menu_02()


def set_cards_deck():
    opcion_ok = False
    opc = ''
    while not opcion_ok:
        print(menu_cards)
        opc = input(">Opcion: ")
        if not opc.isdigit():
            print("== Opcion Incorrecta!!! ===")
        elif int(opc) < 1 or int(opc) > 4:
            print("== Opcion Incorrecta!!! ===")
        else:
            opcion_ok = True
            opc = int(opc)
    if opc == 2:
        mazo.clear()
        mazo.append("Baraja de Poker")
        print("Card Deck's saved!")
        input("Press any key to continue:")
        return menu_principal()
    elif opc == 1:
        mazo.clear()
        mazo.append("Baraja Española")
        print("Card Deck's saved!")
        input("Press any key to continue:")
        return menu_principal()
    elif opc == 3:
        print_cards()
        input("Press any key to continue:")
        return set_cards_deck()
    elif opc == 4:
        return menu_02()


def print_cards():
    print("*" * 50)
    print(" " * 16, " Baraja Española")
    print("-" * 50)
    print("Type's of cards order by preference: ")
    print(" " * 16, "1.Oros\n", " " * 15, "2.Copas\n", " " * 15, "3.Espadas\n", " " * 15, "4.Bastos")
    print("." * 50)
    print(" " * 16, "Value literally:")
    print(" " * 16, "Card's 1-7")
    print("." * 50)
    print(" " * 16, "Value of 0.5:")
    print(" " * 16, "Sota\n", " " * 15, "Caballo\n", " " * 15, "Rey")
    print("*" * 50)
    print("")
    print("*" * 50)
    print(" " * 16, " Baraja Poker")
    print("-" * 50)
    print("Type's of cards order by preference: ")
    print(" " * 16, "1.Corazones\n", " " * 15, "2.Picas\n", " " * 15, "3.Treboles\n", " " * 15, "4.Naipes")
    print("." * 50)
    print(" " * 16, "Value literally:")
    print(" " * 16, "Card's 1-7")
    print("." * 50)
    print(" " * 16, "Value of 0.5:")
    print(" " * 16, "Ocho\n", " " * 15, "Nueve\n", " " * 15, "Diez\n", " " * 15, "Jota\n", " " * 15, "Reina\n",
          " " * 15, "Rey")
    print("*" * 50)


def play_game():
    if len(mazo) == 0:
        print("You have to select a Card's Deck first!")
        input("Press any key to continue:")
        return set_cards_deck()
    if len(game) < 2:
        print(f"You have to add minimun 2 players! There are added {len(game)} player/s.")
        input("Press any key to continue:")
        return add_actual_players()
    else:
        show_actual_players_real()
        contin = question_continue()
        if contin == "y":
            for i in game:
                if players[i]["human"] == True:
                    perfil_player(i)
                else:
                    players[i]["type"] = 40
            return priority_players()
        else:
            return menu_principal()


def perfil_player(i):
    f = players[i]["name"]
    print("\n" + " " * 20 + "Choose Type of player")
    print("*" * 24 + f"Player {f}" + "*" * 24 + "\n" + "1)Daring player \n2)Normal player  \n3)Prudent player")
    try:
        op = input("Option:")
        if not op.isdigit():
            msj = "Incorrect option!"
            raise ValueError
        op = int(op)
        if op != 1 and op != 2 and op != 3:
            msj = "Incorrect option!"
            raise ValueError
    except ValueError:
        print(msj)
        return perfil_player(i)
    else:
        if op == 1:
            players[i]["type"] = 50
            print("Saved!")
            input("Press any key to continue:")
            pass
        elif op == 2:
            players[i]["type"] = 40
            print("Saved!")
            input("Press any key to continue:")
            pass
        elif op == 3:
            players[i]["type"] = 30
            print("Saved!")
            input("Press any key to continue:")
            pass


def priority_players():
    print("*" * 10, "Priority and player roles", "*" * 10)
    input("Press ENTER to deal cards")
    for i in game:
        a = new_card()
        players[i]["cards"].append(a)
        print(players[i]["name"], "=", cartas[mazo[0]][a]["literal"])
    order_players()
    restart_cards()
    input("Press any key to continue:")
    bank_player()
    players_position()
    input("Press any key to continue:")
    return rounds_game()


def new_card():
    new = random.choice(list(cartas_real[mazo[0]]))
    del cartas_real[mazo[0]][new]
    return new


def restart_cards():
    for i in game:
        for j in players[i]["cards"]:
            cartas_real[mazo[0]][j] = cartas[mazo[0]][j]
        players[i]["cards"].clear()
    pass


def order_players():
    for pasada in range(
            len(game) - 1):
        for i in range(len(game) - 1 - pasada):
            if cartas[mazo[0]][players[game[i]]["cards"][0]]["value"] < \
                    cartas[mazo[0]][players[game[i + 1]]["cards"][0]][
                        "value"]:
                game[i], game[i + 1] = game[i + 1], game[i]
            if cartas[mazo[0]][players[game[i]]["cards"][0]]["value"] == \
                    cartas[mazo[0]][players[game[i + 1]]["cards"][0]][
                        "value"]:
                if cartas[mazo[0]][players[game[i]]["cards"][0]]["priority"] < \
                        cartas[mazo[0]][players[game[i + 1]]["cards"][0]][
                            "priority"]:
                    game[i], game[i + 1] = game[i + 1], game[i]
    pass


def bank_player():
    m = players[game[0]]["name"]
    players[game[0]]["priority"] = 1
    players[game[0]]["bank"] = True
    print("*" * 20, "Bank", "*" * 20)
    print(" " * 12, f"The bank is : {m}")
    print("*" * 46)
    input("Press any key to continue:")
    pass


def players_position():
    print("*" * 10, "Priority of players:", "*" * 10)
    m = players[game[0]]["name"]
    players[game[0]]["priority"] = len(game)
    for i in range(len(game[1:])):
        f = players[game[i + 1]]["name"]
        players[game[i + 1]]["priority"] = i + 1
        print(f"Position {i + 1}: {f}")
    print(f"Position {len(game)}: {m} ")
    pass


def rounds_game():
    count_rounds[0] = count_rounds[0] + 1
    context_game["round"] = count_rounds[0]
    if count_rounds[0] == rounds[0] or count_rounds[0] == 30 or len(game) == 1:
        return Game_Over()
    else:
        print("Time for bets")
        input("Press any key to continue:")
        for i in game[1:]:
            betofplayer(i)
        return rounds_starts()


def betofplayer(i):
    if players[i]["human"] == False:
        a = round(players[i]["points"] * (players[i]["type"] / 100))
        if a == 0:
            a = 1
        players[i]["bet"] = a
    else:
        f = players[i]["name"]
        print("*" * 10, f"Turn of {f}", "*" * 10)
        input("Press any key to continue:")
        pnts = players[i]["points"]
        print(f"Your points: {pnts}")
        bet = selectbet(i)
        players[i]["bet"] = bet
        print("Bet saved!")
        input("Press any key to continue:")
    pass


def selectbet(i):
    try:
        bet = input("Your bet:")
        if not bet.isdigit():
            msj = "Write a correct bet"
            raise ValueError
        bet = int(bet)
        if bet <= 0:
            msj = "Incorrect bet!"
            raise ValueError
        if bet > players[i]["points"]:
            msj = "You haven't this points!"
            raise ValueError
        if bet > players[game[0]]["points"]:
            msj = "The bank haven't this points."
            raise ValueError
    except ValueError:
        print(msj)
        return selectbet(i)
    else:
        return bet


def question_continue():
    try:
        op = input("These are the players, you want to continue?[y/n]")
        if op != "y" and op != "n":
            msj = "Incorrect option"
            raise ValueError
    except ValueError:
        print(msj)
        return question_continue()
    else:
        return op


def rounds_starts():
    print("*" * 40, "Dealing cards", "*" * 40)
    input("Press ENTER to deal cards")
    for i in game[1:]:
        players[i]["cards"].append(new_card())
        if players[i]["human"] == True:
            f = players[i]["name"]
            print("*" * 10, f"Turn of {f}", "*" * 10)
            input("Press any key to continue:")
            play_menu(i)
        else:
            play_automatic(i)
        li = []
        for j in players[i]["cards"]:
            li.append(cartas[mazo[0]][j]["realValue"])
        players[i]["roundPoints"] = sum(li)
    else:
        if players[game[0]]["human"] == False:
            return play_bank()
        else:
            print("*" * 20, "Turn of the bank", "*" * 20)
            input("Press any key to continue:")
            return play_bank_human()


def play_menu(i):
    f = players[i]["name"]
    b = players[i]["bet"]
    p = players[i]["points"]
    c = show_carts(i)
    print("\n" + "*" * 20 + f + "*" * 20)
    print("Your cards:")
    print(", ".join(map(str, c)))
    print("-" * 40)
    print(f"Your points: {p} points")
    print(f"Your bet: {b} points")
    print("-" * 40)
    print(
        "1)See your stats\n2)See the stats of all the players\n3)Change your bet\n4)PLay in automatic\n5)Get another card\n6)Finish")
    op = op_menu()
    if op == 1:
        print("See your stats FUNCION")
    elif op == 2:
        print("See the stats of all the players")
    elif op == 3:
        bet = selectbet(i)
        players[i]["bet"] = bet
        return play_menu(i)
    elif op == 4:
        players[i]["human"] = False
        pass
    elif op == 5:
        players[i]["cards"].append(new_card())
        return play_menu(i)
    elif op == 6:
        pass


def show_carts(j):
    l = []
    for i in range(len(players[j]["cards"])):
        l.append(cartas[mazo[0]][players[j]["cards"][i]]["literal"])
    return l


def op_menu():
    try:
        op = input("Option:")
        if not op.isdigit():
            msj = "Write a correct option!"
            raise ValueError
        op = int(op)
        if op != 1 and op != 2 and op != 3 and op != 4 and op != 5 and op != 6:
            msj = "Write a correct option!"
            raise ValueError
    except ValueError:
        print(msj)
        return op_menu()
    else:
        return op


def play_automatic(i):
    li = []
    cont = 0
    for j in players[i]["cards"]:
        li.append(cartas[mazo[0]][j]["realValue"])
    a = sum(li)
    for q in cartas_real[mazo[0]]:
        if cartas_real[mazo[0]][q]["realValue"] + a > 7.5:
            cont = cont + 1
    b = len(cartas_real[mazo[0]])
    res = (cont / b) * 100
    if res > players[i]["type"]:
        pass
    else:
        players[i]["cards"].append(new_card())
        return play_automatic(i)


def play_bank():
    i = game[0]
    players[i]["cards"].append(new_card())
    li = []
    for j in players[i]["cards"]:
        li.append(cartas[mazo[0]][j]["realValue"])
    players[i]["roundPoints"] = sum(li)
    if players[i]["human"] == False:
        if players[i]["roundPoints"] == 7.5:
            return results()
        if players[i]["roundPoints"] > 7.5:
            return results()
        else:
            if calc_bet() == 0:
                return results()
            if players[i]["points"] < calc_bet():
                return play_bank()
            if calc_winners() == 0:
                return play_bank()
            else:
                if card_bank(i) == True:
                    return play_bank()
                if card_bank(i) == False:
                    return results()


def card_bank(i):
    li = []
    cont = 0
    for j in players[i]["cards"]:
        li.append(cartas[mazo[0]][j]["realValue"])
    a = sum(li)
    for q in cartas_real[mazo[0]]:
        if cartas_real[mazo[0]][q]["realValue"] + a > 7.5:
            cont = cont + 1
    b = len(cartas_real[mazo[0]])
    res = (cont / b) * 100
    if res > players[i]["type"]:
        return False
    else:
        return True


def calc_bet():
    l = []
    for i in game[1:]:
        if players[game[0]]["roundPoints"] < players[i]["roundPoints"]:
            l.append(players[i]["bet"])
    a = sum(l)
    return a


def calc_winners():
    con = 0
    for i in game[1:]:
        if players[game[0]]["roundPoints"] > players[i]["roundPoints"]:
            con = con + 1
    return con


def play_bank_human():
    i = game[0]
    players[i]["cards"].append(new_card())
    li = []
    for j in players[i]["cards"]:
        li.append(cartas[mazo[0]][j]["realValue"])
    a = sum(li)
    players[i]["roundPoints"] = a
    print("Players cards:")
    for j in game[1:]:
        print("-" * 40)
        name = players[j]["name"]
        bet = players[j]["bet"]
        cds = show_carts(j)
        print("name:", name)
        print("bet:", bet)
        print("cards:", ", ".join(map(str, cds)))
        print("-" * 40)
    p = players[i]["points"]
    c = show_carts(i)
    print("Your cards:")
    print(", ".join(map(str, c)))
    print("-" * 40)
    print(f"Your points: {p} points")
    print("-" * 40)
    print("\n1)Finish\n2)Get another card")
    op = op_bank()
    if op == 2:
        return play_bank_human()
    if op == 1:
        return results()


def op_bank():
    try:
        op = input("Option:")
        if not op.isdigit():
            msj = "Write a correct option!"
            raise ValueError
        op = int(op)
        if op != 1 and op != 2:
            msj = "Write a correct option!"
            raise ValueError
    except ValueError:
        print(msj)
        return op_bank()
    else:
        return op


def results():
    if players[game[0]]["roundPoints"] > 7.5:
        for i in game[1:]:
            if players[i]["roundPoints"] > 7.5:
                players[i]["bet"] = -(players[i]["bet"])
            else:
                if players[i]["roundPoints"] == 7.5:
                    players[i]["bet"] = (players[i]["bet"]) * 2
                else:
                    players[i]["bet"] = players[i]["bet"]
    elif players[game[0]]["roundPoints"] == 7.5:
        for i in game[1:]:
            players[i]["bet"] = -(players[i]["bet"])
    else:
        for i in game[1:]:
            if players[i]["roundPoints"] > 7.5:
                players[i]["bet"] = -(players[i]["bet"])
            elif players[i]["roundPoints"] == 7.5:
                players[i]["bet"] = (players[i]["bet"]) * 2
            else:
                if players[game[0]]["roundPoints"] > players[i]["roundPoints"]:
                    players[i]["bet"] = -(players[i]["bet"])
                else:
                    players[i]["bet"] = players[i]["bet"]
    return payments()


def payments():
    a = calc_totalpoints()
    if a > players[game[0]]["points"]:
        for i in game[1:]:
            if players[i]["bet"] > players[game[0]]["points"]:
                players[i]["points"] = players[i]["points"] + players[game[0]]["points"]
                players[game[0]]["points"] = 0
            else:
                players[i]["points"] = players[i]["points"] + players[i]["bet"]
                players[game[0]]["points"] = players[game[0]]["points"] - (players[i]["bet"])
    else:
        for i in game[1:]:
            players[i]["points"] = players[i]["points"] + players[i]["bet"]
            players[game[0]]["points"] = players[game[0]]["points"] - (players[i]["bet"])
        return show_payments()


def calc_totalpoints():
    l = []
    for i in game[1:]:
        l.append(players[i]["bet"])
    a = sum(l)
    return a


def show_payments():
    print("*" * 40, "Results", "*" * 40)
    input("Press ENTER to see the results")
    for i in game[1:]:
        print("-" * 40, players[i]["name"], "-" * 40)
        print("*" * 20, "Bank cards", "*" * 20)
        for j in players[game[0]]["cards"]:
            print(cartas[mazo[0]][j]["literal"])
        print("*" * 20, "Your cards", "*" * 20)
        for q in players[i]["cards"]:
            print(cartas[mazo[0]][q]["literal"])
        if players[i]["bet"] > 0:
            print("You win", players[i]["bet"], "points!")
        else:
            print("You lose", -(players[i]["bet"]), "points!")
        input("Press any key to continue:")
    return final_round()


def final_round():
    print("*" * 20, "Puntuations", "*" * 20)
    for i in game:
        print("-" * 53)
        print("Name:", str(players[i]["name"]).rjust(47))
        print("Points:", str(players[i]["points"]).rjust(45))
        print("-" * 53)
    input("Press any key to continue:")
    for j in game:
        if players[j]["points"] <= 0:
            player_eliminated(j)
    return new_bank()


def player_eliminated(i):
    f = players[i]["name"]
    print("*" * 40, "GAME OVER", "*" * 40)
    print(f"Player {f} was eliminated!")
    print("-" * 90)
    input("Press any key to continue:")
    players[i]["points"] = 20
    players[i]["bet"] = 4
    players[i]["bank"] = False
    players[i]["priority"] = 0
    players[i]["cards"].clear()
    game.remove(i)
    if len(game) == 1:
        return Game_Over()
    else:
        pass


def new_bank():
    if players[game[0]]["bank"] == False:
        for i in game:
            if players[i]["roundPoints"] == 7.5:
                game.remove(i)
                game.insert(0, i)
                break
    else:
        players[game[0]]["bank"] = False
        c = 0
        for i in game[1:]:
            if players[i]["roundPoints"] == 7.5:
                game.remove(i)
                game.insert(0, i)
                k = game[1]
                game.remove(k)
                game.append(k)
                c = 1
                break
        if c == 0:
            q = game[0]
            game.remove(q)
            game.append(q)

    players[game[0]]["bank"] = True
    m = players[game[0]]["name"]
    print("*" * 20, "New Bank", "*" * 20)
    print(" " * 12, f"The bank is : {m}")
    print("*" * 50)
    return rounds_game()


def restart_game():
    restart_cards()
    print("*" * 20, "New round", "*" * 20)
    input("Press ENTER to start a new round")
    return new_bank()


def Game_Over():
    s1 = ("                                                                                               ")
    s2 = ("     _/_/_/                                            _/_/                                    ")
    s3 = ("  _/          _/_/_/  _/_/_/  _/_/      _/_/        _/    _/  _/      _/    _/_/    _/  _/_/   ")
    s4 = (" _/  _/_/  _/    _/  _/    _/    _/  _/_/_/_/      _/    _/  _/      _/  _/_/_/_/  _/_/        ")
    s5 = ("_/    _/  _/    _/  _/    _/    _/  _/            _/    _/    _/  _/    _/        _/           ")
    s6 = (" _/_/_/    _/_/_/  _/    _/    _/    _/_/_/        _/_/        _/        _/_/_/  _/            ")
    s7 = ("                                                                                               ")
    print(s1, "\n", s2, "\n", s3, "\n", s4, "\n", s5, "\n", s6, "\n", s7)
    print("-" * 95)
    if count_rounds[0] == rounds[0] or count_rounds[0] == 30:
        print("The maximum rounds have been reached")
        if len(game) > 1:
            for i in game:
                for pasada in range(
                        len(game) - 1):
                    for i in range(len(game) - 1 - pasada):
                        if players[game[i]]["points"] < \
                                players[game[i + 1]]["points"]:
                            game[i], game[i + 1] = game[i + 1], game[i]
    print("The winner is", players[game[0]]["name"])
    print("Congratulations!")
    input("Press ENTER to finish the game")


def capcelera():
    s1 = (
        "   _|_|_|                                                                          _|      _|    _|            _|      _|_|")
    s2 = (
        "_|          _|_|    _|      _|    _|_|    _|_|_|          _|_|_|  _|_|_|      _|_|_|      _|    _|    _|_|_|  _|    _|      ")
    s3 = (
        "  _|_|    _|_|_|_|  _|      _|  _|_|_|_|  _|    _|      _|    _|  _|    _|  _|    _|      _|_|_|_|  _|    _|  _|  _|_|_|_|  ")
    s4 = (
        "      _|  _|          _|  _|    _|        _|    _|      _|    _|  _|    _|  _|    _|      _|    _|  _|    _|  _|    _|      ")
    s5 = (
        "_|_|_|      _|_|_|      _|        _|_|_|  _|    _|        _|_|_|  _|    _|    _|_|_|      _|    _|    _|_|_|  _|    _|      ")
    s6 = ("")
    print(s1, "\n", s2, "\n", s3, "\n", s4, "\n", s5, "\n", s6)
    print("-" * 124)


menu_principal()
