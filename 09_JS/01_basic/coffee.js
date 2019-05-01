function makeCoffee(order, serve) {
    let cup;
    // 커피 밑에 두는 시간
    setTimeout(() => {
        cup = order;
        serve(cup)
    }, 2000);

    return cup;
}

// console.log(makeCoffee('Latte'));

const myCoffee = makeCoffee('latte', console.log);
// console.log(myCoffee);