def translator(language):
   translations = {
    'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
    'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
    'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }
   def translate_word(word):
      if word.lower() in translations[language]:
         return translations[language][word.lower()]
      else:
         return 'not available in this language'
   return translate_word

translate = translator(input('Language: '))
wordinput = translate(input('Word: '))
print(wordinput)