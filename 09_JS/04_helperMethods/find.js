// ES5 for loop
// var avengers = [
//     {name: 'Tony Stark'},
//     {name: 'Steve Rogers'},
//     {name: 'Thor'}
// ];
// var avenger;
// for (var i = 0; i < avengers.length; i++) {
//     if (avengers[i].name === 'Tony Stark') {
//         avenger = avengers[i];
//         break;
//     }
// }
// console.log(avenger);



// ES6+
const avengers = [
    {name: 'Tony Stark'},
    {name: 'Steve Rogers'},
    {name: 'Thor'}
    ];

const a = avengers.find(avenger => avenger.name === 'Tony Stark');
console.log(a);