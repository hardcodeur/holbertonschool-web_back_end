const redis = require('redis')

const cli = redis.createClient();

function setNewSchool(schoolName,value) {
    cli.set(schoolName,value,redis.print);
}
function displaySchoolValue(schoolName) {
    cli.get(schoolName, (err, res) => {
        console.log(res);
    });
}

cli.on('error', (err) => {
    console.log(`redis client not connected to the server: ${err}`)
});

cli.on("connect",()=>{
    console.log('Redis client connected to the server');
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

