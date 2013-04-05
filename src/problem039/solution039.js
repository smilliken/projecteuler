var perims = {};
var limit = 1000;

for (var a = 1; a < limit; a++) {
    for (var b = 1; b <= a; b++) {
        var c = Math.sqrt(a * a + b * b);
        var p = parseInt(a + b + c);
        if (c == parseInt(c) && p <= limit) {
            perims[p] = 1 + (perims[p] || 0);
        }
    }
}
var max;
for (var p in perims) {
    if (!max || perims[p] > perims[max])
        max = p;
}
console.log(max);