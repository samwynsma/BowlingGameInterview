# Fifth Iteration of the bowling game
# First Change: Added basic user interface
# Second Change: Altered display_score in bowling so it gives a list of strings for usage in labels later.
# Third Change: Added basic display of frame numbers, frame data, and scores
# Fourth Change: Fixed major bug with score calculation. First balls no longer add to frame.
# Fifth Change: Added score display and reset button to main display.


import tkinter as tk

class Bowling_Interface(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.bowling_game = Bowling()
            
        self.prompt = tk.Label(self, text = "Enter a score:")
        self.frame_numbers = tk.Label(self, text = "")
        self.frame_data = tk.Label(self, text = "")
        self.frame_scores = tk.Label(self, text = "")
        self.enter_score = tk.Entry(self)
        self.submit = tk.Button(self, text = "Enter Score", command = self.submit_score)
        self.score_output = tk.Label(self, text = "Score: ")
        self.reset_game = tk.Button(self, text = "Reset Game", command = self.reset)

        self.frame_numbers.pack(fill="x")
        self.frame_data.pack(fill="x")
        self.frame_scores.pack(fill="x")
        self.prompt.pack(fill="x")
        self.enter_score.pack(fill="x", padx = 20)
        self.submit.pack(fill ="x")
        self.score_output.pack(fill="x", anchor=tk.S)
        self.reset_game.pack(fill="x", anchor=tk.S)

        self.submit_score()
        

    def submit_score(self):

        throw = self.enter_score.get()

        try:
            throw = int(throw)
        except ValueError:
            print("String input")

        self.bowling_game.add_throw(throw)
        self.score_output.configure(text = "Score: " + str(self.bowling_game.bowling_score()))
        scoring_information = self.bowling_game.display_score()
        frame_string = ""
        scores_string = ""
        numbers_string = ""
        for item in scoring_information[0]:
            frame_string += f"{item:^10}"
        for item in scoring_information[1]:
            scores_string += f"{item:^10}"
        for i in range(len(scoring_information[1]), 10):
            scores_string += f"{' ':^10}"
        for item in scoring_information[2]:
            numbers_string += f"{item:^10}"
        for i in range(len(scoring_information[2]), 10):
            numbers_string += f"{' ':^10}"
            
        self.frame_numbers.configure(text = frame_string)
        self.frame_data.configure(text = scores_string)
        self.frame_scores.configure(text = numbers_string)

    def reset(self):
        self.bowling_game.reset_game()
        self.score_output.configure(text = self.bowling_game.bowling_score())

    
class Bowling():

    def __init__(self):
        print("New game: let's play")
        self.frame_scores = []
        self.rolls = []
        self.invalid_input_reason = ""


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
                        self.frame_scores.append(score)
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
            if i+1 >= len(self.rolls):
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
                first_ball = True
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
            first_score_line += str(i+1)
            first_score_line += " "
        score_strings.append(first_score_line.split(" "))
        second_score_line = ""
        for i in range(len(self.rolls)):
            if frame_count < 9:
                if self.rolls[i] == 'X':
                    second_score_line += "X|_ "
                    frame_count += 1
                else:
                    second_score_line += str(self.rolls[i])
                    if first_ball:
                        first_ball = False
                        second_score_line += "|"
                    else:
                        second_score_line += " "
                        first_ball = True
                        frame_count += 1
            else:
                second_score_line += str(self.rolls[i])
                second_score_line += "|"
                if i+1 >= len(self.rolls):
                    break
                else:
                    second_score_line += str(self.rolls[i+1])
                if i+2 >= len(self.rolls):
                    second_score_line += "|_"
                else:
                    second_score_line += "|"
                    second_score_line += str(self.rolls[i+2])
                frame_count += 1
                break
            
        if frame_count != 10:
            second_score_line += "\u2588"
        score_strings.append(second_score_line.split(" "))
        score_strings.append(self.frame_scores)
        print(score_strings[0])
        print(score_strings[1])
        print(score_strings[2])
        return score_strings

if __name__ == "__main__":   
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
    testGame.display_score()
    testGame.reset_game()
    testGame.add_throw('X')
    testGame.add_throw('X')
    print(testGame.rolls)

    root = tk.Tk()
    Bowling_Interface(root).pack(fill="both", expand = True)
    root.mainloop()
