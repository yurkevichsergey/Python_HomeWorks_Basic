# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
import string

# entered_text = "Python Community i like python community! Should, I. subscribe? Yes!"             # Test string

entered_text = input("Enter the future hashtag: ")

punctuation_list = list(string.punctuation)

for i in punctuation_list:
    entered_text = entered_text.replace(i, "")

entered_text = entered_text.title()
entered_text = entered_text.replace(" ", "")
entered_text = entered_text.strip()
hashtag = '#' + entered_text

if len(hashtag) >= 140:
    hashtag = hashtag[:140]

print(hashtag)

