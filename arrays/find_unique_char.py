def unique_char(str):
    s = set()

    for let in str:

        if let in s:
            return False
        else:
            s.add(let)

    return True

print(unique_char('abceda'))
