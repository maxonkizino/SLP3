def countries(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(' ')
                country = parts[0]
                capital = parts[1]
                population = int(parts[2])
                area=int(parts[3])

                if population > 1000000:
                     print(f"Страна: {country}, Столица: {capital}, Население: {population}, Площадь: {area}")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")



countries('Государство.txt')



