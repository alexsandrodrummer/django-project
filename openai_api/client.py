from openai import OpenAI


client = OpenAI(
    api_key='Your APIKEY'
)


def get_car_ai_description(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 200 caracteres. Descreva coisas específicas desse modelo.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )

    return response.choices[0].message.content
