def generate_password(n):
    password = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                password += f"{i}{j}"
    return password

result = generate_password(6)
print(f"Пароль: {result}")
