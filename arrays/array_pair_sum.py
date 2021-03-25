def array_pair(arr, x):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = x - num

        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(target, num), max(target, num)))

    print('\n'.join(map(str, list(output))))

    return len(output)

arr=[1,3,2,2]
array_pair(arr,4)