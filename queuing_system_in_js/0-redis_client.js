const redis = require('redis')

const cli = redis.createClient();

cli.on('error', (err) => {
    console.log(`redis client not connected to the server: ${err}`)
});

cli.on("connect",()=>{
    console.log('Redis client connected to the server');
})

