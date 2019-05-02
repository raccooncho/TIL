// function addAll (numbers=[]) {
//     let sum = 0;
//     numbers.forEach(number => sum += number);
//     return sum;
// }
//
// function mulAll(number=[]){
//     let mul = 0;
//     numbers.forEach(number => mul *= number);
//     return mul;
// }

module.exports = {
    addAll (numbers=[]) {
        let sum = 0;
        numbers.forEach(number => sum += number);
        return sum;
    },
    mulAll (numbers=[]) {
        let mul = 1;
        numbers.forEach(number => mul *= number);
        return mul;
    },
    name: 'Cho'
};

phoneNumber = '01012345678';

module.exports.phoneNumber = phoneNumber;