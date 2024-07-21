# func_count_sentences.py
def func_count_sentences(text):
    return text.count('.') + text.count('!') + text.count('?')

print(func_count_sentences("Hello world! How are you today? I hope you're doing well."))
