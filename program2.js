const args = process.argv.slice(2);
let words = [];
let output = [];

// preprocessing
for (let word of args){
    words.push(word.split(' '))
}

words = words.flat(Infinity);
console.log(words)

for (let word of words){
    let counter = 0
    for (let word2 of words){
        if (word.toLowerCase()==word2.toLowerCase()){
            counter ++
        }
    }
    if ((counter >= 2) && !(output.includes(word.charAt(0).toUpperCase() + word.slice(1)) | output.includes(word.toLowerCase()))){
        output.push(word);
    }
}

for (let out of output){
    console.log(out)
}
