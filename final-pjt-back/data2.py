import requests
import json
from collections import OrderedDict

apikey = 'd6896467202dce6f8e1bc50756170a26'
movie_list = range(0, 1)
mylist = []
for num in movie_list:
    try:
        file_data = OrderedDict()
        url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=ko-kr".format(num, apikey)
        r = requests.get(url)
        data = json.loads(r.text)

        video_url = "https://api.themoviedb.org/3/movie/{}/videos?api_key={}".format(num, apikey)
        video_r = requests.get(video_url)
        video_data = json.loads(video_r.text)
        # print(video_data)
        video_id = video_data["results"][-1]["key"]

        # print(num)

        if len(data["overview"]) > 10 and int(data["release_date"][:4]) >= 1980 and len(data["poster_path"]) > 10 and len(data["backdrop_path"]) > 10:
            file_data["id"] = 'movie{}'.format(num)
            file_data["title"] = data["title"]
            file_data["genres"] = data["genres"]
            file_data["overview"] = data["overview"]
            file_data["title"] = data["title"]
            file_data["poster_path"] = data["poster_path"]
            file_data["release_date"] = data["release_date"]
            file_data["vote_average"] = data["vote_average"]           
            file_data["video"] = video_id
            file_data["backdrop_path"] = data["backdrop_path"]
            mylist.append(file_data)

    except:
        pass
    
    with open('sub_movies.json', 'w', encoding="utf-8") as make_file:
        json.dump(mylist, make_file, ensure_ascii=False, indent="\t")