const numbers = [1, 2, 3, 4];

numbers[0];   // 1

// numbers[-1];  // undefined

numbers.length;     // 4

/*
원본이 달라지는 methods
 */
numbers.reverse();  // [4, 3, 2, 1] return 후 numbers의 배열을 [4, 3, 2, 1]로 변경
numbers.reverse();

numbers.push('a'); // return 5 -> 바뀐 길이
// [1, 2, 3, 4, 'a']

numbers.pop();  // return 'a'
// [1, 2, 3, 4]

numbers.unshift('a') // return 5 -> 바뀐 길이
// ['a', 1, 2, 3, 4]

numbers.shift(); // return 'a'
// [1, 2, 3, 4]

/*
Copy,  다른 결과 return
 */

numbers.includes(1);   // true
// [1, 2, 3, 4]

numbers.includes(0);    // false

numbers.push('a', 'a');
numbers.indexOf('a');   // 4 -> 처음에 나오는 'a'에 대해서 index를 구해줌
numbers.indexOf('b');   // -1 -> 존재하지 않음

numbers.join('-');  // '1-2-3-4-a-a' -> join 임
numbers.join();     // '1,2,3,4,a,a'

