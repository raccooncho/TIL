// const hi = () => {
//
// };
//
//
// const bye = () => {
//
// };

const me = {
    name: 'mnoko',
    phone: '010 1234 5678',
    email: 'mnoko@naver.com',
    intro: function () {
        return `hi my name is ${this.name} !!`
    }
};

const you = {
    name: 'zaqwes',
    phone: '010 2222 3333',
    email: 'mnoko@naver.com',
    intro: () => {
        return `Hi my name is ${this.name} !!`
    },
    wait: function () {
        setTimeout(() => {
            console.log(this.email)
        }, 1000)
    }

};

console.log(me.intro());
console.log(you.intro());
console.log(you.wait());
