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

    return matches
