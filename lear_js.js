/* Closure
function makeCounter() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}

const counter1 = makeCounter();
console.log(counter1()); // 1
console.log(counter1()); // 2
console.log(counter1()); // 3

const counter2 = makeCounter();
console.log(counter2()); // 1 — новий лічильник

function makeDecrementer() {
    let count = 10;
    return function() {
        if (count > 0) {
            count--;
            return count;
        }
    }
}
const decrementer = makeDecrementer();
console.log(decrementer()); // 9
console.log(decrementer()); // 8    
console.log(decrementer()); // 7
*/
