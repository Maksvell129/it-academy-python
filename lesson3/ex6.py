# Пользователь вводит предложение. Необходимо вывести:
# количество символов;
# количество слов;
# первое слово;
# последнее слово;
# количество уникальных слов.
#
#
# Пример текста: Python — простой язык. Python используется для разработки, анализа данных и автоматизации

sentence = "Python — простой язык. Python используется для разработки, анализа данных и автоматизации?"

print(len(sentence))

sentence = sentence.replace("—", "")
sentence = sentence.replace(".", "")
sentence = sentence.replace(",", "")
sentence = sentence.replace("?", "")

words = sentence.split()

print(len(words))
print(words[0])
print(words[-1], words[len(words)-1])

print(len(set(words)))
