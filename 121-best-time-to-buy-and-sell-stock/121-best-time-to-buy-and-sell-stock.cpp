class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        //one pass approach
        //we check only for local min and max
        
        int minprice = INT_MAX;
        int maxprofit = 0;
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;}
};