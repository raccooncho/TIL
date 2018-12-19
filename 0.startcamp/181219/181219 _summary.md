# 181219 수업정리

## 1. 문제풀이

### 	1. 나의 평균을 구하시오 (float) 	

```python
my_score = [79, 84, 66, 93]

ams = sum(my_score)
len(my_score)
my_average = ams / len(my_score)
print("나의 평균 점수는", my_average, "입니다.")
```



### 	2. 친구의 평균을 구하시오(float)

```python
your_score = {
    '수학' : 87,
    '국어' : 83,
    '영어' : 76,
    '도덕' : 100
}

ays = sum(list(your_score.values()))


your_average = ays / len(your_score)
print("당신의 평균 점수는", your_average, "입니다.")
```



### 	3. 도시별 평균 온도

<보기 자료>

```python
cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
}

```

* 교수님 답안

```python
for city, temperatures in cities_temp.items():   # 모범답안
    print(city, ':', round(sum(cities_temp[city]) / len(cities_temp[city]), 2))


```

* 내 답안

```python
cities_average = {} 

for city in cities_temp:
    cities_average[city] = round(sum(cities_temp[city]) / len(cities_temp[city]), 2)

for city in cities_average:
    print(city, ':', str(cities_average[city]))
```

### 	4. 최근 3일간 가장 추웠던 도시와 가장 더웠던 도시

* 'nadarm'의 답안

```python
hottest_city = {"cityname" : "None", "temp" : -999} # 'nadarm'의 답안
coldest_city = {"cityname" : "None", "temp" : 999}

for city, value in cities_temp.items():
    for temp in value:
        if hottest_city["temp"] < temp:
            hottest_city["cityname"] = city
            hottest_city["temp"] = temp
    for temp in value:
        if coldest_city["temp"] > temp:
            coldest_city["cityname"] = city
            coldest_city["temp"] = temp
    
print("최근 3일간 가장 더운 도시는", hottest_city["cityname"], '이고, 그 온도는', hottest_city["temp"], "였습니다.")
print("최근 3일간 가장 추운 도시는", coldest_city["cityname"], '이고, 그 온도는', coldest_city["temp"], "였습니다.")       

```

* 교수님 답안

```python
# all_temp에 모든 기온을 모은다.  # 교수님 풀이
all_temp = []
for key, value in cities_temp.items():
    all_temp += value

print(all_temp)

# all_temp 에서 max / min을 찾는다.
highest = max(all_temp)
lowest = min(all_temp)
print(highest, lowest)
# cities_temp에서 max / min이 속한 도시를 찾는다.
hottest = []
coldest = []
for key, value in cities_temp.items():
    if highest in value:
        hottest.append(key)
    if lowest in value:
        coldest.append(key)

print(hottest, coldest)
```



