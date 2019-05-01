# Asynchronous Javascript

```sh
$ mkdir SyncAsync
$ touch SyncAsync/sync.js
```

## Sync vs Ascync Code

실제 개발에서는 배열이 아니라 DB를 사용한다. 데이터베이스를 사용하기 전에 드디어 비동기 프로그래밍을 배울 차례가 왔다! 비동기 프로그래밍에 깊고 확실한 이해가 필요하다.

`SyncAsync/sync.js`

```js
console.log('메인 코드 진행중!');
console.log('메인 코드 계속 진행중!');
```

위 코드는 전형적으로 동기적(synchronous / blocking)으로 작동하는 코드다. 첫 줄이 실행되는 동안 두번째 줄이 실행되는 것을 막고있기(blocking) 때문이다.첫 줄이 끝나야지만 다음줄이 실행된다.

반면, 비동기적(asynchronous / non-blocking) 프로그램 역시 존재한다.

```js
console.log('메인 코드 진행중!');
setTimeout(() => {
  console.log('Reading Data from DB');
}, 2000);
console.log('메인 코드 계속 진행중!');
```

위 코드는 DB 에서 정보를 가져올 때 2초 정도가 가정하여 작성했다. `setTimeout()` 은 두번째 인자에 적힌 ms 만큼이 지나면, 첫번째 인자인 익명함수가 실행된다.  어떻게 출력될까? `메인 코드 진행중!` => `Reading Data from DB` => `메인 코드 계속 진행중!` 순서대로 출력될까?

```sh
$ node index.js
메인 코드 진행중!
메인 코드 계속 진행중!
Reading Data from DB
```

`메인 코드 진행중!` => `메인 코드 계속 진행중!` => 2초… => `Reading data from DB` 순으로 출력된다.

`setTimeout()` 은 대표적인 asynchronous / non-blocking 함수이다. 위에서 살펴본듯이 다음 코드의 실행을 막지 않는다. 이 함수는 실행되면, 미래(2초 후)에 수행할 task 를 스케줄링한다.

즉 `2000` 이후에 `() => { console.log('Reading data from DB ')}`라는 함수를 실행하도록 스케줄링 하는 것이다. `setTimeout()` 이 하는 일은 단지 `2000` 이후에 일어날 일(익명함수)을 예약하는 것 뿐이다! 수행이 되지 않은 것이 아니라, 함수 실행은 되었지만, 예약만 하고 바로 다음줄로 넘어간 것이고, 어떠한 코드의 흐름도 기다리거나 막지 않았다.

한가지 다시한번 짚고 넘어가고 싶은것은, 비동기적 처리라는 의미가, 동시다발적(concurrent) / 다중 작업처리(multi-threaded)를 의미하는 것이 아니라는 것이다. 오직 하나의 스레드만이 작동하고 있고, 첫째줄(출력) => 둘째줄(예약) => 셋째줄(출력) 순으로 작업을 처리하고 놀고있게 된다. 2초를 기다리는 동안 어떠한 일도 하지 않고, 2초 후에 예약된 작업이 실행되면 해당 작업을 그제서야 실행한다.

예시로서 많이 사용되는 레스토랑을 생각해보면, 동기적(sync) 레스토랑은 웨이터가 주문을 받고 주방에 주문을 전달한 다음, 음식이 나올때까지 그 앞에서 계속해서 기다리고 있다. 즉 나머지 테이블은 주문을 하지 못한다. 만약 계속해서 주문을 받고싶다면 웨이터(스레드)를 늘려야 한다. 이것이 동시다발적/멀티스레딩 프로그램이다.

반면 비동기적(async) 레스토랑은 웨이터가 주문을 받고 주방에 주문을 전달(예약)한 다음 다음 테이블로 가서 주문을 받는다. 주문한 음식이 나오면 그때 가서 해당 음식을 배달해 주는 방식이다. 동시 다발적으로 스레드가 일을 하는 것이 아니다!

