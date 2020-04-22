POINTSDICT = {0: 'love', 1: 15, 2: 30, 3: 40, 4: '40+adv', 5: '40+adv+adv'}
MIN_POINTS_REQ_TO_WIN = 4
MIN_DIFF_REQ = 2
MIN_GAMES_REQ_TO_WIN = 6
PLAYER_A = 'A'
PLAYER_B = 'B'


def updateScores(points, scores, player1, player2):
    scores[player1] = POINTSDICT[points[player1]]
    scores[player2] = POINTSDICT[points[player2]]
    return scores


def updateSetWin(games, sets, player1, player2):
    if (games[player1] > MIN_GAMES_REQ_TO_WIN and games[player2] == MIN_GAMES_REQ_TO_WIN) or games[player1]-games[player2] >= MIN_DIFF_REQ:
        sets[player1] += 1
        games[player1] = games[player2] = 0
    return games, sets


def updateGameWin(points, games, sets, player1, player2):
    if points[player1] == MIN_POINTS_REQ_TO_WIN and points[player2] == MIN_POINTS_REQ_TO_WIN:
        points[player1] = points[player2] = MIN_POINTS_REQ_TO_WIN-1
    if points[player1]-points[player2] >= MIN_DIFF_REQ:
        games[player1] += 1
        if games[player1] >= MIN_GAMES_REQ_TO_WIN:
            games, sets = updateSetWin(games, sets, player1, player2)
        points[player1] = points[player2] = 0
    return points, games


def updatePoints(points, games, sets, player1, player2):
    points[player1] += 1
    if points[player1] >= MIN_POINTS_REQ_TO_WIN:
        return updateGameWin(points, games, sets, player1, player2)
    return points, games


def tennis(s):
    points = [0, 0]
    scores = [0, 0]
    games = [0, 0]
    sets = [0, 0]
    currentPlayerIndex = 0
    for player in s:
        currentPlayerIndex = 0 if player == PLAYER_A else 1
        points, games = updatePoints(
            points, games, sets, currentPlayerIndex, abs(currentPlayerIndex-1))
        scores = updateScores(points, scores,
                              currentPlayerIndex, abs(currentPlayerIndex-1))
    return "Players : A B"+"\nSets : "+str(sets)+"\nGames : " + str(games)+"\nPoints : "+str(scores)


print(tennis('ABABABABAAA'))
