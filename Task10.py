def first(x):
    print("Starting first")
    second(x)

def second(x):
    print("Starting second")
    third(x)

def third(x):
    print("Starting third")
    try:
        result = 10 / x
        return result
    except:
        x = x + 1
        first(x)

first(0)

# i predict the the output will be Starting first, Starting second, Starting third, 10.0
# the actual output was Starting first, Starting second, Starting third, Starting first, Starting second, Starting third