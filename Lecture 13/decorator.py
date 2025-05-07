def change (func):
    print("Decorator ate function name")
    def inner(inner_number):
        print("inner istead of original func")
        return func(inner_number*2)
    return inner

@change
def add_five(number):
    print("Example lecture 13")
    return number + 5

@change
def sub_five(number):
    print("Original is here")
    return number - 5

print(add_five(6))
