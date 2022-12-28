from datetime import datetime, timedelta
NOW = datetime.now()


class Promo:
    def __init__(self, name:str, expires: datetime):
        self.name = name
        self.expires = expires
        print(f"{self.name} expires on {self.expires}")
        

    @property
    def expired(self):
        return True if datetime.now() >= self.expires else False


if __name__ == "__main__":
    test1 = Promo ("Promo1", datetime.now()-timedelta(days=2))
    print(test1.expired)
    test2 = Promo ("Promo2", datetime.now())
    print(test2.expired)
    test3 = Promo ("Promo2", datetime.now()+timedelta(days=2))
    print(test3.expired)