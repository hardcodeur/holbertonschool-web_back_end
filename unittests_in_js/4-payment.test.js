const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
	it('Should call the payment api', () => {
		const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
		const spy = sinon.spy(console, 'log');

		sendPaymentRequestToApi(100, 20);

		sinon.assert.calledWithExactly(stub, 'SUM', 100, 20);
		sinon.assert.calledWithExactly(spy, 'The total is: 10');

		stub.restore();
		spy.restore();
	});
});