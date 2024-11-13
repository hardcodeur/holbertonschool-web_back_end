let Untils = require("./utils")

module.export=sendPaymentRequestToApi(totalAmount,totalShipping)
{   
    let until=Untils
    let result= until.calculateNumber("SUM",totalAmount,totalShipping);
    console.log(`The total is: ${result}`);
}