class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"оклад": int(wage), "премия": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["оклад"] + self._income["премия"]


kirill = Position('Кирилл', 'Соколов', 'слесарь', 3000, 1000)

print(kirill.get_full_name())
print(kirill.position)
print(kirill.get_total_income())
