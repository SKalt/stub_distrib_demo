def foo(x):
    return sum(
        len(i.replace("a", "")) + len(j)
        # i must be str & j (for reasons outside this line) must be tuple
        for i, j in x.items()  # x must be a Dict
    )
