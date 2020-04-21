# -*- coding: utf-8 -*-
import spacy
import sys
import json
import pandas as pd
import re
import io
import numpy as np

def intentionRecognizerJson(archive):
    correctlyIdentified = []
    incorrectlyIdentified = []
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

    print("Corretamente identificadas: ")
    print()
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

        if(df.iloc[phrase,1] == 'explicito'):
            explicitCounter = explicitCounter + 1
            for token in processedLine:
                for name, synonymsList in dic.items():
                    if(name in ['desligar', 'apagar']):
                        if token.lemma_ in ['diminuir', 'reduzir', 'abaixar']:
                            pass
                        elif token.lemma_ in synonymsList or token.lemma_ == name:
                            print(token.lemma_)
                            desligar = True
                            break

                    elif(name in ['acender', 'acionar', 'ativar', 'ligar']):
                        if token.lemma_ in ['aumentar', 'incrementar']:
                            pass
                        elif token.lemma_ in synonymsList or token.lemma_ == name:
                            print(token.lemma_)
                            ligar = True
                            break

                    elif(name in ['mudar', 'trocar']):
                        if token.lemma_ in synonymsList or token.lemma_ == name:
                            print(token.lemma_)
                            trocar = True
                            break

                    elif(name in ['aumentar', 'incrementar']):
                        if token.lemma_ in ['acender', 'acionar', 'ativar', 'ligar']:
                            pass
                        elif token.lemma_ in synonymsList or token.lemma_ == name:
                            print(token.lemma_)
                            aumentar = True
                            break

                    elif(name in ['diminuir', 'reduzir', 'abaixar']):
                        if token.lemma_ in ['desligar', 'apagar']:
                            pass
                        elif token.lemma_ in synonymsList or token.lemma_ == name:
                            print(token.lemma_)
                            diminuir = True
                            break
            print(processedLine)

            oldCounter = rightCounter
            for token in processedLine:
                if (token.lemma_ in ['lampada', 'luz', 'luzir']):
                    print(desligar, ligar, token.lemma_)
                    if(desligar is True):
                        if(df.iloc[phrase,2] == 'Apagar a lampada.'):
                            rightCounter = rightCounter + 1
                            break
                    elif(ligar is True):
                        if(df.iloc[phrase,2] == 'Acender a lampada.'):
                            rightCounter = rightCounter + 1
                            break

                elif (token.lemma_ == 'ventilador'):
                    print(desligar, ligar, token.lemma_)
                    if(desligar is True):
                        if(df.iloc[phrase,2] == 'Desligar o ventilador.'):
                            rightCounter = rightCounter + 1
                            break
                    elif(ligar is True):
                        if(df.iloc[phrase,2] == 'Ligar o ventilador.'):
                            rightCounter = rightCounter + 1
                            break

                elif (token.lemma_ in ['televisao','tv','TV']):
                    print(desligar, ligar, token.lemma_)
                    if(ligar is True):
                        if(df.iloc[phrase,2] == 'Ligar a televisao.'):
                            rightCounter = rightCounter + 1
                            break
                    elif(desligar is True):
                        if(df.iloc[phrase,2] == 'Desligar a televisao.'):
                            rightCounter = rightCounter + 1
                            break

                if (token.lemma_ in ['televisao', 'tv', 'canal', 'emissora']):
                    print(trocar, token.lemma_)
                    if(trocar is True):
                        if(df.iloc[phrase,2] == 'Trocar de canal.'):
                            rightCounter = rightCounter + 1
                            break
                if (token.lemma_ in ['televisao', 'tv', 'volume', 'som']):
                    print(aumentar, diminuir, token.lemma_)
                    if(aumentar is True):
                        if(df.iloc[phrase,2] == 'Aumentar o volume.'):
                            rightCounter = rightCounter + 1
                            break
                    elif(diminuir is True):
                        if(df.iloc[phrase,2] == 'Diminuir o volume.'):
                            rightCounter = rightCounter + 1
                            break

            if(rightCounter > oldCounter):
                correctlyIdentified.append(df.iloc[phrase,0])
            else:
                incorrectlyIdentified.append(df.iloc[phrase,0])

            print()
    print(correctlyIdentified)
    print()


    print("Incorretamente identificadas: ")
    print(incorrectlyIdentified)
    print()

    print("Correct Counter: " + str(rightCounter))
    print("Explicit Counter: " + str(explicitCounter))

    precision = rightCounter/explicitCounter
    coverage = rightCounter/len(df)
    fMeasure = (2*precision*coverage)/(precision+coverage)

    print()
    print("Precision: " + str("{:1.2f}".format(precision)))
    print("Coverage: " + str("{:1.2f}".format(coverage)))
    print("F-Measure: " + str("{:1.2f}".format(fMeasure)))



def main():
    intentionRecognizerJson(sys.argv[1])

main()
