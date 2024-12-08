import json

def calculate_profits(filename):
    profits = {}
    total_profit = 0
    profit_count= 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Убираем пробелы и разбиваем строку
            parts = line.split()
            firm_name = parts[0]
            revenue = int(parts[2])
            costs = int(parts[3])
            profit = revenue - costs

            profits[firm_name] = [parts[1],profit]

            if profit > 0:
                total_profit += profit
                profit_count += 1

    # Вычисляем среднюю прибыль
    average_profit = total_profit / profit_count if profit_count > 0 else 0

    # Формируем результирующий список
    result = [profits, {"average_profit": average_profit}]

    return result

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)




#=============================================================

filename = 'Фирмы.txt'
json_filename = 'Выгода_фирм.json'

profit_data = calculate_profits(filename)
save_to_json(profit_data, json_filename)

print(f"Данные успешно сохранены в {json_filename}")


