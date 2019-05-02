const utility = require('./utility');

const accountA = 100;
const accountB = 200;
const accountC = 400;
const totalBalance = utility.addAll([accountA, accountB, accountC]);
const allMul = utility.mulAll([accountA, accountB, accountC]);
console.log(totalBalance);
console.log(allMul);
console.log(utility.name);