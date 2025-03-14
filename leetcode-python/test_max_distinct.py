input = 'aaba'

def do_the_thing(s) -> int:
    # Let's allow lengths of 0 and 1, as edge cases.
    from collections import defaultdict
    counter = defaultdict(int)
    limit = len(set(s))
    result = 0
    start = 0
    # Use exclusively, per Python convention.
    end = 0

    # The substring s[start:] satisfies the requirement, 
    # as do any of its substrings.

    while True:
        while end < len(s):
            c = s[end]
            # We can't add this character to the current substring.
            if counter[c] == limit:
                break
            counter[c] += 1
            end += 1
        assert(len(set(s[start:end]))) <= limit
        # Every substring starting at start meets the requirement.
        result += end - start
        if end == len(s):
            break
        
        # The character s[end] was the one that exceeded the
        # the limit. We need to get rid of the first instance
        # of it in the current substring, i.e. we have to 
        # delete the prefix up to and including it.
        counter[s[end]] += 1
        while counter[s[end]] > limit:
            counter[s[start]] -= 1
            start += 1

    # When we broke from the loop, s[start:end + 1] was a maximal substring.
    # Now we need to include all substrings beginning after start.
    start += 1
    while start < len(s):
        result += len(s) - start - 1

    return result

output = do_the_thing(input)
print(output)

print(do_the_thing('abcdefg'))