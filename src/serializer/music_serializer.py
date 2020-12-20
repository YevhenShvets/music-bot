def get_music_list_serealizer(musics):
    answer = ""
    for i in range(len(musics)):
        answer += f"*{(i+1)}.* {musics[i]['author']} - "
        answer += f"{musics[i]['name']}\n"
    return answer
