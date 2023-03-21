def bowling_score(rolls):
    frame = 1
    score = 0
    frameScore = 0
    firstBall = True
    for i in range(len(rolls)):
        score += rolls[i]
        if not frame == 10:
            if firstBall:
                if rolls[i] == 10:
                    if(i+1 < len(rolls)):
                        score += rolls[i+1]
                    if(i+2 < len(rolls)):
                        score += rolls[i+2]
                    frame += 1
                else:
                    firstBall = False
                    frameScore += rolls[i]
            else:
                frame += 1
                firstBall = True
                if rolls[i] + frameScore == 10:
                    if(i+1 < len(rolls)):
                        score += rolls[i+1]
                frameScore = 0
    return score

print(bowling_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
print(bowling_score([9,1, 9,1, 9,1, 9,1, 9,1, 9,1, 9,1, 9,1, 9,1, 9,1, 9]))
print(bowling_score([10, 10, 0, 10, 0, 10]))
