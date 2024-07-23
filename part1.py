def read_calls(file: open) -> {(str, str): int}:
    calls = {}

    for line in file:
        parts = line.strip().split(':')
        caller = parts[0]
        callees = parts[1:]

        for callee in callees:
            if (caller, callee) in calls:
                calls[(caller, callee)] += 1
            else:
                calls[(caller, callee)] = 1

    return calls

def call1to2(calls: {(str, str): int}) -> {str: {str: int}}:
    calls_nested_dict = {}

    for (caller, callee), count in calls.items():
        if caller not in calls_nested_dict:
            calls_nested_dict[caller] = {}
        calls_nested_dict[caller][callee] = count

    return calls_nested_dict
