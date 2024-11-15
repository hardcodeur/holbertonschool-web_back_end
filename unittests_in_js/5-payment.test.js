const sinon = require('sinon');

const sendPaymentRequestToAPI = require('./5-payment');

describe("sendPaymentRequest",()=>{
    let spy;
    
    beforeEach(function () {
        spy = sinon.spy(console, 'log');
    });

    afterEach(function () {
        sinon.assert.calledOnce(spy)
        spy.restore();
    });

    it("Should log the total when the values are 100 and 20",()=>{
        sendPaymentRequestToAPI(100,20)
        sinon.assert.calledWithExactly(spy, 'The total is: 120');
    })

    it("Should log the total when the values are 10 and 10 ",()=>{
        sendPaymentRequestToAPI(10,10)
        sinon.assert.calledWithExactly(spy, 'The total is: 20');
    })

})