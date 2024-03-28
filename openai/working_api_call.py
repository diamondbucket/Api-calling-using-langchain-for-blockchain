from openai import OpenAI
import json 
import gas_price_app as gap
import top
OPENAI_API_KEY = "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"

client = OpenAI(api_key=OPENAI_API_KEY)

def second_response():
    second_response = client.chat.completions.create(
            model = "gpt-3.5-turbo-0125",
            messages=[
                {"role":"user","content":query},
                message,
                {
                    "role":"function",
                    "name" : function_name,
                    "content": function_response
                },
            ],
        )
    print(second_response.choices[0].message.content)

def gas_price_info(gas_info : str):
    gas_info = {
        "name": gas_info,
        "gas_price": gap.gas_price(),
    }
    return json.dumps(gas_info)

def erc20_top(token_info :str):
    token_info = {
        "name":token_info,
        "token_info": top.top_erc20_tokens(),
    }
    return json.dumps(token_info)

functions = [
    {
        "name":"erc20_top",
        "description":"gives the price for top crypto currencies right now",
        "parameters":{
            "type":"object",
            "properties":{
                "token_info":{
                    "type":"string",
                    "description":"query from the user inquiring about the trending crypto currencies"
                },
            },"required":["token_info"]
        },
    },
    {
        "name":"gas_price_info",
        "description":"gives the gas price for transaction in ethereum mainnet",
        "parameters":{
            "type":"object",
            "properties":{
                "gas_info":{
                    "type":"string",
                    "description":"query from the user inquiring about the gas price"
                },
            },"required":["gas_info"]
        },
    }
]

def chat(query):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role":"user","content": query}],
        functions=functions
    )
    message = response.choices[0].message
    return message

while(1):
    query = str(input("enter the prompt: "))
    message = chat(query)
    #print(message)
    if message.function_call==None:
            print(message.content)
    elif message.function_call:
        if "token_info" in message.function_call.arguments:
            function_name = message.function_call.name
    
            token_info = json.loads(message.function_call.arguments).get("token_info")
            function_response = erc20_top(
                token_info=token_info
            )
            second_response()
        
        elif "gas_info" in message.function_call.arguments == '{"gas_info":"gas price"}':
            gas_info = json.loads(message.function_call.arguments).get("gas_info")
            function_name = message.function_call.name
            function_response = gas_price_info(
                gas_info=gas_info
            )
            second_response()
    if query == "/bye":
        break