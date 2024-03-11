
// read whole_quran.json file with ascii encoding
const fs = require('fs');
const path = require('path');
const wholeQuran = fs.readFileSync(path.join(__dirname, 'whole_quran.json'), 'ascii');

// parse the whole_quran.json file
const wholeQuranParsed = JSON.parse(wholeQuran);
console.log(wholeQuranParsed.fatihah);