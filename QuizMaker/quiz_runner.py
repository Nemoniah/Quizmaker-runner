def remove(item, _list):
    while item in _list:
        _list.remove(item)
    return _list


question_i = 0
answer_i = (1, 2, 3)
correct_i = 4
points = 5
answer_letter_list = ["A", "B", "C"]
score = 0
max_score = 0

file_name = input("Enter file name: ")
if file_name[-4:] != ".txt":
    file_name += ".txt"
f = open(file_name, "r")
text = f.read()

questions = text.split("\n")
remove("", questions)
for question in questions:
    new = question.split(";")
    remove("", new)
    print(new[question_i])
    answers = new[answer_i[0]:answer_i[-1]+1]
    for answer in answers:
        print(answer)
    valid_input = False
    while not valid_input:
        answer = input("> ")
        if answer.upper() not in answer_letter_list:
            print("Invalid input. Enter a letter corresponding to an answer.")
            continue
        else:
            valid_input = True
    if answer.upper() == new[correct_i]:
        print("Correct!")
        score += int(new[points])
    else:
        print("Incorrect!")
    max_score += int(new[points])
print(f"You scored {score} points! That's {score/max_score*100}%!")
