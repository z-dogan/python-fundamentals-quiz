def menu():
    print("\n1-Take the Quiz\n2-View History and Highest Score\n3-Exit")


quiz = {
    "What keyword is used to define a function in Python?": "def",
    "Which built-in function returns the number of items in a list or string?": "len",
    "What boolean value does the comparison (5 == 5) return?": "true",
    "Which loop structure repeats as long as a condition remains True?": "while",
    "What symbol is used to indicate a single-line comment in Python?": "#",
}

questions = list(quiz.keys())
answers = list(quiz.values())
score_hist = []

while True:
    menu()
    missed = []
    total_score = 0

    try:
        option = int(input("Please choose an option:"))
        if option == 1:
            for q in questions:
                a = answers[questions.index(q)]
                print(q)
                guess = input("Please write your answer:")
                guess1 = guess.strip().lower()
                if guess1 == a:
                    total_score += 1
                else:
                    missed.append([q, a])

            score_hist.append(total_score)

            print("\nRESULTS")
            print("Your total score:", total_score)

            percentage = (total_score * 100) / 5
            if percentage == 100:
                print("\nYour grade: A+")
            else:
                print("Correct answers for missed questions:")
                for m in missed:
                    print(m)
                if percentage == 0:
                    print("\nYour grade: F")
                elif percentage == 20:
                    print("\nYour grade: D")
                elif percentage == 40:
                    print("\nYour grade: C")
                elif percentage == 60:
                    print("\nYour grade: B")
                elif percentage == 80:
                    print("\nYour grade: A")
        if option == 2:
            if len(score_hist) == 0:
                print("\nNo quiz history yet.")
            else:
                print("\nScore history:")
                for h in score_hist:
                    print(h)
                print("Highest score:", max(score_hist))

        if option == 3:
            print("You exited.")
            break

    except ValueError:
        print("\nYou should enter a number.")
