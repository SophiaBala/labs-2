def transition_function(needle, alphabet):
    m = len(needle)
    transition = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for char in alphabet:
            k = min(m, state + 1)
            while k > 0 and not (needle[:k] == (needle[:state] + char)[-k:]):
                k -= 1
            transition[state][char] = k
    return transition

def finite_automaton_search(text_list, needle):
    results = []
    needle = needle.lower()

    for line in text_list:
        haystack = line.lower()
        if not needle or not haystack:
            continue

        alphabet = set(haystack)
        transition = transition_function(needle, alphabet)
        state = 0

        for i in range(len(haystack)):
            char = haystack[i]
            state = transition[state].get(char, 0)
            if state == len(needle):
                results.append(line)
                break  
    return results