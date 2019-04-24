const myObject = {
    coffee: 'CafeLatte',
    iceCream: 'CherryIceCream',
};

const jsonData = JSON.stringify(myObject);
console.log(typeof jsonData); // string

const parseData = JSON.parse(jsonData);
console.log(typeof parseData);  // object