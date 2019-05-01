console.log('메인 코드 진행중!');
const user = getUser(1);
console.log(user);
console.log('메인 코드 계속 진행중!');

function getUser(id) {
    const users = [
        { id: 1, githubID: 'neo'},
        { id: 2, githubID: 'john'},
    ];
    setTimeout(() => {
        return users.find((user) => {
            return user.id === id;
        });
    }, 2000)
}
