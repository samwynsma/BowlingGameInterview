# Second iteration of the bowling game.
# First change: bowling is now a class and can play like a game.
# Second change: frame scores can now be accessed at any time
# Third change: rolls can now be accessed at any time
# Fourth change: throws can now be added to bowling game
# Fifth change: Game Over has now been implemented

class Bowling():

    frame_scores = []
    rolls = []
    def __init__(self):
        print("New game: let's play")

    def add_throw(self, item):
        if self.is_game_over():
            print("The game is already over. No more rolls")
        else:
            self.rolls.append(item)
            print("Score added to game")
            if self.is_game_over():
                print("Game Over")
                print("Rolls: " + str(self.rolls))
                self.bowling_score()
                print("Frame Results: " + str(self.frame_scores))
                print("Final Score: " + str(self.bowling_score()))

    def bowling_score(self):
        self.frame_scores = []
        frame = 1
        score = 0
        frameScore = 0
        firstBall = True
        for i in range(len(self.rolls)):
            score += self.rolls[i]
            if not frame == 10:
                if firstBall:
                    if self.rolls[i] == 10:
                        if(i+1 < len(self.rolls)):
                            score += self.rolls[i+1]
                        if(i+2 < len(self.rolls)):
                            score += self.rolls[i+2]
                        frame += 1
                    else:
                        firstBall = False
                        frameScore += self.rolls[i]
                else:
                    frame += 1
                    firstBall = True
                    if self.rolls[i] + frameScore == 10:
                        if(i+1 < len(self.rolls)):
                            score += self.rolls[i+1]
                    frameScore = 0
            self.frame_scores.append(score)
        return score

    def is_game_over(self):
        frame_count = 0
        first_ball = True
        for i in range(len(self.rolls)):
            if first_ball:
                if self.rolls[i] == 10:
                    frame_count += 1
                else:
                    first_ball = False
            else:
                frame_count += 1
        if frame_count == 10:
            return True
        return False

testGame = Bowling()
testGame.add_throw(10)
testGame.add_throw(3)
testGame.add_throw(3)
testGame.add_throw(3)
testGame.add_throw(3)
testGame.add_throw(5)
testGame.add_throw(3)
testGame.add_throw(10)
testGame.add_throw(10)
testGame.add_throw(10)
testGame.add_throw(10)
testGame.add_throw(10)
testGame.add_throw(10)
testGame.add_throw(10)
testGame.add_throw(10)
