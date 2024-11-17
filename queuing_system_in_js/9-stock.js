const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const client = redis.createClient();

const asyncGet = promisify(client.get).bind(client);

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

const getItemById = (id) => {
    return listProducts.find((item) => {
        item.itemId === parseInt(id)
    });
};

const reserveStockById = (itemId, stock) => {
    client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
    return await asyncGet(`item.${itemId}`);
};

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    const stock = await getCurrentReservedStockById(itemId);
    if (!item) res.json({ status: 'Product not found' });
    else res.json({ ...item, currentQuantity: stock });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    const stock = await getCurrentReservedStockById(itemId);
    if (!item) res.json({ status: 'Product not found' });
    else if (stock < 1) res.json({ status: 'Not enough stock available', itemId: itemId });
    else {
        reserveStockById(itemId, stock - 1);
        res.json({ status: 'Reservation confirmed', itemId: itemId });
    }
});

app.listen(1245, () => {
    listProducts.forEach((product) => {
        reserveStockById(product.itemId, product.initialAvailableQuantity);
    });
});