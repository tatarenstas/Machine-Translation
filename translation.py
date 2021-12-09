import translators as ts

def translate(text,from_language,to_language):
  return ts.google(text, from_language, to_language)

print(translate("Це тест перекладу","uk","en")) #Result: This is a translation test
