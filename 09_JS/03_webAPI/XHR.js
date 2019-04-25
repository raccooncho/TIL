const DOMAIN = 'https://jsonplaceholder.typicode.com/';
const RESOURCE = 'posts';
const QUERY_STRING = '/';

const URL = DOMAIN + RESOURCE + QUERY_STRING;
// req 대리인 XHR 객체 생성
const XHR = new XMLHttpRequest();
// XHR 요청 발사 준비 (method, url)

// 요청을 만들고, 정보를 담고, 보내고, 기다리고, 처리한다.
XHR.open('POST', URL);

XHR.setRequestHeader(
    'Content-Type',
    'application/json;charset=UTF-8'        // POST처리를 보내기 위해서 전송하는 정보의 형태를 json으로 가공해 줘야 한다.
);
// XHR 요청 발사!
XHR.send(
    JSON.stringify({ "title": "NewPost", "body": "This is New Post", "userId": 1 })  // POST보내기 위해서 정보를 답아야 한다.
);

XHR.addEventListener('load', e => {
    const parseData = JSON.parse(e.target.response);
    console.log(parseData)
});