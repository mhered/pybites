class RecordScore():
    """Class to track a game's maximum score"""


    def __init__(self):
        self.top_score = None

    
    def __call__(self, new_score):
        if not self.top_score or new_score > self.top_score:
            self.top_score = new_score
        return self.top_score


record = RecordScore()
print(record(-5))
print(record(-9))
print(record(-2))
