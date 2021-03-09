###Tokenization du vocabulaire :

vocabulary = open("dictionnaire.txt","r",encoding="utf-8").read()


### on va creer une liste de mots:
tokenization_vocabulary = vocabulary.split(" ")


f = open("texte.txt","r",encoding="utf-8")
text_string = f.read()

### fonction qui remplace un argument donne par du vide
def clean_string(string,change_string):
  replacement_string = ""
  cleaning_string = string.replace(change_string, replacement_string)
  return(cleaning_string)


goal= clean_string("Gooooooooaaaaaalll!!!!!!!!!!!!!!!!!!!!!!!!!!!","!")
print(goal)

### fonction qui remplace un argument donne par un autre argument:

def modify_string(text_string,modify_string,replacement_string):
  modify_string = text_string.replace(modify_string, replacement_string)
  return(modify_string)

goal = modify_string("Gooooooooaaaaaalll!!!!!!!!!!!!!!!!!!!!!!!!!!!","!","@")
print(goal)

def clean_text(string,special_character,replacement_string):
  cleaned_string = text_string

  for string in special_character:
    cleaned_string = cleaned_string.replace(string,replacement_string)
  cleaned_string = cleaned_string.lower()
  return(cleaned_string) 

clean_characters = [".",",","'","\n"]
replacement =""
cleaned_text= clean_text(text_string,clean_characters,replacement)

print(cleaned_text)