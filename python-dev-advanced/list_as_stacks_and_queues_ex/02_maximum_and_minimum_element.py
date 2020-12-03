
def solve():
    n = int(input())
    sequence = []

    for _ in range(n):
        data = input().split()
        command = data[0]

        if command == '1':
            sequence.append(data[1])
        elif command == '2':
            if sequence:
                sequence.pop()
        elif command == '3':
            if sequence:
                print(max(sequence))
        elif command == '4':
            if sequence:
                print(min(sequence))
    return sequence


sequence = solve()
print(', '.join(sequence[::-1]))
