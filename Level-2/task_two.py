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


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
