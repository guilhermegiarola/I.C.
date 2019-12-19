import spacy
import sys
import json
import pandas as pd
import re
import io
import numpy as np

def intentionRecognizerJson(archive):
    
    pd.set_option('display.max_rows',157)
    
    nlp = spacy.load('pt_core_news_sm')
    with open(archive, 'r') as myfile:
        data = myfile.read()
        df = pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)), delimiter=';')

    for col in df.columns: #To replace all line breaks in all textual columns
        if df[col].dtype == np.object_:
            df[col] = df[col].str.replace('\n','')

    explicitCounter = 0
    rightCounter = 0

    for phrase in range(0, len(df)):
        line = df.iloc[phrase,0].lower()
        processedLine = nlp(line)
        synonymsList = []
        content = open('synonyms.json').read()
        dic = json.loads(content)
        desligar = False
        ligar = False
        trocar = False
        aumentar = False
        diminuir = False

        if(df.iloc[phrase,1] == "explícito"):
            explicitCounter = explicitCounter + 1
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

                    elif(name in ['aumentar', 'incrementar']):
                        if token.lemma_ in synonymsList or token.lemma_ == name:
                            aumentar = True

                    elif(name in ['diminuir', 'reduzir']):
                        if token.lemma_ in synonymsList or token.lemma_ == name:
                            diminuir = True

            for token in processedLine:
                if (token.lemma_ in ['lâmpada', 'luz', 'luzir']):
                    if(desligar is True):
                        if(df.iloc[phrase,2] == "Apagar a lâmpada."):
                            rightCounter = rightCounter + 1
                    elif(ligar is True):
                        if(df.iloc[phrase,2] == "Acender a lâmpada."):
                            rightCounter = rightCounter + 1

                elif (token.lemma_ == 'ventilador'):
                    if(desligar is True):
                        if(df.iloc[phrase,2] == "Desligar o ventilador."):
                            rightCounter = rightCounter + 1
                elif(ligar is True):
                        if(df.iloc[phrase,2] == "Ligar o ventilador."):
                            rightCounter = rightCounter + 1

                elif (token.lemma_ in ['televisão','tv','TV']):
                    if(ligar is True):
                        if(df.iloc[phrase,2] == "Ligar a televisão."):
                            rightCounter = rightCounter + 1
                    elif(desligar is True):
                        if(df.iloc[phrase,2] == "Desligar a televisão."):
                            rightCounter = rightCounter + 1

                if (token.lemma_ in ['televisão', 'tv', 'canal', 'emissora']):
                    if(trocar is True):
                        if(df.iloc[phrase,2] == "Trocar de canal."):
                            rightCounter = rightCounter + 1
                if (token.lemma_ in ['televisão', 'tv', 'volume', 'som']):
                    if(aumentar is True):
                        if(df.iloc[phrase,2] == "Aumentar o volume."):
                            rightCounter = rightCounter + 1
                    elif(diminuir is True):
                        if(df.iloc[phrase,2] == "Diminuir o volume."):
                            rightCounter = rightCounter + 1
    
    print("Correct Counter: " + str(rightCounter))
    print("Explicit Counter: " + str(explicitCounter))

    precision = rightCounter/explicitCounter
    coverage = rightCounter/len(df)
    fMeasure = (2*precision*coverage)/(precision+coverage)

    print("Precision: " + str("{:1.2f}".format(precision)))
    print("Coverage: " + str("{:1.2f}".format(coverage)))
    print("F-Measure: " + str("{:1.2f}".format(fMeasure)))



def main():
    intentionRecognizerJson(sys.argv[1])

main()
