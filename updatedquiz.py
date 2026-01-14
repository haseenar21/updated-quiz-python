incorrect=0
correct=0
grp = {
    "first":{
       "ques":"Q1 What is the correct file extension for Python?",
       "options":"A) .py \n B) .p \n C) .pyt \n D) .python",
       "correct_answer":"A"
       },
    "second":{
        "ques":"Q2 Which keyword is used to define a function in Python?",
        "options":"A) fun \n B) define \n C) def \n D) function",
        "correct_answer":"C"
    },
    "third":{
        "ques":"Q3 What will len([1,2,3]) return?",
        "options":"A) 2 \n B) 3 \n C) Error \n D) None",
        "correct_answer":"B"
    },
    "fourth":{
        "ques":"Q4 Which symbol is used for comments in Python??",
        "options":"A) // \n B) <!-- --> \n C) # \n D) **",
        "correct_answer":"C"
    }
}


def ask(num):
    global correct,incorrect
    print(num["ques"])
    print(num["options"])
    ans=input("Enter your option (A/B/C/D): ")
    if ans.upper() == num["correct_answer"]:
        print("Correct answer")
        correct +=1
    else:
        print("Incorrect\nCorrect answer : "+num["correct_answer"])
        incorrect +=1
print("-------------------------------------------------------")
print("        PYTHON QUIZ")
print("-------------------------------------------------------")
print("Total Questions : ",len(grp))
print("Each correct answer = 1 mark")
if(input("Do you want to play (y/n) : ").lower() == "y"):
    print("Let's play.")

    for key in grp.values():
        ask(key)

    print("------------------------")
    print("        RESULT")
    print("------------------------")

    print("Correct Answers : ",correct)
    print("Wrong Answers : ",incorrect)
    print("Final Score : ",correct,"/",len(grp))

    if(incorrect >= 3):
        print("RESULT : FAIL")
    else:
        print("RESULT : PASS")

else:
    print("Exiting")