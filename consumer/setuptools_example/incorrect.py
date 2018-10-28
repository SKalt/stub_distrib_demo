from my_other_package.bar import bar

slightly_wrong = {"a": [1, 2, 3], "bca": (4, 5)}

flaming_wrong = {["a"]: ["b"]}

bar(slightly_wrong)
bar(flaming_wrong)
