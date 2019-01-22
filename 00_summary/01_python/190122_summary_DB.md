## 190122 Summary DB

### 1. 기분 물어보고 저장하기

##### 기분을 물어보고 파일에 저장하기

```python
import csv
from datetime import datetime

def create():
    answer = input('What\'s up?: ')
    f = open('feeling.csv', 'a+', encoding='utf-8', newline='' )
    writer = csv.writer(f)
    fr = open('feeling.csv', 'r+', encoding='utf-8', newline='' )
    a = len(fr.readlines())
    dt = datetime.now()
    now = dt.strftime('%Y%m%d%H%M%S')
    writer.writerow([a, answer, now])
    f.close()
    fr.close()
    print([a, answer, now])
```



##### 몇번째에 어떤 기분이 저장되어 있는지 확인하기

```python
def read(**kwargs):
    f = open('feeling.csv', 'r+', encoding='utf-8', newline='')
    hint = [r.split(',') for r in f.readlines()]
    for i in range(len(hint)):
        hint[i][-1] = hint[i][-1].rstrip('\r\n')
        if i != 0:
            hint[i][0] = int(hint[i][0])
    for arg in kwargs.values():
        for i in hint:
            if i[0] == arg:
                print(i)
    f.close() 
```



##### n번째 기분을 수정하기

```python
def update(num='1', feeling='bad'):
    dt = datetime.now()
    timestamp = dt.strftime('%Y%m%d%H%M%S')
    f = open('dummy.csv', 'w+', encoding='utf-8', newline='' )
    fr = open('feeling.csv', 'r+', encoding='utf-8', newline='' )
    hint = [r.split(',') for r in fr.readlines()]
    writer = csv.writer(f)
    for h in hint:
        h[-1] = h[-1].rstrip('\r\n')
        if h[0] != 'id':
            h[0] = int(h[0])
        if str(h[0]) == str(num):
            h[1] = feeling
            h[2] = timestamp
        writer.writerow(h)
    f.close()
    fr.close()
    f = open('feeling.csv', 'w+', encoding='utf-8', newline='' )
    fr = open('dummy.csv', 'r+', encoding='utf-8', newline='' )
    hint = [r.split(',') for r in fr.readlines()]
    writer = csv.writer(f)
    for h in hint:
        h[-1] = h[-1].rstrip('\r\n')
        if h[0] != 'id':
            h[0] = int(h[0])
        writer.writerow(h)    
    f.close()
    fr.close()
```

이건 더미를 만들어서 수정한 내용을 옮겼다가 다시 원본파일을 덮어 씌우기..



##### 너무 복잡하다...



그래서 필요한게 RDBMS(관계형 데이터베이스 관리 시스템)

* MySQL
* SQLite  -> 이걸로 수업 진행
* PostgreSQL
* ORACLE  -> 유료!
* SQLserver -> 유료!



### 2. 기본 용어 정리

##### 스키마(scheme)

| column   | id   | age  | phone | email |
| -------- | ---- | ---- | ----- | ----- |
| datatype | INT  | INT  | TEXT  | TEXT  |

​			

##### 사용방법

* 터미널에서 $sqlite3 실행

* sqlite> CREATE TABLE menus(

  ...> id INTEGER,

  ...> menu_1 TEXT,

  ...> menu_2 TEXT

  ...> );

  * 이렇게 메뉴라는 테이블을 생성함

* sqlite> .table

  * menus table을 확인

* sqlite> INSERT INTO menus (id, menu1, menu2)
     ...> VALUES (1, 'Pho', 'Pork');

  * 이렇게 value를 입력

* SELECT id FROM menus WHERE id=1;

  * id가 1인 id를 검색
  * SELECT menu_1 FROM menus WHERE id=1;
    * id가 1인 menu_1을 검색

* SELECT * FROM menus;

  * 모든 menus table을 검색

* SELECT * FROM <table_name> Where [condition]

  * 조건으로 검색..

  ```sqlite
  SELECT * FROM users WHERE id=100;
  ```

  

