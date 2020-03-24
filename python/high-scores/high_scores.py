def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    tmp = scores.copy()
    tmp.sort()
    output = []
    for i in range (3):
        if len(tmp) == 0:
            break
        output.append(tmp.pop())
        
    return output
