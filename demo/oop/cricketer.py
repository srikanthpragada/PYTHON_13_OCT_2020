class Cricketer:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def print(self):
        print('Name     :', self.name)
        print('Country  :', self.country)


class Batsman(Cricketer):
    def __init__(self, name, country, runs):
        super().__init__(name, country)
        self.runs = runs

    def points(self):
        return self.runs // 50

    def print(self):
        super().print()
        print("Runs   :", self.runs)


class Bowler(Cricketer):
    def __init__(self, name, country, wickets):
        super().__init__(name, country)
        self.wickets = wickets

    def points(self):
        return self.wickets // 2

    def print(self):
        super().print()
        print("Wickets   :", self.wickets)


bowler = Bowler("Xyz", "India", 233)
print(bowler.points())
bowler.print()
