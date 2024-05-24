#main file by Bavanan Bramillan(bb3323)
import questions as Q

#this takes each question from the main func and displays it and also takes in/asks for the answer
def answerQuestion(question):
    print(question.displayForTest())
    userAnswer = input("\nEnter the answer: ")
    return userAnswer.strip().lower()

#this relies on the above func and each question from main func to determine points through answer checking
def gradeQuestion(question, userAnswer):

    #question used here is for the q1 etc as shown in for loop
    if userAnswer.lower() == question.getCorrectAnswer().lower():
        return question.getPoints()
    else:
        return 0


#this has all the questions
def main():
    q1 = Q.MultipleChoice("Who wrote Seinfeld?", 10, ['A. Larry David', 'B. David Zaslav', 'C. Jerry Seinfeld'], "C")
    q2 = Q.FillInTheBlank("The Burj Khalifa is in _____","Dubai", 7)
    q3 = Q.ShortAnswer("The primary colors recognized by human eye?", 20, "Red, Green, Blue", 8)


    listofQs = [q1,q2, q3]
    totalPoints = 0

    #this takes the list of q's and cycles each one thru the answerQuestion & gradeQuestion
    for question in listofQs:
        userAnswer = answerQuestion(question)
        points_earned = gradeQuestion(question, userAnswer)
        totalPoints += points_earned

            
    print(f"\nYou earned: {totalPoints} points!")

main()
