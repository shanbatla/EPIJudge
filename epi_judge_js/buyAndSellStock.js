const assert = require('assert');

function buyAndSellStock(prices) {
    let minPriceSoFar = Infinity;
    let maxProfit = 0;

    prices.forEach((price) => {
        let maxProfitToday = price - minPriceSoFar;
        maxProfit = Math.max(maxProfit, maxProfitToday);
        minPriceSoFar = Math.min(minPriceSoFar, price);
    });

    return maxProfit;
}

const prices = [310, 315, 275,295, 260, 270, 290, 230, 255, 250];
const ans = 30;

assert.strictEqual(buyAndSellStock(prices), ans);