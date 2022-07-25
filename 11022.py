T = int(input())
n = 0

for n in range(T):
    A, B = map(int, input().split())
    C = A + B
    print(f'Case #{n + 1}: {A} + {B} = {C}')
    n += 1
    