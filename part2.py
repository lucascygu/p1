def question1(n: dict) -> dict:
    return {v: k for k, v in n.items()}

def question2(n: dict) -> dict:
    result = {}
    for k, v in n.items():
        result.setdefault(v, []).append(k)
    return result

def question3(n: dict, m: dict) -> dict:
    result = n.copy()
    for k, v in m.items():
        if k in result:
            result[k] += v
        else:
            result[k] = v
    return result

def question4(n: list) -> list:
    from collections import Counter
    flat_list = [item for sublist in n for item in sublist]
    return [item for item, count in Counter(flat_list).items() if count > 1]
