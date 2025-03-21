input = 'aaba'

def do_the_thing(s) -> int:
    if not s:
        return 1
    # Let's allow a length of 1, as a edge case.
    from collections import defaultdict
    counter = defaultdict(int)
    limit = len(set(s))
    result = 0
    start = 0
    end = 0

    def advance():
        nonlocal start
        nonlocal end
        nonlocal counter
        nonlocal limit
        for c in s[start:]:
            if counter[c] == limit:
                break
            counter[c] += 1
            if end < len(s):
                end += 1

    # The substring s[start:end] satisfies the requirement, 
    # as do any of its substrings.
    advance()
    result += end - start
    while end < len(s):
        # The character s[end] was the one that exceeded the
        # the limit. We need to get rid of the first instance
        # of it in the current substring, i.e. we have to 
        # delete the prefix up to and including it.
        while counter[s[end]] == limit:
            counter[s[start]] -= 1
            start += 1
        # Now start adding characters again.
        advance()

        result += end - start

    return result

output = do_the_thing(input)
print(output)

print(do_the_thing('abcdefg'))