// callback.js 는 예전에 함수가 크리스마스 트리구조가 필수적이여서 가독성이 떨어졌다. ==> 이를 해결하기 위해 새로운 접근

const getUser = id => {
    const users = [
        { id: 1, githubID: 'eduyu' },
        { id: 2, githubID: 'edujohn' },
    ];

    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            const user = users.find(user => user.id === id);
            if (user) resolve(user);
            else reject(new Error(`Can't find user ${id}`));
        }, 2000)
    });
};

const getRepos = user => {
    const repos = ['TIL', 'Workshop_HW', 'Python', 'JS'];
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (repos) resolve(repos);
            else reject(new Error('No REPOs'))
        });
    });
};

const getCommits = repo =>  {
    const commits = ['Init repo', 'Make index.html'];

    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            if (commits) {
                resolve(commits);
            } else {
                reject(new Error('ERRRRRRORRR'));
            }
        }, 2000)
    });
};


// 함수한에 unblocking 하게 있는 요소가 최소 하나라도 있다면
async function main () {  // async 는 Promise 가 있을 때만 !
    try {  // 성공했을 때 (resolve)
        const user = await getUser(1);
        const repos = await getRepos(user);
        const commits = await getCommits(repos[0]);
        console.log(commits.length)
    } catch (e) {  // 실패했을 때 (reject)
        console.log(e);
    }
}

main();


