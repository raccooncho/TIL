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

getUser(1)
    .then(user => getRepos(user))  // if (user) => resolve user
    .then(repos => getCommits(repos[0]))
    .then(commits => console.log(commits.length))
    .catch(err => console.error(err));  // else => reject error

