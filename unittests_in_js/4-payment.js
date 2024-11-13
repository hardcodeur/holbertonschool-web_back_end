const Untils = require("./utils")

const sendPaymentRequestToApi =(totalAmount,totalShipping)=>{   
    let util = new Untils
    let result= util.calculateNumber("SUM",totalAmount,totalShipping);
    console.log(`The total is: ${result}`);
}

module.export=sendPaymentRequestToApi
