// ES5 for loop
// var products = [
//     {name: 'cucumber', type:'vege'},
//     {name: 'banana', type:'fruit'},
//     {name: 'carrot', type:'vege'},
//     {name: 'tamato', type:'vege'},
// ];
// var fruits = [];
// for (var i = 0; i < products.length; i++) {
//     if (products[i].type === 'fruit') {
//         fruits.push(products[i]);
//     }
// }
// console.log(fruits);



// ES6+
const products = [
    {name: 'cucumber', type:'vege'},
    {name: 'banana', type:'fruit'},
    {name: 'carrot', type:'vege'},
    {name: 'tamato', type:'vege'},
];
const fruits = products.filter(product => {
    // 해당 조건문에서 true가 나오면  return
    return product.type === 'fruit'
});
console.log(fruits);

const users = [
    {id: 1, admin: true},
    {id: 2, admin: false},
    {id: 3, admin: true},
    {id: 4, admin: false},
    {id: 5, admin: false},
];
const adminUsers = users.filter(user => {
    return user.admin;
});
console.log(adminUsers);