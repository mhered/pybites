from datetime import date
MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""


    def __setitem__(self, name, birthday):
        for bday in self.values():
            if birthday.day == bday.day and birthday.month == bday.month:
                # match
                print(MSG.format(name))
        super().__setitem__(name, birthday)


bd = BirthdayDict()
bd['bob'] = date(1987, 6, 15)
bd['tim'] = date(1984, 7, 15)
print(bd)
bd['mary'] = date(1987, 6, 15)  # whole date match
# Hey mary, there are more people with your birthday!
bd['sara'] = date(1987, 6, 14)
bd['mike'] = date(1981, 7, 15)  # day + month match
# Hey mike, there are more people with your birthday!
