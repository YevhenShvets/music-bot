def get_name_films_serealizer(data):
    answer = ""
    for i in range(len(data)):
        answer += f"*{(i+1)}.* {data[i]['name']}\n"
    return answer


def get_film_info(data):
    answer = ""
    answer += f"*{data['name']}*\n"
    answer += f"*Тип: *_{data['type']}_\n"
    answer += f"*Режисер: *_{data['director']}_\n"
    answer += f"*Про фільм: *_{data['description']}_\n"
    return answer
