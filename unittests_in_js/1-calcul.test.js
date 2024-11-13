let assert = require('assert');
const {calculateNumber} = require("./1-calcul.js");

describe("calculateNumber",()=>{
    it("sum, subtract or divide a value",()=>{
        assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
        assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    })
})