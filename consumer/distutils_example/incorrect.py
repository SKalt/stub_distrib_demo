from my_package.foo import foo

slightly_wrong = {"a": [1, 2, 3], "bca": (4, 5)}

flaming_wrong = {["a"]: ["b"]}

foo(slightly_wrong)
foo(flaming_wrong)
