const fs = require('fs');
var argv = require('minimist')(process.argv.slice(2));

const rawData = fs.readFileSync(argv.s || argv.spec, 'utf8');
const apiSpec = JSON.parse(rawData);

const info = {
    title: "Bandwidth",
    description: "Bandwidth's Communication APIs",
    contact: {
        name: "Bandwidth",
        url: "https://dev.bandwidth.com",
        email: "letstalk@bandwidth.com"
    },
    version: "1.0.0",
}

apiSpec.info = info;

fs.writeFileSync(argv.s || argv.spec, JSON.stringify(apiSpec), 'utf8');
