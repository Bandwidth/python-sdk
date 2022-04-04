const fs = require('fs');
const yaml = require('js-yaml');
var argv = require('minimist')(process.argv.slice(2));

const configFile = yaml.load(fs.readFileSync(argv.c || argv.config, 'utf8'));

for (i in configFile.inputs) {
    let rawData = fs.readFileSync(configFile.inputs[i].inputFile);
    let apiSpec = JSON.parse(rawData);
    servers = apiSpec.servers;

    for (path in apiSpec.paths) {
        apiSpec.paths[path].servers = servers;
    }

    delete apiSpec.info;
    delete apiSpec.servers;

    fs.writeFileSync(configFile.inputs[i].inputFile, JSON.stringify(apiSpec), 'utf8');
}
