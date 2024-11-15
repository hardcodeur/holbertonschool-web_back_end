const assert = require('assert');
const request = require('request');

describe('#router.get(/)',()=>{
    it("Should return status code 200",(done)=>{
        request.get("http://localhost:7865",(error, response, body)=>{
            assert.equal(response.statusCode,200)
            done();
        })
    })

    it("Should return welcome sentence",(done)=>{
        request.get("http://localhost:7865",(error, response, body)=>{
            assert.equal(body,"Welcome to the payment system")
            done();
        })
    })
})
