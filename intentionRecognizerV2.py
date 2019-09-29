import spacy
import sys

def intentionRecognizer(line):
    nlp = spacy.load('pt_core_news_sm')
    processedLine = nlp(line)

    for token in processedLine:
        if(token.lemma_ in ['apagar','desligar','desativar']):
            for token in processedLine:
                if(token.lemma_ in ['lâmpada','luzir']):
                    print("Apagou a luz.")
                    return
        elif(token.lemma_ in ['acender', 'acionar', 'ativar', 'ligar']):
            for token in processedLine:
                if(token.lemma_ in ['lâmpada', 'luzir']):
                    print("Acendeu a luz.")
                    return
        elif(token.lemma_ in ['ligar', 'ativar', 'iniciar', 'acionar']):
            for token in processedLine:
                if (token.lemma_ == 'ventilador'):
                    print("Ligou o ventilador.")
                    return
                elif (token.lemma_ in ['televisão', 'tv', 'TV']):
                    print("Ligou a televisão.")
                    return
        elif(token.lemma_ in ['desligar', 'desativar', 'terminar']):
            for token in processedLine:
                if (token.lemma_ == 'ventilador'):
                    print("Desligou o ventilador.")
                    return
                elif(token.lemma_ in ['televisão', 'tv', 'TV']):
                    print("Desligou a televisão.")
                    return
        elif(token.lemma_ in ['mudar', 'trocar']):
            for token in processedLine:
                if(token.lemma_ in ['canal', 'emissora']):
                    print("Trocou de canal.")
                    return
        else:
            print("Não entendi.")
            return

def main():
    intentionRecognizer(sys.argv[1].lower())

main()
