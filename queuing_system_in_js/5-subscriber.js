const redis = require('redis')

const cli = redis.createClient()

cli.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});
  
cli.on('connect', () => {
    console.log('Redis client connected to the server');
});

const CHANNEL = "holberton school channel"

cli.subscribe(CHANNEL)

cli.on("message",(channel, message)=>{
    if(channel == "KILL_SERVER"){
        cli.unsubscribe(channel);
        cli.quit();
    }
    console.log(message); 
})

