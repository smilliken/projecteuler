fs = require('fs');

var range = function(start, end) {
    var ret = [];
    for (var i = start; i <= end; i++)
        ret.push(i);
    return ret;
};

var count = function(str, substr){
    var cnt = 0;
    var lastIdx = 0;
    while (str.indexOf(substr, lastIdx) >= 0) {
        cnt += 1;
        lastIdx = str.indexOf(substr, lastIdx) + 1;
    }
    return cnt;
};

var max = function(array, predicate) {
    var highScore = null;
    var highVal = null;
    for (var i = 0; i < array.length; i++) {
        var score = predicate(array[i]);
        if (highScore == null || score > highScore) {
            highScore = score;
            highVal = array[i];
        }
    }
    return highVal;
};

var sum = function(array) {
    var total = 0;
    for (var i = 0; i < array.length; i++)
        total += array[i];
    return total;
};

var decrypt = function(ciphertext, key) {
    var plaintext = [];
    for (var i = 0; i < ciphertext.length; i++)
        plaintext.push(String.fromCharCode(ciphertext[i] ^ parseInt(key[i % key.length])));
    return plaintext.join('');
};

var ciphertext = fs.readFileSync('cipher1.txt').toString().split(',');
var lowerAlpha = range('a'.charCodeAt(), 'z'.charCodeAt());
var keys = [];
for (var c1 = 0; c1 < lowerAlpha.length; c1++)
    for (var c2 = 0; c2 < lowerAlpha.length; c2++)
        for (var c3 = 0; c3 < lowerAlpha.length; c3++)
            keys.push([lowerAlpha[c1], lowerAlpha[c2], lowerAlpha[c3]]);

var candidates = [];
for (var keyIdx = 0; keyIdx < keys.length; keyIdx++) {
    candidates.push(decrypt(ciphertext, keys[keyIdx]));
}

plaintext = max(candidates, function(candidate){ return count(candidate, ' and ');});
console.log(sum(plaintext.split('').map(function(char){ return char.charCodeAt(); })));