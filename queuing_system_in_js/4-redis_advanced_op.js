const redis = require('redis')

const cli = redis.createClient();

cli.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});
  
cli.on('connect', () => {
    console.log('Redis client connected to the server');
});

const key = "HolbertonSchools"

let data = [
    ["Portland",50],
    ["Seattle",80],
    ["New York",20],
    ["Bogota",20],
    ["Cali",40],
    ["Paris",2],
]

cli.del(key)

data.forEach(elt=>{
    cli.hset(key,elt[0],elt[1],redis.print)
})

cli.hgetall(key,(err, object)=>{
    console.log(object);
})