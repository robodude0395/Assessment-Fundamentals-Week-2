
"""Define Trainee and Assessment objects"""
from datetime import date

class Trainee:
    """Define trainee object with name email and date of birth (DOB)"""
    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self):
        """Return trainee age based on DOB"""
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def add_assessment(self, assessment: Assessment):
        """Add an assessment object to trainee's assessment list"""
        if not isinstance(assessment, Assessment):
            raise TypeError

        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment:
        """Get an assessment from trainee's assessment list based on assessment name"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def get_assessment_of_type(self, assessment_type: str) -> list[Assessment]:
        """Return a list of a given assessment type from the trainee's assessment list"""
        assessments_output_list = []

        for assessment in self.assessments:
            if assessment.type_name == assessment_type:
                assessments_output_list.append(assessment)

        return assessments_output_list
class Assessment:
    """Define assessment class with name, type and score"""
    weight = 1
    type_name = "assessment"

    def __init__(self, name: str, score: float):
        self.name = name

        if not 0 <= score <= 100:
            raise ValueError()

        self.score = score

    def calculate_score(self):
        """Return a score based on the assessment's score and weight"""
        return self.score*self.weight


class MultipleChoiceAssessment(Assessment):
    """Multiple choice child of assessment parent class"""
    def __init__(self, name, score):
        super().__init__(name, score)
        self.weight = 0.7
        self.type_name = "multiple-choice"

class TechnicalAssessment(Assessment):
    """Technical child of assessment parent class"""
    def __init__(self, name, score):
        super().__init__(name, score)
        self.weight = 1
        self.type_name = "technical"

class PresentationAssessment(Assessment):
    """Presentation child of assessment parent class"""
    def __init__(self, name, score):
        super().__init__(name, score)
        self.weight = 0.6
        self.type_name = "presentation"

class Question:
    """Question class which has """
    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    """Quiz holder class which contains the question, selected and correct answer"""
    def __init__(self, questions: list[Question], name: str, assessment_type: str):
        self.questions = questions
        self.name = name
        self.assessment_type = assessment_type


class Marking:
    """
    Marking class which takes in a quiz and returns a marked assessment of correct type and score.
    """
    assessment_types = {"presentation": PresentationAssessment,
                        "technical": TechnicalAssessment,
                        "multiple-choice": MultipleChoiceAssessment}

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz

    def mark(self) -> int:
        """
        This method should return the total score for the assessment as a percentage,
        rounded to zero decimal places (i.e. an int)."""
        total = len(self._quiz.questions)
        if total == 0:
            return 0

        correct = 0

        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                correct += 1

        return int((correct/total)*100)

    def generate_assessment(self) -> Assessment:
        """
        This should return an instance of an Assessment of
        the correct subclass with the correct name and score.
        """
        score = self.mark()
        name = self._quiz.name
        return self.assessment_types[self._quiz.assessment_type](name, score)

if __name__ == "__main__":
    # Example questions and quiz
    input_questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz_example = Quiz(input_questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