* `.heders on` 혹은 `.mode column`을 입력하면 select를 할 때 보기 편하게 보인다.

  * `.headers on`

  ```sqlite
  id|name|price
  1|Pho|10000
  2|짬뽕|8000
  3|알리오올리오|12000
  ```

  * `.mode column`

  ```sqlite
  id          name        price     
  ----------  ----------  ----------
  1           Pho         10000     
  2           짬뽕      8000      
  3           알리오 12000  
  ```



### 3. 파일로 정리하기

##### sqlite3 폴더에 `create_table.sql`파일과 `insert_record.sql`파일을 생성한다.

##### `create_table.sql`파일에 테이블을 생성하는 명령어를 입력해 준다

```sqlite
CREATE TABLE computers (
    id INT PRIMARY KEY,
    year INT,
    company TEXT,
    model TEXT
);
```

##### `insert_record.sql`파일에 values를 insert해주는 명령어를 입력해준다.

```sqlite
INSERT INTO computers (year, company, model)
VALUES 
(2018, 'Samsung', 'Series9'),
(2019, 'LG', 'Gram17');
```

##### 해당 폴더에서 각 파일을 read한다

```sqlite
.read create_table.sql 

.read insert_record.sql      
```

##### 그 다음 파일 내용을 읽어들이면 입력한 내용이 다 포함되어있다.

```sqlite
|2018|Samsung|Series9
|2019|LG|Gram17
```



##### zzu.li/hellodb 에서 users.csv를 받은 후에

```sqlite
.mode csv
.import users.csv users
```

를 하면 users라는 table로 users.csv파일이 저장되게 된다.



#### TABLE 삭제

```sqlite
DROP TABLE users;
```

이렇게 하면 users table이 삭제된다.



#### TABLE 이름 변경 

```sqlite
ALTER TABLE users RENAME TO userss;
```

이렇게 하면 users table이 userss로 이름이 변경된다.



#### DATA 수정

```sqlite
UPDATE <table_name>
SET <col_1>=<val_1>, <col_2>=<val_2>, ...
WHERE [condition]; -- 보통 primary key (id)로 선택
```



#### Data 삭제

```sqlite
DELETE FROM <table_name>
WHERE [condition]; -- 보통 primary key (id)로 선택
```





## 4. SQLite3 전용 명령어

| 명령어                           | 설명                                        |
| -------------------------------- | ------------------------------------------- |
| .mode csv                        | csv 처럼 보임                               |
| .mode column                     | 컬럼 기준으로 보임                          |
| .headers on                      | 헤더(컬럼이름) 같이 출력                    |
| .read <file.sql>                 | 해당 sql 스크립트 실행                      |
| .import <file.name> <table.name> | 해당 파일의 데이터를 지정한 테이블에 import |
| .schema                          | 스키마 전체 보기                            |



## 5. 표현식

##### 해당 컬럼의 갯수

```sqlite
SELECT COUNT(<col>) FROM <table_name>;
```



##### 해당 컬럼의 평균 / 총합 / 최소 / 최대

```sqlite
SELECT AVG(<col>) FROM <table_name>;  -- 평균
SELECT SUM(<col>) FROM <table_name>;  -- 총합
SELECT MIN(<col>) FROM <table_name>;  -- 최소
SELECT MAX(<col>) FROM <table_name>;  -- 최대
```





## 6. 정렬

##### order

```sqlite
SELECT <col> FROM <table_name>
ORDER BY <col_1>, <col_2> [ASC | DESC];
```

* ASC : 오름차순
* DESC : 내림차순

##### 제한(limit)

```sqlite
SELECT <col> FROM <table_name>
LIMIT <num>
```

* num 만큼만 출력함

##### 패턴(pattern)

```sqlite
SELECT * FROM <table_name>
WHERE <col> LIKE '<pattern>'
```

| 시작 | 예시    | 설명                                            |
| ---- | ------- | ----------------------------------------------- |
| %    | 2%      | 2로 시작하는 값                                 |
|      | %2      | 2로 끝나는 값                                   |
|      | %2%     | 2가 포함되는 값                                 |
| _    | _2      | 2번째 글자가 2인 값                             |
|      | 1___    | 1로 시작하며 4자리인 값                         |
|      | _2%     | 한글자 뒤에 2가 오고 뒤에 다른 값이 이어지는 값 |
|      | `2_%_%` | 2로 시작하는데 최소 3자리인 값                  |