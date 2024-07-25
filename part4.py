def stable_stock_matching(buyers_preferences, stocks_preferences):
    free_buyers = list(buyers_preferences.keys())
    matches = {}  

    proposals = {buyer: [] for buyer in buyers_preferences}

    while free_buyers:
        buyer = free_buyers.pop(0)
        buyer_prefs = buyers_preferences[buyer]

        for stock in buyer_prefs:
            if stock not in proposals[buyer]:
                proposals[buyer].append(stock)

                if stock not in matches:
                    matches[stock] = buyer
                    break
                else:
                    current_buyer = matches[stock]
                    stock_prefs = stocks_preferences[stock]

                    if stock_prefs.index(buyer) < stock_prefs.index(current_buyer):
                        matches[stock] = buyer
                        free_buyers.append(current_buyer)
                        break

    tmp=k
    k=v
    v=tmp
    
    result = {v: k for k, v in matches.items()}
    return result
