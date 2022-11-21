import urllib.request
import json
# import sqlite3

# 데이터베이스에 저장

# test.sqlite가 있는지 확인하고 없으면 새로운 데이터베이스 파일 생성
# data = sqlite3.connect("test.sqlite")
# cur = data.cursor()

# JSON 파일을 읽어오기
page = '1'
num = 4
key = []
for i in range(1, num):
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=d6896467202dce6f8e1bc50756170a26&language=ko-KR&page=' + str(i)

    # print(url)

    response = urllib.request.urlopen(url)
    response_message = response.read().decode('utf8')
    # print(response_message)

    response_data = json.loads(response_message)
    # print(response_data)

    # 원하는 데이터의 속성 지정
    columns = [
        'title',
        'release_date',
        'overview',
        'genre_ids',
        'vote_average',
        'poster_path',
        'backdrop_path',
        'popularity',
    ]
    genres = [
        {"id": 28, "name": "액션"}, 
        {"id": 12, "name": "모험"}, 
        {"id": 16, "name": "애니메이션"}, 
        {"id": 35, "name": "코미디"}, 
        {"id": 80, "name": "범죄"}, 
        {"id": 99, "name": "다큐멘터리"}, 
        {"id": 18, "name": "드라마"}, 
        {"id": 10751, "name": "가족"}, 
        {"id": 14, "name": "판타지"}, 
        {"id": 36, "name": "역사"}, 
        {"id": 27, "name": "공포"}, 
        {"id": 10402, "name": "음악"}, 
        {"id": 9648, "name": "미스테리"}, 
        {"id": 10749, "name": "로맨스"}, 
        {"id": 878, "name": "SF"}, 
        {"id": 10770, "name": "TV영화"}, 
        {"id": 53, "name": "스릴러"}, 
        {"id": 10752, "name": "전쟁"}, 
        {"id": 37, "name": "서부"}
    ]
    
    # 원하는 데이터를 리스트에 모으기
    for data2 in response_data['results']:
        keys = { "model" : "movies.movie"}
        fields = dict()
        genre_list = []
        for i in columns:
            if i == 'genre_ids':
                for j in range(len(data2[i])):
                    # print(j)
                    # print(data2[i][j])
                    for k in range(len(genres)):
                        if data2[i][j] == genres[k]['id']:
                            genre_list.append(genres[k]['name'])
                fields['genre_list'] = genre_list
            else:
                fields[i] = data2[i]
        # print(genre_list)
        print(fields)
        keys['fields'] = fields
        key.append(keys)

        
    # print(key)
    # print(len(key))
    

    file_path='./movies.json'

    with open(file_path, 'w', encoding="utf-8") as outfile:
        json.dump(key, outfile, ensure_ascii=False, indent=4)