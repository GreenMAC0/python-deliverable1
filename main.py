# STEP 1 prompt user for their name.
name = input("Welcome to GC mini golf! What is your name?")
# STEP 2Next prompt the user if they would like to play 3 or 6 holes of mini golf.
holes = int(input("Hi," + name +"! Would you like to play 3 or 6 holes today? "))
# STEP 3 Finally, prompt the user either 3 times or 6 times (depending on their input for the second prompt) for each "hole of golf" asking for the number of putts for that specific hole.
cumulative_score = 0
total_par = holes * 3

for i in range(holes):
    putts = int(input(f"how many putts for hole {i +1} (par:3)"))
    cumulative_score += putts
# STEP 4 Keep track of their cumulative score (total number of putts) and, at the end, compare that to the total course par (9 if they chose 3 holes, 18 if they chose 6 — par is 3 for every hole) to calculate the golfer’s total par for the round.
total_score = cumulative_score - total_par

# STEP 5 After the last hole, one of three messages is printed to the console depending on if the user was over, under or on par for the round:
# print("your score is:" + str(cumulative_score))
# STEP 6 If over par, the message should read "Nice try, (name)... Your total score was: +(par)." [be sure to include the plus symbol here to denote over par].
if total_score > 0:
    print("Nice try," + name + "... Your total score was: +" + str(total_score) + ".")
# STEP 7 If under par, the message should read "Great job, (name)! Your total score was: -(par)." [include the minus symbol]
elif total_score < 0:
    print("Great job," + name + ". Your total score was: -" + str(total_score) + ".")
# STEP 8 If even with par, the message should read "Good game, (name). Your total score was: 0."
else: print("Good game," + name + ". Your total score was: 0.")
