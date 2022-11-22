class FootballPlayer:
    def __init__(self, name, surname, goal=1, assist=1):
        self._name = name
        self._surname = surname
        self._goal = goal
        self._assist = assist

    def __str__(self):
        return (f"{self._name} {self._surname}: "
                f"goals = {self._goal}, "
                f"assists = {self._assist}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, goal):
        if goal > 0:
            self._goal = goal

    @property
    def assist(self):
        return self._assist

    @assist.setter
    def assist(self, assist):
        if assist > 0:
            self._assist = assist
