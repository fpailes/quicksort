

letters = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
points = [1,3,3,2,1,4,2,4,1,8,5,1,3,4,1,3,10,1,1,1,1,4,4,8,4,10]

letter_to_points = dict(zip(letters, points))

letter_to_points[" "] = 0
print(letter_to_points)

for letter in letters:
    if letter != letter.lower():
        letters.append(letter.lower())


def score_word(word):
    point_total = 0
    for letter in word:
       if letter in word:
            point_total += letter_to_points[letter]
    return point_total


brownie_points = score_word("BROWNIE")

print(str(score_word("HELLO")))
print(brownie_points)

player_to_words = { "player1" : ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con" : ["ERASER", "BELLY", "HUSKY"], "Prof Reader" : ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

def player_score(player):
    player_points = 0
    for word in player:
        player_points += score_word(word)
    return player_points

def game_score(players):
    for player in players:
        player_to_points[player] = player_score(players[player])
    return player_to_points

print(game_score(player_to_words))

def play_word(player, word):
    player_to_words[player].append(word)
