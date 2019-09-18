import spacy

counterArray = [0]*7

def intentionRecognizer(line):
    nlp = spacy.load('pt')
    processedLine = nlp(line)

    for token in processedLine:
        if(token.lemma_ == 'apagar'):
            counterArray[0] += 1
            return

        elif(token.lemma_ == 'acender'):
            counterArray[1] += 1
            return

        elif(token.lemma_ == 'ligar'):
            for token in processedLine:
                if (token.lemma_ == 'ventilador'):
                    counterArray[2] += 1
                    return
                elif (token.lemma_ == 'tv' or token.lemma_ == 'televisão'):
                    counterArray[3] += 1
                    return
                elif (token.lemma_ == 'luz' or token.lemma_ == 'lâmpada'):
                    counterArray[1] += 1
                    return

        elif(token.lemma_ == 'desligar'):
            for token in processedLine:
                if (token.lemma_ == 'ventilador'):
                    counterArray[4] += 1
                    return
                elif(token.lemma_ == 'tv' or token.lemma_ == 'televisão'):
                    counterArray[5] += 1
                    return
                elif(token.lemma == 'luz' or token.lemma == 'lâmpada'):
                    counterArray[0] += 1
                    return


        elif(token.lemma_ == 'mudar'):
            for token in processedLine:
                if(token.lemma_ == 'canal'):
                    counterArray[6] += 1
                    return

def printResults():
        print("Intenções: ")
        print("     Apagar a luz: " + str(counterArray[0]))
        print("     Acender a luz: " + str(counterArray[1]))
        print("     Ligar o ventilador: " + str(counterArray[2]))
        print("     Ligar a televisão: " + str(counterArray[3]))
        print("     Desligar o ventilador: " + str(counterArray[4]))
        print("     Desligar a televisão: " + str(counterArray[5]))
        print("     Mudar de canal: " + str(counterArray[6]))
        return

def main():
    file = open("phraseList.txt", "r")

    for line in file:
        intentionRecognizer(line)

    print()
    printResults()

main()
