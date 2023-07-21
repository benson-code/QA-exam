
def print_triangle(n):
    for i in range(n):
        for j in range((n - i) - 1):
            print(" ", end="")
        for k in range(i + 1):
            if k == 0 or k == i or i == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

n = int(input("請輸入正空心三角形的邊長："))
print_triangle(n)
