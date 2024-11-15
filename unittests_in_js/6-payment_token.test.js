const assert = require('assert');
const getPaymentTokenFromAPI = require("./6-payment_token");

describe("#getPaymentTokenFromAPI()",()=>{

    it("should return promise when success is true",()=>{
        getPaymentTokenFromAPI(true).then(
            (rep)=>{
                assert.equal(rep,{ data: 'Successful response from the API' })
                done();
            }
        );
    })

    it("should return promise when success is false",()=>{
        getPaymentTokenFromAPI(false).then(
            (rep)=>{
                assert.equal(rep,{})
                done();
            }
        );
    })
})
