import itertools


def gradeOneGuessAndAnswer(inputs, answer):
    # Grades a single guess against a single answer. Returns a single int - score (1 value)
    score = 0
    inarow = False
    corrects = []

    for x in range(len(answer)):
        if (inputs[x] == answer[x]):
            corrects.append(True)
        else:
            corrects.append(False)
        if (len(corrects) > 2):
            if (corrects[x] and corrects[x-1] and corrects[x-2]):
                inarow = True

    correctcount = corrects.count(True)
    if (correctcount > 3 or correctcount > 2 and inarow):
        score = correctcount

    return score


def gradeOneGuessAndManyAnswers(inputs, answers):
    # Grades a single answer against all answers. Returns a list of scores (8 values)
    scores = []

    for ans in answers:
        scores.append(gradeOneGuessAndAnswer(inputs, ans))

    return scores


def gradeAllGuesses(guesses, answers):
    # Grades all guesses against all answers. Returns list of list of scores (64 values). anslist[guesslist[score]]
    scores = []

    for guess in guesses:
        scores.append(gradeOneGuessAndManyAnswers(guess, answers))

    return scores


def setBestMatrix(scoreslist):
    # Iterates through the list of list of scores to find the best combination of scores using exactly one score per answer. Returns a list of tuples in the format of (index_of_answer, score_for_that_answer);
    # *The list of tuples is ordered in order of guess index (ie. the first item in the returned tuplelist relates to guess 1, etc.)

    tuplelist = []
    highscore = 0
    highcombo = []

    permutations = set(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7]))

    for p in permutations:
        score = 0

        for x in range(len(p)):
            score = score + scoreslist[x][p[x]]

        if (score > highscore):
            highscore = score
            highcombo = p

    # By this point, should have the highest total score and the permutation that found it. need to return a list of tuples in format: [(guessindex, guessscore)]
    for x in range(len(highcombo)):
        tuplelist.append((x, scoreslist[x][highcombo[x]]))

    if (highscore == 0):
        tuplelist = [(0, 0), (1, 0), (2, 0), (3, 0),
                     (4, 0), (5, 0), (6, 0), (7, 0)]

    return tuplelist


def SolveEquation(guesses, answers):
    scoreslist = gradeAllGuesses(guesses, answers)
    return setBestMatrix(scoreslist)
