letter='''Dear <|Name|>,
You are Selected for Job!

Date for Meeting: <|Date|>
'''

name=input("Name\n")
date=input("Date for Meeting\n")

letter=letter.replace("<|Name|>", name)
letter=letter.replace("<|Date|>", date)

print(letter)
