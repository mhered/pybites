class RecordScore():
    """Class to track a game's maximum score"""
    top_score = None
    
    def __call__(self, new_score):
        if not self.top_score or new_score > self.top_score:
            self.top_score = new_score


record = RecordScore()
print(record(10))
print(record(9))
print(record(11))
