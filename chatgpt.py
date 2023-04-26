# Key se obtiene en https://platform.openai.com/docs/api-reference
# en personal ---> View API Keys ---> create new secret key
import openai


openai.api_key = 'Key'

while True: 


    prompt = input('\n Introduce una pregunta:')

    if prompt =='exit':
        break

    completion = openai.Completion.create(engine="text-davinci-003",
                                            prompt=prompt,
                                            max_tokens=2048)

    print(completion.choices[0].text)
