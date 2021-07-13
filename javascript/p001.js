/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
 */
/* 100, 2318 */
function checkMultiples(n) {
    var s = 0;
    n = n -1;
    sum3 = Math.floor(3 * ((n/3) * ((n/3) + 1) ) / 2);
    sum5 = Math.floor(5 * ((n/5) * ((n/5) + 1) ) / 2);
    sum35 = Math.floor(15 * ((n/15) * ((n/15) + 1) ) / 2);
    s = sum3 + sum5 - sum35;
    console.log(s)
}

//n(n + 1)/2

checkMultiples(100)