console.log('메인 코드 진행중!');
const user = getUser(1);
console.log('메인 코드 계속 진행중!');

function getUser(id, callback) {
    console.log(`Finding user with id < ${id} > in DB`);
    const users = [
        {id: 1, githubID: 'neo'},
        {id: 2, githubID: 'john'},
    ];

    setTimeout(() => {
        const user = users.find((user) => {
            return user.id === id;
        });
        return user;
    }, 2000);
}