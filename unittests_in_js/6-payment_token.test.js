const { expect } = require('chai');
const getPaymentTokenFromAPI = require("./6-payment_token");

describe("#getPaymentTokenFromAPI()",()=>{

    it("should return promise when success is true",()=>{
        getPaymentTokenFromAPI(true).then(
            (rep)=>{
                expect(rep).to.eql({ data: 'Successful response from the API' });
                done();
            }
        );
    });
})
