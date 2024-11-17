const assert = require('assert');
const request = require('request');

describe("API", () => {

    describe('#router.get(/)', () => {
        it("Should return status code 200", (done) => {
            request.get("http://localhost:7865", (error, response, body) => {
                assert.equal(response.statusCode, 200)
                done();
            });
        });

        it("Should return welcome sentence", (done) => {
            request.get("http://localhost:7865", (error, response, body) => {
                assert.equal(body, "Welcome to the payment system")
                done();
            });
        });

    })

    describe("#router.get(/cart/:id)", () => {
        it("Should return status code 200 with id parameter is number", (done) => {
            let id = 10;
            request.get(`http://localhost:7865/cart/${id}`, (error, response, body) => {
                assert.equal(response.statusCode, 200);
                done();
            });
        });

        it("Should return status code 404 with id parameter string", (done) => {
            let id = "bouh";
            request.get(`http://localhost:7865/cart/${id}`, (error, response, body) => {
                assert.equal(response.statusCode, 404);
                done();
            })
        });
    })
})
