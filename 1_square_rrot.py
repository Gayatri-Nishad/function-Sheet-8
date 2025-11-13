def perfect_square_root(A):
    i = 1
    while i * i <= A:
        if i * i == A:
            return i
        i += 1
    return -1

# 🔹 Test
print(perfect_square_root(16))  # 4
print(perfect_square_root(20))  # -1