왜 이렇게 복잡하고 장황한 내용을 알아야 하는가.. ( •́ ̯•̀  )? 왜냐하면 Node.js 프로그래밍에서 저장공간이나 네트워크 접속에 관련된 작업을 수행할 때 반드시 비동기 코드를 다뤄야 하기 때문이다. 그리고 비동기 코드를 어떻게 아름답고 유지보수 가능하게 짜는 것을 아는것이 매우 중요하다.

## Async Code 처리 패턴

좀더 이전에 작성한 코드를 실제 상황에 맞게 작성해보자.

`SyncAsync/sync.js`

```js
console.log('메인 코드 진행중!');
const user = getUser(1);
console.log(user);
console.log('메인 코드 계속 진행중!');


function getUser(id) {
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];
  setTimeout(() => {
    return users.find((user) => {
      return user.id === id;
    });
  }, 2000)
}
```

실행해 보면  `메인 코드 진행중!` => `undefined` => `메인 코드 계속 진행중!` 순으로 수행된다! `console.log(getUser(1))` 에서 `console.log` 는 먼저 수행되면서 `getUser(1)` 를 실행하고 출력해 버리는데, 출력되는 시점에서는 `getUser()` 가 아무것도 return하고 있지 않기 때문이다! 실제 DB 에서 정보를 읽어오는 작업은 아무리 빨라도 시간이 걸리기 마련이다. 때문에 `getUser()` 안에 `setTimeout()`으로 시뮬레이션을 만든 것이다.

그렇다면 메인 프로그램에서 `const user = getUser(1)` 코드를 작동하게 하려면 어떤 방법을 써야할까? 이런 비동기 코드를 작성할 때에는 3가지 패턴이 있다.

1. Callback
2. Promise
3. `async` / `await` (Syntactical sugar)

## 패턴1: Callback

우선 코드에서 `getUser(1)` 의 리턴 값이 바로 사용 불가능 한것은 확인했다. 그렇다면 이제 콜백함수를 사용해서 이 `getUser(1)` 의 리턴값을 사용 가능하게 만들어 보자.

```sh
$ pwd
.../.../SyncAsync
$ touch callback.js
```

`SyncAsync/callback.js`

```js
console.log('메인 코드 진행중!');
const user = getUser(1);
console.log('메인 코드 계속 진행중!');


function getUser(id, callback) {
  console.log(`Finding user with id < ${id} > in DB`);
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];

  setTimeout(() => {
    const user = users.find((user) => {
      return user.id === id;
    });
    // 여기서 준비 완료!!
    return user;
  }, 2000);
}
```

`getUser` 의 두번째 인자로, `callback` 을 추가하자. `callback` 은 우리의 비동기적 명령(`setTimeout()`)이 예약한 명령(함수)의 결과가 준비된 이후 실행할 함수다(우리가 그렇게 설계할 것이다). 즉 위 코드에서는 `return user` 직전이 되겠다! 바로 이 때 우리는 인자로 넘어온  `callback`을 실행할 것이다.

```js
console.log('메인 코드 진행중!');
getUser(1, (user) => {
  console.log(user);
});
console.log('메인 코드 계속 진행중!');


function getUser(id, callback) {
  console.log(`Finding user with id < ${id} > in DB`);
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];

  setTimeout(() => {
    const user = users.find((user) => {
      return user.id === id;
    });

    callback(user);
  }, 2000);
}
```

우리가 현재 하려는 작업은 단순 출력이기 때문에 실제 `getUser()` 호출때 출력작업만 같이 넘겨주었다.

1. `메인 코드 진행중!` 출력
2. `getUser()` 호출
   1. `setTimeout()` 을 통해 2초 후에 작업 스케줄링
   2. 2초 후에 `users` 에서 `user` 찾음.
   3. 같이 넘어온 `callback()` 실행.
   4. `callback` 내용에 따라 `user` 출력.
3. `메인 코드 계속 진행중!` 출력

---

