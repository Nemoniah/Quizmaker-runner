file_name = input("Enter the name of the file: ")
if file_name[-4:] != ".txt":
    file_name += ".txt"

question_string = ""
run_again_list = ["YES"]
not_run_again_list = ["NO", "QUIT"]
answer_letter_list = ["A", "B", "C"]

while True:
    correct_letter = ""
    upper_correct_letter = ""
    run_again = ""
    points = ""

    question = input("Enter the question: ")
    answers = ["A." + input("Enter answer A: "), "B." + input("Enter answer B: "), "C." + input("Enter answer C: ")]

    while upper_correct_letter not in answer_letter_list:
        correct_letter = input("Enter the letter corresponding to the correct answer: ")
        upper_correct_letter = correct_letter.upper()
        if upper_correct_letter in answer_letter_list:
            correct_letter = upper_correct_letter
        else:
            print("Invalid input.")
            continue

    valid_input = False
    while not valid_input:
        points = input("Enter the number of points awarded for the correct answer: ")
        if points.isdigit():
            valid_input = True
        else:
            print("Invalid input. You must enter a number.")

    question_string += f"\n{question};{answers[0]};{answers[1]};{answers[2]};{correct_letter};{points}"

    with open(file_name, "w") as f:
        f.write(question_string)

    while run_again not in run_again_list and run_again not in not_run_again_list:
        run_again = input("Do you want to add another question? ")
        if run_again.upper() in not_run_again_list:
            quit()
        elif run_again.upper() in run_again_list:
            break
        else:
            print("Invalid input.")
            continue
