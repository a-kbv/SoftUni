

def list_manipulator(ll, command, where, *numbers):
    if not numbers:
        numbers = []
        numbers.append(1)

    if command == "add":
        if where == "beginning":
            for i in range(len(numbers)):
                ll.insert(i, numbers[i])
        if where == "end":
            for i in range(len(numbers)):
                ll.append(numbers[i])
    elif command == "remove":
        if where == "beginning":
            for _ in range(numbers[0]):
                ll.pop(0)
        if where == "end":
            for _ in range(numbers[0]):
                ll.pop()
    return ll
