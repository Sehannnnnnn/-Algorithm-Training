// let fs = require("fs");
// let input = fs.readFileSync('/dev/stdin').toString().split(' ');

// let num = Number(input);

function goldminsu(n) {
    let gold = 0;
    for (let i = n; i>=4; i--) {
        if (checkGold(i)) gold = i;
    }
    return gold;
}

function checkGold (n) {
    let a = String(n);
    for (_ of a) {
        if(not.includes(_)) return false
    } 
    return true;
}

const not = ['0','1','2','3','5','6','8','9'];

console.log(goldminsu(100));