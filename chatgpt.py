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