그렇다면 이번에는, user 를 찾은 이후, 해당 user 의 `githubID` 로 github 의 모든 repos 를 찾는 함수를 작성해보자.

```js
/* main */
console.log('메인 코드 진행중!');
getUser(1, (user) => {
  console.log(user);
});
console.log('메인코드 계속 진행중!');

/* functions */
function getUser(id, callback) {
  console.log(`Finding user with id < ${id} > in DB`);
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];

  setTimeout(() => {
    const user = users.find((user) => {
      return user.id === id;
    });

    callback(user);
  }, 2000);
}

function getRepos(userID) {
  console.log(`Finding [${userID}]'s all github repos..`)
  return ['TIL', 'ES6', 'Express-demo'];
}
```

전혀 비동기 요소가 없는 함수 `getRepos()` 다. 비동기적으로 1초후에 받아오는 시뮬레이션 코드로 바꿔보자. 그리고 `getUser(1)` 을 통해 얻은 사용자의 `githubID` 로 repos 를 받아올 것(`getRepos()`)이라는 점을 참고하여 코드를 완성하자.

```js
/* main */
console.log('메인 코드 진행중!');
getUser(1, (user) => {
  const repos = getRepos(user.githubID);
  console.log(repos);
});
console.log('메인코드 계속 진행중!');

/* functions */
function getUser(id, callback) {
  console.log(`Finding user with id < ${id} > in DB`);
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];

  setTimeout(() => {
    const user = users.find((user) => {
      return user.id === id;
    });

    callback(user);
  }, 2000);
}

function getRepos(userID) {
  console.log(`Finding [${userID}]'s all github repos..`)
  setTimeout(() => {
    return ['TIL', 'ES6', 'Express-demo'];
  }, 1000);
}
```

이렇게 작성하면 될까? 아니다. `getUser()` 안의 콜백에서 결국 아까와 같은 일이 일어나게 된다.. `getCommits()` 도 작성했다.

```js
/* main */
console.log('메인 코드 진행중!');
getUser(1, (user) => {
  console.log(user);
  getRepos(user.githubID, (repos) => {
    console.log(repos);
  });
});
console.log('메인코드 계속 진행중!');

/* functions */
function getUser(id, callback) {
  console.log(`Finding user with id < ${id} > in DB`);
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];

  setTimeout(() => {
    const user = users.find((user) => {
      return user.id === id;
    });

    callback(user);
  }, 2000);
}

function getRepos(userID, callback) {
  console.log(`Finding [${userID}]'s all github repos..`)
  setTimeout(() => {
    callback(['TIL', 'ES6', 'Express-demo']);
  }, 1000);
}

function getCommits(repoName, callback) {
  console.log(`Getting all commits in repo [ ${repoName} ]`);
  setTimeout(()=>{
    callback(['Init repo', 'Add index.html', 'Struct index.html']);
  }, 1500);
}
```

### Callback 지옥

지금까지 짠 코드는 우리가 원하는 대로 잘 동작한다. 지금까지의 흐름은(시뮬레이션이기는 하지만,) DB 에서 사용자 정보를 찾고, 해당 사용자의 github id 를 통해 모든 repo 들을 가져왔다. 다음으로는, 해당 repo 들 중에서 첫번째 repo 에 담긴 모든 commit 들을 가져오고 싶다! `getCommit()` 코드를 작성해서 한 단계 더 깊은 코드를 만들어 봤다.

`callback.js`

```js
// 가로로 Christmas 트리를 만드는중이다.
getUser(1, (user) => {
  getRepos(user.githubID, (repos) => {
    getCommits(repos[0], (commits) => {
      console.log(commits);
    })
  });
});

/* functions */
function getUser(id, callback) {
  console.log(`Finding user with id [ ${id} ] in DB`);
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];

  setTimeout(() => {
    const user = users.find((user) => {
      return user.id === id;
    });

    callback(user);
  }, 2000);
}

