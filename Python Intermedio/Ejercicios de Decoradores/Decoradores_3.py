from datetime import date


class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
    
def check_adult(func):
    def wrapper(*args, **kwargs):
        user = args[0]

        if not isinstance(user, User):
            raise TypeError("First argument must be a User")

        if user.age < 18:
            raise ValueError("User must be an adult")

        return func(*args, **kwargs)

    return wrapper


@check_adult
def enter_casino(user):
    print("Welcome to the casino")

adult = User(date(1990, 1, 1))
enter_casino(adult)

teen = User(date(2010, 1, 1))
enter_casino(teen)