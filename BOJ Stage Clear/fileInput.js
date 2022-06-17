const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split('\n');


let T = +input[0];


for (let i = 1; i < T+1; i++) {
    let n,m = 0;
    [n, m] = input[i].split(" ").map(ele => +ele);
    console.log(combination(m,n));
}

function combination(n,m) {
    n = Number(n); m = Number(m);
    let a = 1; let b = 1;
    if (m >= n/2+0.5) {
        m = n-m;
    }
    for (let i = 1; i <= m; i++) {
        a *= n;
        b *= i;
        n --;
    }
    return a/b;
}
