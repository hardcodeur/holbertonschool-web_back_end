import { createClient } from 'redis';

const cli = createClient();

cli.on('error', (err) => {
    console.log(`redis client not connected to the server: ${err}`)
});

cli.on("connect",()=>{
    console.log('Redis client connected to the server');
})