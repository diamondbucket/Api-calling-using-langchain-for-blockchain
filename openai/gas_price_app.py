def gas_price():
    import requests
    import json
    const =  0.000000001
    method = "get"
    apiUrl = "https://api.1inch.dev/gas-price/v1.5/1"
    requestOptions = {
          "headers": {
      "Authorization": "Bearer {api_key}"
    },
          "body": {},
          "params": {}
    }
    # Prepare request components
    headers = requestOptions.get("headers", {})
    body = requestOptions.get("body", {})
    params = requestOptions.get("params", {})
    
    response = requests.get(apiUrl, headers=headers, params=params)
    price_in_eth = int(response.json()['baseFee'])*const
    return str(price_in_eth)
