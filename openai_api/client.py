from openai import OpenAI


client = OpenAI(
    api_key='sk-fgLDIsH0kqJBf4FG5fhPqXLz4xTBT_7yqvCaZVGiKMT3BlbkFJ6AgaCwdXvjPszesKNEw1dPypV7hZZnvcwfc7rmbvMA'
)


def get_car_ai_description(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
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