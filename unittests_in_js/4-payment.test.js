let sinon = require("sinon");
let expect = require("chai").expect;

let sendPaymentRequestToApi = require("./3-payment")
let Untils = require("./utils")

// import sinon from "sinon";
// import { expect } from "chai";

// import {sendPaymentRequestToApi} from "./3-payment.js";
// import {Utils} from "./utils.js";

describe("sendPaymentRequestToApi",()=>{
    it('should call the payment api',()=>{
        const utils = new Utils();
        const stub = sinon.stub(utils,"calculateNumber").returns(10);
        const spy = sinon.spy(console, "log");
        
        const api = sendPaymentRequestToApi(100, 20);

        expect(stub.calledOnceWithExactly("SUM",100,20)).to.be.true;
        expect(spy.calledOnceWithExactly("The total is: 10")).to.be.true;
        expect(utils.calculateNumber('SUM', 100, 20)).to.equal(api);

        spy.restore();
        stub.restore();
        
    })
})
