POINTSDICT = {0: 0, 1: 15, 2: 30, 3: 40, 4: "40+adv", 5: "40+adv+adv"}
MIN_POINTS_REQ_TO_WIN = 4
MIN_DIFF_REQ = 2
MIN_GAMES_REQ_TO_WIN = 6
PLAYER_A = 'A'
PLAYER_B = 'B'


def printDict(dictionary: dict) -> str:
    return ''.join(str(dictionary[i])+' ' for i in dictionary)


def updateScores(points: dict, scores: dict, player1: str, player2: str):
    scores[player1] = POINTSDICT[points[player1]]
    scores[player2] = POINTSDICT[points[player2]]
    return scores


def updateSetWin(games: dict, sets: dict, player1: str, player2: str):
    if (games[player1] > MIN_GAMES_REQ_TO_WIN and games[player2] == 6) or games[player1]-games[player2] >= MIN_DIFF_REQ:
        sets[player1] += 1
        games[player1] = games[player2] = 0
    return games, sets


def updateGameWin(points: dict, games: dict, sets: dict, player1: str, player2: str):
    if points[player1] == MIN_POINTS_REQ_TO_WIN and points[player2] == MIN_POINTS_REQ_TO_WIN:
        points[player1] = points[player2] = MIN_POINTS_REQ_TO_WIN-1
    if points[player1]-points[player2] >= MIN_DIFF_REQ:
        games[player1] += 1
        if games[player1] >= MIN_GAMES_REQ_TO_WIN:
            games, sets = updateSetWin(games, sets, player1, player2)
        points[player1] = points[player2] = 0
    return points, games


def updatePoints(points: dict, games: dict, sets: dict, player1: str, player2: str) -> dict:
    points[player1] += 1
    if points[player1] >= MIN_POINTS_REQ_TO_WIN:
        return updateGameWin(points, games, sets, player1, player2)
    return points, games


def otherPlayer(player: str) -> str:
    return PLAYER_B if player == PLAYER_A else PLAYER_A


def tennis(s):
    points = {PLAYER_A: 0, PLAYER_B: 0}
    scores = {PLAYER_A: 0, PLAYER_B: 0}
    games = {PLAYER_A: 0, PLAYER_B: 0}
    sets = {PLAYER_A: 0, PLAYER_B: 0}
    for player in s:
        points, games = updatePoints(
            points, games, sets, player, otherPlayer(player))
        scores = updateScores(points, scores,
                              player, otherPlayer(player))
    return "Players : A B"+"\nSets : "+printDict(sets)+"\nGames : " + printDict(games)+"\nPoints : "+printDict(scores)


print(tennis('ABABABABAAA'))