function getRepos(userID, callback) {
  console.log(`Finding [ ${userID} ]'s all github repos..`)
  setTimeout(() => {
    callback(['TIL', 'ES6', 'Express-demo']);
  }, 1000);
}

function getCommits(repoName, callback) {
  console.log(`Getting all commits in repo [ ${repoName} ]`);
  setTimeout(()=>{
    callback(['Init repo', 'Add index.html', 'Struct index.html']);
  }, 1500);
}
```

 아래코드는 따로 복사해서 저장해 놓자.

```sh
$ pwd
.../SyncAsync/callback.js
$ cp callback.js callback-hell.js
$ ls
callback.js			callback-hell.js	  	sync.js	
```

이게 만약 동기적으로 작동하는(일반 프로그래밍 언어로 작성한) 코드였다면, 아래와 같은 코드로 구성되었을 것이다.

```ruby
user = getUser(1)
repos = getRepos(user[githubID])
commits = getCommits(repos[0])
```

> Callback HELL  (동기천국 콜백지옥)



## 패턴2: Promise

**Promise : 비동기작업에서 언젠가 일어날 결과 (eventual result)** 를 잡고있다. 

| 경우(Case)    | 결과(Consequence) |
| ------------- | ----------------- |
| 성공(Success) | 값(Value)         |
| 실패(Fail)    | 에러(Error)       |

사실 어떤 작업이던지 2가지의 경우밖에 없긴 하다… promise 는 성공했을 때는 값을, 실패했을 때는 에러를 갖게되고, 어느것이라도 될 수 있다. promise 비동기 작업의 결과로 값/에러 둘중 하나를 줄것을 약속(promise)한다. 이 Promise 인스턴스는 3가지 상태중에 하나일 수 밖에 없다.

|  현재   |         진행          |            결과             |
| :-----: | :-------------------: | :-------------------------: |
| Pending | = Async Operation =>  | 1) Resolved/Fulfilled(성공) |
| 대기중  | = 비동기 작업 실행 => |      2) Rejected(실패)      |

어떻게 보면 너무 당연한 이야기다. 이제 코드로 살펴보도록 하자.

```sh
$ pwd
.../.../SyncAsync
$ touch promise.js
```

`SyncAsync/promise.js`

```js
const promise = new Promise((resolve, reject) => {
  // Async 작업 시작
  // ...

});
```

promise 는 이렇게 구성된다. 당연하지만, `promise` 는 값(value) 혹은 에러(error) 둘중에 하나를 반드시 가지게 될것이다. 뭐가 될지 모르지만 둘중에 하나를 가지게 될것이라는 약속(promise)! 

 만약 성공해서 값을 가지게 된다면, 우리는 `promise` 의 소비자(consumer)에게 값을 return 하고싶을 것이다. 때문에 코드 어디선가는 우리 promise 를 소비해야 한다. 왜냐하면, `promise` 는 async 작업의 결과물을 줄것을 약속하고 있기 때문에 이 약속받은 결과를 받아내야 한다. 

그러면 이제 결과를 소비자에게 어떻게 보내게 되는지를 알아보자. 방법은 다름아닌 `(resolve, reject)` 안에 있다.이 두 가지는 모두 함수다.

```js
 const promise = new Promise((resolve, reject) => {
  // Async 작업 시작
  // ...
  resolve("HappyHacking! ٩(ᐛ)و ");
  reject(new Error('Unhappy Error.. ( •́ ̯•̀  )')); // 단순 메세지보다 Error객체!
});
```

이해하기 어려운 코드는 아니다. `promise` 는 각 경우마다 값을 가지고 있는 것인데, 성공하면 `HappyHacking! ٩(ᐛ)و ` 을, 실패하면 `Unhappy Error.. ( •́ ̯•̀  )` 라는 에러를 갖게 된다. 

실제 프로그램에서는 성공시 이런 string 보다는, user 정보를 담고있는 object 를 갖게 될것이다. promise 를 만들었다면, 이 promise 를 소비해보자.

```js
const promise = new Promise((resolve, reject) => {
  // Async 작업 시작
  // ...
  resolve("HappyHacking! ٩(ᐛ)و ");
  // reject(new Error('Unhappy Error.. ( •́ ̯•̀  )')); // 단순 메세지보다 Error객체!
});

