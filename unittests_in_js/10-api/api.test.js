const assert = require('assert');
const request = require('request');

describe("API", () => {

    describe('#router.get(/)', () => {
        it("Should return status code 200", (done) => {
            request.get("http://localhost:7865", (error, response, body) => {
                assert.equal(response.statusCode, 200);
                done();
            });
        });

        it("Should return welcome sentence", (done) => {
            request.get("http://localhost:7865", (error, response, body) => {
                assert.equal(body, "Welcome to the payment system");
                done();
            });
        });
    })

    describe("#router.get(/cart/:id)", () => {
        it("Should return status code 200 with id parameter is number", (done) => {
            const id = 10;
            request.get(`http://localhost:7865/cart/${id}`, (error, response, body) => {
                assert.equal(response.statusCode, 200);
                assert.equal(body, `Payment methods for cart ${id}`);
                done();
            });
        });

        it("Should return status code 404 with id parameter is string", (done) => {
            const id = "bouh";
            request.get(`http://localhost:7865/cart/${id}`, (error, response, body) => {
                assert.equal(response.statusCode, 404);
                done();
            })
        });
    })

    describe('#router.get(/available_payments)', () => {
        it('Should return a object with the payment option', (done) => {
            const expectedBody = JSON.stringify({
                payment_methods: {
                    credit_cards: true,
                    paypal: false
                }
            });
            request.get(`http://localhost:7865/available_payments`, (error, response, body) => {
                assert.equal(response.statusCode, 200);
                assert.equal(body, expectedBody);
                done();
            });
        });
    });

    describe('#router.post(/login)', () => {
        it('Should return the message with the name of user logged', (done) => {
            const username = "bouh";
            const req = {
                url: "http://localhost:7865/login",
                json: { userName: username }
            };
            const expectedBody = `Welcome ${username}`;
            request.post(req, (error, response, body) => {
                assert.equal(response.statusCode, 200);
                assert.equal(body, expectedBody);
                done();
            });
        });
    });
})
