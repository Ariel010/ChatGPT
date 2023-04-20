import openai


openai.api_key = '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'

while True: 


    prompt = input('\n Introduce una pregunta:')

    if prompt =='exit':
        break

    completion = openai.Completion.create(engine="text-davinci-003",
                                            prompt=prompt,
                                            max_tokens=2048)

    print(completion.choices[0].text)
