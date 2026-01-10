print("\n----------------------------PYTHON QUIZ---------------------------------")

def menu():
    print("1. Start")
count = 0
start = int(input("press 1 to start : ")) #this line takes the input

if start == 1:
    def question1():#this is the function of Q1
        print("\n-------------------------PYTHON QUIZ----------------------------------")
        print("\nQ1. Which of the following is a correct variable name in Python?")
        print("a) 1name ")
        print("b) name_1 ")
        print("c) class ")
        print("d) my-name ")
        answer1 = input("enter the correct option : ")
        if answer1 == "b":#if answer is correct it will go to Q2 if not then it will repeat Q1
            print("correct answer!")
            global count
            count = count + 1

        else:
            print("\nIncorrect answer\n")
  

    def question2():#this is the function of Q2
        print("\nQ2. -------------------------PYTHON QUIZ----------------------------------")
        print("\nWhat is the correct file extension for a Python file?")
        print("a) .py ")
        print("b) .pt ")
        print("c) .p ")
        print("d) .python ")

        answer2 = input("enter the correct option : ")
        if answer2 == "a":#if answer is correct it will go to Q3 if not then it will repeat Q2
            print("correct answer!")
            global count
            count = count + 1
        else:
            print("\nIncorrect answer\n")
        


    def question3():#this is the function of Q3
        print("\n-------------------------PYTHON QUIZ----------------------------------")
        print("\nQ3. What will this code print? \nx = 5 \nprint(x)")
        print("a) x ")
        print("b) 0 ")
        print("c) 5 ")
        print("d) Error")

        answer3 = input("enter the correct option: ")
        if answer3 == "c":#if answer is correct it will go to Q4 if not then it will repeat Q3
            print("correct answer!")
            global count
            count = count + 1
        else:
            print("\nIncorrect answer\n")     

    def question4():#this is the function of Q4
        print("\n-------------------------PYTHON QUIZ----------------------------------")
        print("\nQ4. Which data type is this value: 3.14?")
        print("a) int ")
        print("b) float ")
        print("c) str ")
        print("d) bool")

        answer4 = input("enter the correct option : ")
        if answer4 == "b":#if answer is correct it will go to Q5 if not then it will repeat Q4
            print("correct answer!")
            global count
            count = count + 1
        else:
            print("\nIncorrect answer\n") 

    def question5():#this is the function of Q5
        print("\n-------------------------PYTHON QUIZ----------------------------------")
        print("\nQ5. Which of these creates a list in Python?")
        print("a) x = (1,2,3)")
        print("b) x = {1,2,3} ")
        print("c) x = [1,2,3] ")
        print("d) x = 1,2,3")

        answer5 = input("enter the correct option : ")
        if answer5 == "c":#if answer is correct it will go to Q6 if not then it will repeat Q5
            print("correct answer!")
            global count
            count = count + 1
        else:
            print("\nIncorrect answer\n")            

    def result():
        print("\n\n----------------------SCORE = ",count,"/5","------------------------------------")
        


    #from now function calling and next and previous will work (the code will execute from here)
    question1()
    next_prev1 = input("enter 'n' for next question | enter 'p' for previous question : ")
    
    
    while True:
        if next_prev1 == 'n':
            break
        elif next_prev1 == 'p':
            question1()
            break
            
    question2()
    next_prev2 = input("enter 'n' for next question | enter 'p' for previous question : ")
    while True:
        if next_prev2 == 'n':
            break
        elif next_prev2 == 'p':
            question1()
            question2()
            break
    
    question3()
    next_prev3 = input("enter 'n' for next question | enter 'p' for previous question : ")
    while True:
        if next_prev3 == 'n':
            break
        elif next_prev3 == 'p':
            question2()
            question3()
            break

    question4()
    next_prev4 = input("enter 'n' for next question | enter 'p' for previous question : ")
    while True:
        if next_prev4 == 'n':
            break
        elif next_prev4 == 'p':
            question3()
            question4()
            break

    question5()
    next_prev5 = input("enter 'n' for next question | enter 'p' for previous question : ")
    
    while True:
        if next_prev5 == 'n':
            print("---------------------QUIZ COMPLETED---------------------")
            break
        elif next_prev5 == 'p':
            question4()
            question5()
            break
    result()

    
    
