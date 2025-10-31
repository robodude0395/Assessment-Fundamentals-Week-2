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
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment:
        """Get an assessment from trainee's assessment list based on assessment name"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

class Assessment:
    """Define assessment class with name, type and score"""
    assessment_types = ["multiple-choice", "technical", "presentation"]

    def __init__(self, name: str, assessment_type: str, score: float):
        self.name = name

        if assessment_type not in self.assessment_types:
            raise ValueError()

        self.assessment_type = type

        if not 0 <= score <= 100:
            raise ValueError()

        self.score = score



if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
