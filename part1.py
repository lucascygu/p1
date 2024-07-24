def read_calls(file_path):
    calls_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            calls = line.strip().split(':')
            caller = calls[0]
            for callee in calls[1:]:
                if (caller, callee) in calls_dict:
                    calls_dict[(caller, callee)] += 1
                else:
                    calls_dict[(caller, callee)] = 1
    return calls_dict

def call1to2(calls_dict):
    nested_dict = {}
    for (caller, callee), count in calls_dict.items():
        if caller not in nested_dict:
            nested_dict[caller] = {}
        nested_dict[caller][callee] = count
    return nested_dict

if __name__ == "__main__":
    calls_dict = read_calls('calls.txt')
    print(calls_dict)
    nested_dict = call1to2(calls_dict)
    print(nested_dict)
