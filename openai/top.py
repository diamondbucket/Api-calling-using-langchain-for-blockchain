def top_erc20_tokens():
    token_info = []
    from moralis import evm_api
    import json
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6ImE0NzY4ZGIzLTIwNjEtNDk5MC1hYzk4LTVjMWU0MDY0YTQzMiIsIm9yZ0lkIjoiMzgzNjA3IiwidXNlcklkIjoiMzk0MTY3IiwidHlwZUlkIjoiZDA3M2IwZmQtYTFjYi00NzNjLWJjYWUtMTIxYzZlYTZlMjQxIiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE3MTA4NDM2ODAsImV4cCI6NDg2NjYwMzY4MH0.Cu7Sw2TrNCsPh-IhEOZ1ZmcqenvxIQ88Gdo2jV3guss"
    
    result = evm_api.market_data.get_top_erc20_tokens_by_market_cap(
      api_key=api_key,
    )
    with open("top_tokens.json","w") as f:
        json.dump(result,f)
    for i in result:
        token_info.append([i['token_name'],i['price_usd']])
    return token_info


    