promise
  .then(result => console.log('성공!! ', result));
  .catch(error => console.error('실패ㅠ ', error));
```

```js
const promise = new Promise((resolve, reject) => {
  // Async 작업 시작
  // ...
  // resolve("HappyHacking! ٩(ᐛ)و ");
  reject(new Error('Unhappy Error.. ( •́ ̯•̀  )')); // 단순 메세지보다 Error객체!
});

promise
  .then(result => console.log('성공!! ', result));
  .catch(error => console.error('실패ㅠ ', error));
```

실행해보면 바로 감이 온다. promise 는 우리에게 async 작업 결과물을 줄 것을 약속하지만, 그 결과물이 성공해서 값이 될지, 실패새서 에러가 될지는 우리가 알수 없다. 때문에 각 시나리오별로 어떻게 대처할지는 우리의 몫이다. 좀 더 실제 상황처럼 만들어보자.  

``` js
const getAccoount = new Promise((resolve, reject) => {
  setTimeout(() => {
    const number = Math.floor(Math.random() * 100);
    if (number % 2 === 1) resolve({ id: 1, email: 'neo@hphk.kr' });
    else reject(new Error('Can not access Lost Arc API'));
  }, 1000);
});

getAccoount
  .then(result => console.log(`Success: [ ${result.email} ]`))
  .catch(error => console.error('Fail: ', error));
```

동시접속자가 너무 많아서 계속해서 터지는 서버에서 API 를 통해 계정정보를 불러오는 상황을 시뮬레이팅 하는 코드다.

다시 정리해보자. promise 는 이후에 일어날 결과에 대한 값을 잡고있다. 기본적으로 생성할 때는 pending state 이며 생성할 때, 성공(resolved, fulfilled)했을 경우의 값과 실패(rejected)했을 때 소비할 값을 지정해 놓을 수 있다.

이후 이 promise 를 소비할 때 두가지 시나리오에 대하여 각각 `.then` 과 `.catch` 를 통해 이후에 실행할 코드를 작성할 수 있다. 당장은 불가능할지 모르지만, 만약 우리가 생성한 함수가  `callback` 을 받게된다면, 이 코드는 `new Promise` 로 수정해야 한다.

### CallBack => Promise

아까 복사해 놓은 `callback-hell.js` 를 복사하고 Promise 로 바꿔보자.

```sh
$ cp callback-hell.js hell-to-promise.js
```

우선 실행(소비) 부분은 제외하고 함수들만 바꿔보자.

`…/SyncAsync/callback-to-js`

```js
...
/* functions */
function getUser(id, callback) {
  console.log(`Finding user with id [ ${id} ] in DB`);
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];

  setTimeout(() => {
    const user = users.find((user) => {
      return user.id === id;
    });
    
    callback(user);
  }, 2000);
}
...
```

```js
...
/* functions */
function getUser(id) {
  console.log(`Finding user with id [ ${id} ] in DB`);
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];
  
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const user = users.find((user) => {
        return user.id === id;
      });
      if(user) resolve(user);
      else reject(new Error(`Can not find User with ID [ ${id} ]`))
    }, 2000);
  });
}
...
```

이제 실패했을 경우도 분기 할 수 있으니 `reject` 도 사용해 보았다. 나머지는 직접 바꿔보자.

```js
...
/* functions */
function getUser(id) {
  console.log(`Finding user with id [ ${id} ] in DB`);
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];
  
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const user = users.find((user) => {
        return user.id === id;
      });
      if(user) resolve(user);
      else reject(new Error(`Can not find User with ID [ ${id} ]`))
    }, 2000);
  });
}

