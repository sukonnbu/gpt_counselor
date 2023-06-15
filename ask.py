import openai

openai.api_key = "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"


def ask_help(content: str):
    result = openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature=1, messages=[{"role": "user",
                                                                                           "content": content
                                                                                           }]).choices[0].message.content

    result = openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature=1, messages=[{"role": "user",
                                                                                           "content": f"""
                                                                            다음 문장에서
                                                                            종종 마침표를 '☆', '~', '응응!', '!'의 문자들 중 무작위로 치환해줘.
                                                                            가끔씩은 '(*≧∀≦)ﾉ', '(★≧▽^))★☆', '(-ω- )'과 같은 무작위의 이모티콘으로 치환해줘. :
                                                                            '''{result}'''
                                                                            """
                                                                                           }]).choices[0].message.content

    return result


openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature=0.8, messages=[
                             {"role": "system",
                                 "content": """너는 심리상담 전문가이자 나의 심리상담 상대야. 내가 물어보는 것에 따뜻하게 답해 줘."""}])

running = True

while running:
    user_input = input("U: ")
    if user_input == "":
        running = False
        break

    respond = ask_help(user_input)
    print(respond)
