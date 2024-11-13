// let Untils = require("./utils")
import { Utils } from './utils.js';

export function sendPaymentRequestToApi(totalAmount,totalShipping)

{   
    let util = new Utils
    let result= util.calculateNumber("SUM",totalAmount,totalShipping);
    console.log(`The total is: ${result}`);
}