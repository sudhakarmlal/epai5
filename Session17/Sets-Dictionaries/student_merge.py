from collections import defaultdict, Counter

def merge_with_defaultdict(*args):
    merged_dicts = defaultdict(int)
    for dicts in args:
        for key in dicts.keys():
            merged_dicts[key] += dicts.get(key)
    return merged_dicts


def merge_with_counter(*args):
    merged_dicts = Counter()
    for dicts in args:
        for key in dicts.keys():
            merged_dicts[key] += dicts.get(key)
    return merged_dicts