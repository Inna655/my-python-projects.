pswd = input("Введите пароль:")
lenght_ok = len(pswd) >= 8
not_weak = pswd != "12345"
is_strong = lenght_ok and not_weak
print(f"Пароль: {pswd}")
print(f"Длина >= 8: {lenght_ok}")
print(f"Пароль не 12345: {not_weak}")
print(f"Пароль надежный: {is_strong}")