function getRepos(userID) {
  console.log(`Finding [ ${userID} ]'s all github repos..`)
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(['TIL', 'ES6', 'Express-demo']);
      // reject(new Error('Can not get repos'));
    }, 1000);
  });
}

function getCommits(repoName) {
  console.log(`Getting all commits in repo [ ${repoName} ]`);
  return new Promise((resolve, reject) => {
    setTimeout(()=>{
      resolve(['Init repo', 'Add index.html', 'Struct index.html']);
      // reject(new Error('Can not get commits'));
    }, 1500);
  });
}
```

### Promise 소비하기

이제 Promise 를 return 하도록 바꾼 코드를 실행하여 promise 를 소비하는 방법을 알아보자.

```js
// Callback HELL
getUser(1, (user) => {
  getRepos(user.githubID, (repos) => {
    getCommits(repos[0], (commits) => {
      console.log(commits);
    })
  });
});
...
```

Test 를 위해 하나만 실행해 보도록 하자.

```js
// Promise
const userPromise = getUser(1);
userPromise.then(user => console.log(user));
...
```

잘 나온다면, 이제 코드를 좀 더 단순하게 만들어보자.

```js
// Promise
getUser(1)
	.then(user => console.log(user));
```

좋다! 아주 잘 동작한다. 그런데 원래 우리는 찾은 `user` 를 가지고 `getRepos()` 를 호출했다. 그렇다면 아래 코드의 결과는 무엇일까?

```js
// Promise Check
const a = getUser(1)
  .then(user => getRepos(user.githubID));
console.log(a); // Promise { <pending> }
```

그렇다! `getUser(1).then(user => getRepos(user.githubID))` 에는 뭐가 될지는 모르겠지만 결국 Promise 를 return 하고 있다. 결국 `.then()` 의 결과물도 promise 이므로,

```js
// Promise Chaining
getUser(1)
  .then(user => getRepos(user.githubID))
  .then(repos => getCommits(repos[0]))
  .then(commits =>  console.log(commits));
```

로 계속해서 Chaining 이 가능하다! Callback HELL 과 비교해 보면 훨씬 깔끔하다. 마지막으로 error 가 나올 경우 에러를 체이닝 해주면 된다. 3가지중 어느것이 되어도 실패하면 `.then` 을 무시하고 `.catch` 로 향할 것이기 때문에 한번만 적어주면 된다.

```js
// Promise Chaining
getUser(1)
  .then(user => getRepos(user.githubID))
  .then(repos => getCommits(repos[0]))
  .then(commits =>  console.log(commits))
  .catch(error => console.error(error.message));
```

아무 `reject()` 를 주석 풀고 `resolve()` 를 주석 처리하거나, `getUser(3)` 과 같이 존재하지 않는 id 로 사용자를 찾아보자. (`error vs error.message`)



## 패턴3: Async & Await

기존에 `hell-to-promise.js` 의 코드를 더 쉽게 바꿀 수 있다. ES6 에 새롭게 추가된 `async`/`await` 기능 덕분이다. 

 `async`/`await`  를 사용하면 마치 동기 코드를 작성하듯 코드를 작성할 수 있다.

```sh
$ pwd
.../SyncAsync/
$ cp hell-to-promise async-await.js
```

```js
/* Promise Chaining
getUser(1)
  .then(user => getRepos(user.githubID))
  .then(repos => getCommits(repos[0]))
  .then(commits =>  console.log(commits))
  .catch(error => console.error(error.message));
*/

/* Async and Await approach */
const user = await getUser(1);
const repos = await getRepos(user.githubID);
const commits = await getCommits(repos[0]);
console.log(commits);

/* functions */
function getUser(id) {
  console.log(`Finding user with id [ ${id} ] in DB`);
  const users = [
    { id: 1, githubID: 'neo' },
    { id: 2, githubID: 'john' },
  ];

  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const user = users.find((user) => {
        return user.id === id;
      });
      if(user) resolve(user);
      else reject(new Error(`Can not find User with ID [ ${id} ]`))
    }, 2000);
  });
}

