let sinon = require("sinon");
let expect = require("chai");

let sendPaymentRequestToApi = require("./3-payment")
let untils = require("./utils")

// import sinon from "sinon";
// import { expect } from "chai";

// import {sendPaymentRequestToApi} from "./3-payment.js";
// import {Utils} from "./utils.js";

describe("sendPaymentRequestToApi",()=>{
    it('should call the payment api',()=>{
        const utils = new untils();
        const spy = sinon.spy(utils,"calculateNumber")
        const api = sendPaymentRequestToApi(100, 20);
        
        expect(spy.calledOnceWith("SUM",100,20)).to.be.true
        expect(utils.calculateNumber('SUM', 100, 20)).to.equal(api);

        spy.restore();
    })
})
