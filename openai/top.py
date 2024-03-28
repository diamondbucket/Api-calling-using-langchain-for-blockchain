def top_erc20_tokens():
    token_info = []
    from moralis import evm_api
    import json
    api_key = "......"
    
    result = evm_api.market_data.get_top_erc20_tokens_by_market_cap(
      api_key=api_key,
    )
    with open("top_tokens.json","w") as f:
        json.dump(result,f)
    for i in result:
        token_info.append([i['token_name'],i['price_usd']])
    return token_info


    
