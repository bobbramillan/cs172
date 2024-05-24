#question file
from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, prompt="", correctAnswer="", points=0):
        self.__prompt = prompt
        self.__correctAnswer = correctAnswer
        self.__points = points
    
    @abstractmethod
    def displayForTest(self):
        pass

    def getPrompt(self):
        return self.__prompt

    def getCorrectAnswer(self):
        return self.__correctAnswer                    

    def getPoints(self):
        return self.__points

    def __str__(self):
        return f"Prompt: {self.__prompt}\nCorrect Answer: {self.__correctAnswer}\nPoints: {self.__points}"


class MultipleChoice(Question):
    def __init__(self, prompt, points, choices=[], correctAnswer=""):
        super().__init__(prompt, correctAnswer, points)
        self.__choices = choices

    def getChoices(self):
        return self.__choices

    def addChoice(self, newChoice):
        self.__choices.append(newChoice)

    def updateChoice(self, index, updatedChoice):
        self.__choices[index] = updatedChoice

    def displayForTest(self):
        result = f'{self.getPrompt()}'
        for choice in self.__choices:
            result += f"\n{choice}"
        return result

    def __str__(self):
        return f"{super().__str__()}\nChoices: {self.__choices}"

class ShortAnswer(Question):
    def __init__(self, prompt, length, correctAnswer="", points=0):
        super().__init__(prompt, correctAnswer, points)
        self.__length = length

    def getLength(self):
        return self.__length

    def setLength(self, length):
        self.__length = length

    def displayForTest(self):
        return f"\n{self.getPrompt()} (up to {self.__length} characters)"

    def __str__(self):
        return f"{super().__str__()}\nCharacter limit: {self.__length}"


class FillInTheBlank(Question):
    def __init__(self, prompt, correctAnswer="", points=0):
        super().__init__(prompt, correctAnswer, points)

    def displayForTest(self):
        return f"\nFill in the blank:\n{self.getPrompt()}"

    def __str__(self):
        return f"{super().__str__()}\n"
