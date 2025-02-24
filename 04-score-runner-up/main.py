if __name__ == "__main__":
    n = int(input())
    if not (n >= 2 and n <= 10):
        print("error 1")
        raise Exception("Sorry, the number has to be between 2 and 10")
    arr = map(int, input().split())
    scores = list(set(arr))
    scores.sort(reverse=True)
    for score in scores:
        if not (score >= -100 and score <= 100):
            raise Exception("Sorry, the score has to be between -100 and 100")
    print(scores[1])
