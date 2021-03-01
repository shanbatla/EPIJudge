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

function buyAndSellStockv2(prices) {
    let minPriceSoFar;
    let maxProfit = 0;

    for (let idx = 0; idx < prices.length; idx++) {
        if (idx === 0) {
            minPriceSoFar = prices[idx];
            continue;
        } else {
            minPriceSoFar = Math.min(minPriceSoFar, prices[idx]);
            let profitToday = prices[idx] - minPriceSoFar;
            maxProfit = Math.max(maxProfit, profitToday); 
        }
    }

    return maxProfit;
}

const prices = [310, 315, 275,295, 260, 270, 290, 230, 255, 250];
const ans = 30;

assert.strictEqual(buyAndSellStockv2(prices), ans);