from bisect import bisect

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score, scores=scores, belts=belts):
    # scores_belts= list(zip(scores,belts))
    ind= bisect(scores, user_score)
    if ind==0:
        return None
    elif ind>=len(belts):
        return belts[-1]
    else:
        return belts[ind-1]

for score, expected in [(3,'None'),(10,'white'),(12,'white'),(900,'paneled'),(1000,'red'),(1001,'red')]:
    print(f"{score=} {expected=} result={get_belt(score)}")