class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return f'{self.first_name} {self.last_name}'

    def age(self):
        return 2017 - int(self.birth_date[-4:])

    def work(self):
        if self.gender == 'male':
            return f'Hi is a {self.job}'
        elif self.gender == 'female':
            return f'She is a {self.job}'
        elif self.gender == 'unknown':
            return f'Is a {self.job}'

    def money(self):
        space = 1
        a = ''
        s = str(int(self.working_years * 12 * self.salary))[::-1]
        for i in s:
            if space == 4:
                a += ' '
                space = 1
            space += 1
            a += i
        return a[::-1]

    def home(self):
        return f'Lives in {self.city}, {self.country}'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    print(p1.name())  # == "John Smith", "Name"
    print(p1.age())  # = 38, "Age"
    print(p2.work())  # == "Is a designer", "Job"
    print(p1.money())  # == "648 000", "Money"
    print(p2.home())  # == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")
