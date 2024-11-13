import { expect } from 'chai';
import { calculateNumber } from './2-calcul_chai.js';

describe("calculateNumber", () => {
    it("should sum, subtract or divide a value", () => {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
});