
import openai
openai.api_key = "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"
def generate(text):
    response = openai.Completion.create(
        promt = text,
        engine = 'gpt-3.5-turbo-0613',
        max_tokens = 100,
        temperature = 0.7,
        n=1,
        stop=None,
        timeout = 15
    )
    if response and response.choises:
        return response.choises[0].text.strip()
    else:
        return None
    
generate('Як справи')