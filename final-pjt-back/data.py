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
    ]

    # 원하는 데이터를 리스트에 모으기
    for data2 in response_data['results']:
        keys = { "model" : "movies.movie"}
        fields = dict()
        for i in columns:
            fields[i] = data2[i]
        print(fields)
        keys['fields'] = fields
        key.append(keys)
        
    # print(key)
    # print(len(key))
    

    file_path='./movies.json'

    with open(file_path, 'w', encoding="utf-8") as outfile:
        json.dump(key, outfile, ensure_ascii=False, indent=4)