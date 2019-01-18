import requests
from datetime import datetime, timedelta
import csv
import os
KOBIS_KEY = os.getenv('KOBIS_KEY')
NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')

movie_list = []
movie_data_w = {}

time1 = datetime(2019,1,13)
day = []
for i in range(10):
    times = time1 + timedelta(days =- 7*i)
    day.append(times.strftime('%Y%m%d'))
day.reverse()
for j in range(10):
    URL_w = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={KOBIS_KEY}&targetDt={day[j]}&weekGb=0'
    data_w = requests.get(URL_w).json()
    result_w = data_w['boxOfficeResult']['weeklyBoxOfficeList']

    for i in range(10):
        simple_data = {}
        simple_data['moviecd'] = result_w[i]['movieCd']
        simple_data['name'] = result_w[i]['movieNm']
        simple_data['audience'] = result_w[i]['audiAcc']
        simple_data['day'] = day[j]
        if simple_data['moviecd'] not in movie_list:
            movie_list.append(simple_data['moviecd'])
            movie_data_w[result_w[i]['movieNm']] = simple_data
        else:
            movie_data_w[result_w[i]['movieNm']]['audience'] = result_w[i]['audiAcc']
            movie_data_w[result_w[i]['movieNm']]['day'] = day[j]

f = open('boxoffice.csv', 'w+', encoding='utf-8', newline='' )
writer = csv.writer(f)
writer.writerow(['영화코드', '영화제목', '누적관객', '검색일'])
for key, value in movie_data_w.items():
    result = []
    result += value['moviecd'], value['name'], value['audience'], value['day']
    writer.writerow(result)
f.close()


movie_data_i = {}
movie_names = []
for i in range(len(movie_list)):
    URL_i = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={KOBIS_KEY}&movieCd={movie_list[i]}'
    data_i = requests.get(URL_i).json()
    result_i = data_i['movieInfoResult']['movieInfo']
    result = {}
    result['moviecd'] = movie_list[i]
    result['name'] = result_i['movieNm']
    result['nameE'] = result_i['movieNmEn'].replace(',', '.')
    result['nameO'] = result_i['movieNmOg']
    result['year'] = result_i['prdtYear']
    result['showtime'] = result_i['showTm'] + 'min'
    result['genre'] = result_i['genres'][0]['genreNm']
    result['direc'] = result_i['directors'][0]['peopleNm']
    result['audit'] = result_i['audits'][0]['watchGradeNm']
    result['actor1'] = ''
    result['actor2'] = ''
    result['actor3'] = ''
    if len(result_i['actors']) > 0:
        result['actor1'] = result_i['actors'][0]['peopleNm']
        if len(result_i['actors']) > 1:
            result['actor2'] = result_i['actors'][1]['peopleNm']
            if len(result_i['actors']) > 2:
                result['actor3'] += result_i['actors'][2]['peopleNm']
    movie_data_i[result_i['movieNm']] = result
    movie_names.append(result['name'])
f = open('movie.csv', 'w+', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(['영화코드','영화제목','영문제목', '원어제목', '개봉년', '상영시간', '장르', '감독', '관람등급', '배우1', '배우2', '배우3'])
for key, value in movie_data_i.items():
    result = []
    result += value['moviecd'], value['name'], value['nameE'], value['nameO'], value['year'], value['showtime'], value['genre'], value['direc'], value['audit'], value['actor1'], value['actor2'], value['actor3']
    writer.writerow(result)
f.close()


import time
movie_data_n = {}
count = 0
for movie in movie_names:
    URL = f'https://openapi.naver.com/v1/search/movie.json?query='
    headers = { 'X-Naver-Client-Id': NAVER_CLIENT_ID, 'X-Naver-Client-Secret': NAVER_CLIENT_SECRET }
    data_n = requests.get(URL + movie, headers=headers).json()['items'][0]
    result = {}
    result['name'] = movie
    result['moviecd'] = movie_list[count]
    result['image'] = data_n['image']
    result['url'] = data_n['link']
    result['rate'] = data_n['userRating']
    movie_data_n[result['name']] = result
    count += 1
    if count % 5 == 0:
        time.sleep(1)
    fileurl = result['image']
    filename = result['moviecd']
    f = open(f'./picture/{filename}.jpg', 'wb+')    
    response = requests.get(fileurl, stream=True)
    for block in response.iter_content(1024):
        if not block:
            break
        f.write(block)
    f.close()
f = open('movie_naver.csv', 'w+', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(['영화제목','영화코드','썸네일', 'URL', '평점'])
for key, value in movie_data_n.items():
    result = []
    result += value['name'], value['moviecd'], value['image'], value['url'], value['rate']
    writer.writerow(result)
f.close()