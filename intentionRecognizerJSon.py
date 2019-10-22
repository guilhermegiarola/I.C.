import spacy
import sys
import json

def intentionRecognizerJson(line):
    nlp = spacy.load('pt_core_news_sm')
    processedLine = nlp(line)
    synonymsList = []
    content = open('synonyms.json').read()
    dic = json.loads(content)
    desligar = False
    ligar = False
    trocar = False
    
    for token in processedLine:
        for name, synonymsList in dic.items():
            if(name in ['desligar', 'apagar']):
                if token.lemma_ in synonymsList or token.lemma_ == name:
                    desligar = True
        
            elif(name in ['acender', 'acionar', 'ativar', 'ligar']):
                if token.lemma_ in synonymsList or token.lemma_ == name:
                    ligar = True
    
            elif(name in ['mudar', 'trocar']):
                if token.lemma_ in synonymsList or token.lemma_ == name:
                    trocar = True

    for token in processedLine: 
        if (token.lemma_ in ['lâmpada', 'luz']):
            if(desligar is True):
                print("Apagou a luz.")
                return
            elif(ligar is True):
                print("Acendeu a luz.")
                return
        
        elif (token.lemma_ == 'ventilador'):
            if(desligar is True):
                print("Desligou o ventilador.")
                return
            elif(ligar is True):
                print("Ligou o ventilador.")
                return
        
        elif (token.lemma_ in ['televisão','tv','TV']):
            if(ligar is True):
                print("Ligar a televisão.")
                return
            elif(desligar is True):
                print("Desligar a televisão.")
                return
            elif(trocar is True):
                print("Trocou de canal.")
                return

def main():
    intentionRecognizerJson(sys.argv[1].lower())

main()
