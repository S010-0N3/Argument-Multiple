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

def wash_string(text,text_a_modifier,text_de_remplacement):
  text_a_nettoyer = text_string

  for texts in text_a_modifier:
    text_a_nettoyer = text_a_nettoyer.replace(texts,text_de_remplacement)
  text_a_nettoyer = text_a_nettoyer.lower()
  return(text_a_nettoyer)


olist3 =["'",".","!",";","\n",","]
repla = "123"
iop = wash_string(text_string,olist3,repla)
print(iop)