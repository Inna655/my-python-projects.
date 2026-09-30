tempC = float(input("Введите температуру в цельсиях:"))
tempF = tempC * 9/5 + 32
km = float(input("Введите расстояние в км:"))
ml = km * 0.621371
kg = float(input("Введите вес в кг:"))
ft = kg * 2.20462

print("=== Конвертер ===")
print(f"Температура: {tempC} C = {tempF} F")
print(f"Расстояние: {km} км = {ml} миль")
print(f"Вес: {kg} кг = {ft} фунтов")
print("=================")