function getRepos(userID) {
  console.log(`Finding [ ${userID} ]'s all github repos..`)
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(['TIL', 'ES6', 'Express-demo']);
      // reject(new Error('Can not get repos'));
    }, 1000);
  });
}

function getCommits(repoName) {
  console.log(`Getting all commits in repo [ ${repoName} ]`);
  return new Promise((resolve, reject) => {
    setTimeout(()=>{
      resolve(['Init repo', 'Add index.html', 'Struct index.html']);
      // reject(new Error('Can not get commits'));
    }, 1500);
  });
}

```

정말로 동기코드처럼 보인다! 다만 `await` 는 어디있지?

`async` 는 `await` 데코레이터를 사용한 함수 안에서만 사용할 수 있다. 그러므로 우리 코드가 최종적으로 하려는 일이 `commits`를 출력하는 거라면 이 모든 작업을 `displayCommits()` 라는 함수를 정의 해 그 안에 넣고 `displayCommits()`를 `async` 데코레이터로 감싸주면 된다. 

```js
displayCommits()
  .then(result => console.log(result));

async function displayCommits() {
  const user = await getUser(1);
  const repos = await getRepos(user.githubID);
  const commits = await getCommits(repos[0]);
  console.log(commits);
}

/* functions */
...
```

기본적으로, 모든 async 함수들은 promise 를 리턴한다. 하지만 아무 기능도 없기때문에 `.then` 을 사용하지 않아도 된다. 마치 동기 코드처럼 보이지만, 실제로는 비동기로 작동한다는 것을 잊지 말자.

```sh
$ node async-await.js
Finding user with id [ 1 ] in DB
Finding [ neo ]'s all github repos..
Getting all commits in repo [ TIL ]
[ 'Init repo', 'Add index.html', 'Struct index.html' ]
undefined # .then()
```

마지막으로, `async` 에서는 `.catch` 를 사용할 수 없다. 하지만 에러 핸들링은 필요하다. 때문에 `async` 에서는 `try`/`catch` 블록을 사용한다.

```js
...
async function displayCommits() {
  try{
    const user = await getUser(3); // 3번으로 reject 시켜보자.
    const repos = await getRepos(user.githubID);
    const commits = await getCommits(repos[0]);
    console.log(commits);
  } catch (error) {
    console.error(error.message)
  }
}
...
```

## Exercise

```js
// to async-await
getCustomer(1, (customer) => {
  console.log('Customer: ', customer);
  if (customer.isGold) {
    getTopMovies((movies) => {
      console.log('Top movies: ', movies);
      sendEmail(customer.email, movies, () => {
        console.log('Email sent...')
      });
    });
  }
});

function getCustomer(id, callback) {
  setTimeout(() => {
    callback({ 
      id: 1, 
      name: 'Mosh Hamedani', 
      isGold: true, 
      email: 'email' 
    });
  }, 4000);  
}

function getTopMovies(callback) {
  setTimeout(() => {
    callback(['movie1', 'movie2']);
  }, 4000);
}

function sendEmail(email, movies, callback) {
  setTimeout(() => {
    callback();
  }, 4000);
}
```

```js
async function notifyCustomer() {
  try {
    const customer = await getCustomer(1);
    console.log('Customer: ', customer);
    if (customer.isGold) {
      const movies = await getTopMovies();
      console.log('Top movies: ', movies);
      await sendEmail(customer.email, movies);
      console.log('Email sent...');
    }
  } catch (error) {
    console.error(error.message)
  }
}

notifyCustomer();


function getCustomer(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({ 
        id: 1, 
        name: 'Mosh Hamedani', 
        isGold: true, 
        email: 'email' 
      });
    }, 4000);  
  });
}

function getTopMovies() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(['movie1', 'movie2']);
    }, 4000);
  });
}

function sendEmail(email, movies) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, 4000);
  });
}
```

