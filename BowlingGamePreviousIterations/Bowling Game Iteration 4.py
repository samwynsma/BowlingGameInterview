# Fourth iteration of the bowling game.
# First Change: Added a basic score display feature.

class Bowling():

    frame_scores = []
    rolls = []
    invalid_input_reason = ""
    
    def __init__(self):
        print("New game: let's play")


    def add_throw(self, throw):
        if type(throw) == str:
            throw = throw.upper()
            
        if self.is_game_over():
            print("The game is already over. No more rolls")
        elif self.is_valid_input(throw):
            self.rolls.append(throw)
            print("Score added to game")
            if self.is_game_over():
                print("Game Over")
                print("Rolls: " + str(self.rolls))
                self.bowling_score()
                print("Frame Results: " + str(self.frame_scores))
                print("Final Score: " + str(self.bowling_score()))
        else:
            print("Invalid input: " + self.invalid_input_reason)


    def bowling_score(self):
        self.frame_scores = []
        frame = 1
        score = 0
        frameScore = 0
        firstBall = True
        for i in range(len(self.rolls)):
            if self.rolls[i] == 'X':
                score += 10
            elif self.rolls[i] == '/':
                score += (10 - self.rolls[i-1])
            else:
                score += self.rolls[i]
            if not frame == 10:
                if firstBall:
                    if self.rolls[i] == 'X':
                        if(i+1 < len(self.rolls)):
                            if self.rolls[i+1] == 'X':
                                score += 10
                            else:
                                score += self.rolls[i+1]
                        if(i+2 < len(self.rolls)):
                            if self.rolls[i+2] == 'X':
                                score += 10
                            elif self.rolls[i+2] == '/':
                                score += (10 - self.rolls[i+1])
                            else:
                                score += self.rolls[i+2]
                        frame += 1
                    else:
                        firstBall = False
                        frameScore += self.rolls[i]
                else:
                    frame += 1
                    firstBall = True
                    if self.rolls[i] == '/':
                        if(i+1 < len(self.rolls)):
                            if self.rolls[i+1] == 'X':
                                score += 10
                            else:
                                score += self.rolls[i+1]
                    frameScore = 0
            self.frame_scores.append(score)
        return score


    def is_game_over(self):
        frame_count = 0
        first_ball = True
        final_frame_third_ball = False
        for i in range(len(self.rolls)):
            if first_ball:
                if self.rolls[i] == 'X' and frame_count != 9:
                    frame_count += 1
                else:
                    first_ball = False
            elif frame_count == 9 and first_ball == False and final_frame_third_ball == False:
                if self.rolls[i-1] == 'X' or self.rolls[i] == '/':
                    final_frame_third_ball = True
                else:
                    frame_count += 1
            else:
                frame_count += 1
        if frame_count == 10:
            return True
        return False


    def is_valid_input(self, roll):
        first_ball = True
        frame_score = 0
        for i in range(len(self.rolls)):
            if first_ball:
                if self.rolls[i] == 'X':
                    frame_score = 0
                else:
                    first_ball = False
                    frame_score = self.rolls[i]
            else:
                first_ball = True
                frame_score = 0
        
        if type(roll) is int:
            if roll > 10:
                self.invalid_input_reason = "Number must be below 10. For a ten pin roll, type \'X\'"
                return False
            elif roll == 10:
                self.invalid_input_reason = "Use \'X\', not 10, for a strike."
                return False
            elif roll < 0:
                self.invalid_input_reason = "Cannot hit a negative number of pins."
                return False
            elif roll + frame_score > 10:
                self.invalid_input_reason = "Cannot hit more pins than there are pins left."
                return False
            elif roll + frame_score == 10:
                self.invalid_input_reason = "Use \'/\' for a spare, not the remaining number of pins."
                return False
        elif type(roll) is str:
            if roll == 'X':
                if not first_ball:
                    self.invalid_input_reason = "Strikes are not possible on the second throw."
                    return False
            elif roll == '/':
                if first_ball:
                    self.invalid_input_reason = "Spares are not possible on the first throw."
                    return False
            else:
                self.invalid_input_reason = "Invalid string input."
                return False
        else:
            self.invalid_input_reason = "Invalid input. Only strings and ints are allowed."
            return False
        return True


    def reset_game(self):
        print("Game has been reset. All scores have been removed.")
        self.frame_scores = []
        self.rolls = []
        self.invalid_input_reason = ""

    def display_score(self):
        self.bowling_score()
        score_strings = []
        frame_count = 0
        first_ball = True
        first_score_line = ""
        for i in range(10):
            first_score_line += str(i)
        score_strings.append(first_score_line)
        second_score_line = ""
        for i in range(len(self.rolls)):
            if frame_count < 9:
                if self.rolls[i] == 'X':
                    second_score_line += "X|_"
                else:
                    second_score_line += str(self.rolls[i])
                    if first_ball:
                        first_ball = False
                        second_score_line += "|"
                    else:
                        first_ball = True
            else:
                second_score_line += str(self.rolls[i])
                second_score_line += "|"
                second_score_line += str(self.rolls[i+1])
                if self.rolls[i+2] == len(self.rolls):
                    second_score_line += "|_"
                else:
                    second_score_line += "|"
                    second_score_line += str(self.rolls[i+2])
        if frame_count != 10:
            second_score_line += "\u2588"
        score_strings.append(second_score_line)
        score_strings.append(str(self.frame_scores))
        print(first_score_line)
        print(second_score_line)
        print(score_strings[2])
        return score_strings

testGame = Bowling()
testGame.add_throw('X')
testGame.add_throw(15)
testGame.add_throw(-1)
testGame.add_throw(10)
testGame.add_throw('/')
testGame.add_throw("Strike")
testGame.add_throw(['X', 'X'])
testGame.add_throw('x')
testGame.display_score()
testGame.add_throw('X')
testGame.add_throw('X')
testGame.add_throw('X')
testGame.add_throw('X')
testGame.add_throw('X')
testGame.add_throw('X')
testGame.add_throw('X')
testGame.add_throw(3)
testGame.add_throw(7)
testGame.display_score()
testGame.add_throw(8)
testGame.add_throw('X')
testGame.add_throw('/')
testGame.add_throw(7)
testGame.add_throw('X')
testGame.reset_game()
testGame.add_throw('X')
testGame.add_throw('X')
print(testGame.rolls)
