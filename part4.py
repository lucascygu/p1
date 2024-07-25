def stable_stock_matching(buyers_preferences, stocks_preferences):
    
    free_buyers = list(buyers_preferences.keys())
    matches = {}
    stock_to_buyer = {}

    proposals = {buyer: [] for buyer in buyers_preferences}

    while free_buyers:
        buyer = free_buyers.pop(0)
        buyer_prefs = buyers_preferences[buyer]
        
        for stock in buyer_prefs:
            if stock not in proposals[buyer]:
                proposals[buyer].append(stock)
                
                if stock not in stock_to_buyer:
                    stock_to_buyer[stock] = buyer
                    matches[buyer] = stock
                    break
                else:
                    current_buyer = stock_to_buyer[stock]
                    stock_prefs = stocks_preferences[stock]
                    
                    if stock_prefs.index(buyer) < stock_prefs.index(current_buyer):
                        stock_to_buyer[stock] = buyer
                        matches[buyer] = stock
                        free_buyers.append(current_buyer)
                        del matches[current_buyer]
                        break
                        
    return reverse_matches(matches)

def reverse_matches(matches):
    reversed_matches = {buyer: stock for stock, buyer in matches.items()}
    return reversed_matches

# Time Complexity:
# O(B * S), where B is the number of buyers and S is the number of stocks.
# Each buyer proposes to each stock at most once, and each operation is constant time.

# Space Complexity:
# O(B + S + B * S):
# - O(B) for free_buyers.
# - O(S) for matches and stock_to_buyer.
# - O(B * S) for proposals.

# Optimality:
# Follows the Gale-Shapley algorithm.
# Efficient time and space complexity for practical use.
