""" class MyLLM():
    @staticmethod
    def call_openai(model, prompt):
        response = openai.ChatCompetion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    
    # Definir o modelo LLM
    gpt_mini                = lambda prompt: MyLLM.call_openai("gpt-4o-mini", prompt)
    gpt4o_mini              = lambda prompt: MyLLM.call_openai("gpt-4o-mini", prompt)
    gpt4o_mini_2024_07_18   = lambda prompt: MyLLM.call_openai("gpt-4o-mini-2024-07-18", prompt)
    gpt_4o_2024_08_06       = lambda prompt: MyLLM.call_openai("gpt-4o-2024-08-06", prompt)
    gpt4o                   = lambda prompt: MyLLM.call_openai("gpt-4o", prompt)
    gpt_o1                  = lambda prompt: MyLLM.call_openai("o1-preview", prompt)
    gpt_o1_mini             = lambda prompt: MyLLM.call_openai("o1-mini", prompt)"""