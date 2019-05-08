// rest operator 이 없다면

function addAll(a, b, c, d, e) {
        const numbers = [a, b, c, d, e];
        let acc = 0
        for (const number of numbers) {
            acc += number;
        }
        return acc;
}

// rest operator 이 있다면

function addAll(...numbers) {
    let acc = 0
    for (const number of numbers) {
        acc += number;
    }
    return acc;
}

console.log(addAll(1, 2, 3, 4, 5, 6, 7, 8));

const a1 = [1, 2, 3, 4, 5];
const a2 = [6, 7, 8, 9, 10];
const a3 = [...a1, ...a2]; // [1,2,3,4,5,6,7,8,9,10]

console.log(a3);



first0last100 = (...numbers) => {
    return [0, ...numbers, 100]
};

console.log(first0last100(4,5,6,7,8,9,12));