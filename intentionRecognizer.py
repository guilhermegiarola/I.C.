import spacy
import os
import time
import json
from spacy.tokenizer import Tokenizer
from stateMachine import stateMachine
class intentionRecognizer:

    states = []
    for rooms in range(0,4):
        auxIter = stateMachine()
        states.append(auxIter)

    def recognizer(self,line):
        nlp = spacy.load('pt_core_news_sm')
        tokenizer = Tokenizer(nlp.vocab)

        processedLine = tokenizer(line)

        synonymsList = []
        content = open('synonyms.json').read()
        dic = json.loads(content)
        tokenAtivacao = self.activateToken(processedLine)
        if(tokenAtivacao):
            self.statementAction(processedLine, dic)
        else:
            print("O token de ativação não foi reconhecido.")

    def activateToken(self,processedLine):
        if(processedLine[0].lemma_ == 'token'):
            return True
        return False

    def statementAction(self, processedLine, dic):
        for name, synonymsList in dic.items():
            if(name in ['acender', 'acionar', 'ativar', 'ligar','desligar', 'apagar','mudar', 'trocar']):
                if(processedLine[1].lemma_ in synonymsList or processedLine[1].lemma_ == name):
                    functionality, ambience = self.actionManager(processedLine)
                    turnOn, turnOff, switch = self.recognizeAction(processedLine, dic)
                    self.printAction(turnOn, turnOff, switch, functionality, ambience)
                    return
            elif(name in ['luzir', 'ventilador', 'tv', 'televisão', 'canal', 'emissora']):
                if(processedLine[1].lemma_ in synonymsList or processedLine[1].lemma_ == name):
                    self.statusManager(processedLine, dic)
                    return

    def actionManager(self,processedLine):
        for token in processedLine:
            if(token.lemma_ in ['lâmpada', 'luzir', 'claro', 'escuro']):
                functionality = 'lâmpada'
            elif(token.lemma_ in ['ventilador', 'calor']):
                functionality = 'ventilador'     
            elif(token.lemma_ in ['televisão','tv','TV', 'canal', 'emissora']):
                functionality = 'tv'
        
        for token in processedLine:
            if(token.text == 'quarto.'):
                ambience = 'quarto'
            elif(token.text == 'sala.'):
                ambience = 'sala'
            elif(token.text == 'banheiro.'):
                ambience = 'banheiro'
            elif(token.text == 'cozinha.'):
                ambience = 'cozinha'

        return functionality, ambience

    def recognizeAction(self,processedLine, dictionary):
        trocar = False
        ligar = False
        desligar = False
        
        for token in processedLine:
            for name, synonymsList in dictionary.items():
                if(name in ['desligar', 'apagar']):
                    if (token.lemma_ in synonymsList or token.lemma_ == name):
                        desligar = True
            
                if(name in ['acender', 'acionar', 'ativar', 'ligar']):
                    if (token.lemma_ in synonymsList or token.lemma_ == name):
                        ligar = True
        
                if(name in ['mudar', 'trocar']):
                    if (token.lemma_ in synonymsList or token.lemma_ == name):
                        trocar = True
        return ligar, desligar, trocar

    def printAction(self,turnOn, turnOff, switch, functionality, ambience):   
        #states[0] - Sala
        if(ambience == 'sala'):
            if(functionality == 'lâmpada'):
                if(self.states[0].lampada is False and turnOff is True):
                    print("As luzes da sala já estão apagadas.")
                elif(self.states[0].lampada is False and turnOn is True):
                    self.states[0].lampada = True
                    print("Acenderam-se as luzes da sala.")
                elif(self.states[0].lampada is True and turnOff is True):
                    self.states[0].lampada = False
                    print("Apagaram-se as luzes da sala.")
                elif(self.states[0].lampada is True and turnOn is True):
                    print("As luzes da sala já estão acesas.")

            elif(functionality == 'tv'):
                if(self.states[0].televisao is False and turnOff is True):
                    print("A televisão da sala já está desligada.")
                elif(self.states[0].televisao is False and turnOn is True):
                    print("A televisão da sala foi ligada.")
                    self.states[0].televisao = True
                elif(self.states[0].televisao is True and turnOff is True):
                    print("A televisão da sala foi desligada.")
                    self.states[0].televisao = False
                elif(self.states[0].televisao is True and turnOn is True):
                    print("A televisão da sala já está ligada.")
                elif(self.states[0].televisao is False and switch is True):
                    print("A televisão da sala está desligada.")
                elif(self.states[0].televisao is True and switch is True):
                    print("A televisão da sala trocou de canal.")
            
            elif(functionality == 'ventilador'):
                if(self.states[0].ventilador is False and turnOff is True):
                    print("O ventilador da sala já está desligado.")
                elif(self.states[0].ventilador is False and turnOn is True):
                    self.states[0].ventilador = True
                    print("O ventilador da sala foi ligado.")
                elif(self.states[0].ventilador is True and turnOff is True):
                    self.states[0].ventilador = False
                    print("O ventilador da sala foi desligado.")
                elif(self.states[0].ventilador is True and turnOn is True):
                    print("O ventilador da sala já está ligado.")
        
        #states[1] - Quarto
        if(ambience == 'quarto'):
            if(functionality == 'lâmpada'):
                if(self.states[1].lampada is False and turnOff is True):
                    print("As luzes do quarto já estão apagadas.")
                elif(self.states[1].lampada is False and turnOn is True):
                    self.states[1].lampada = True
                    print("Acenderam-se as luzes do quarto.")
                elif(self.states[1].lampada is True and turnOff is True):
                    self.states[1].lampada = False
                    print("Apagaram-se as luzes do quarto.")
                elif(self.states[1].lampada is True and turnOn is True):
                    print("As luzes do quarto já estão acesas.")

            elif(functionality == 'ventilador'):
                if(self.states[1].ventilador is False and turnOff is True):
                    print("O ventilador do quarto já está desligado.")
                elif(self.states[1].ventilador is False and turnOn is True):
                    self.states[1].ventilador = True
                    print("O ventilador do quarto foi ligado.")
                elif(self.states[1].ventilador is True and turnOff is True):
                    self.states[1].ventilador = False
                    print("O ventilador do quarto foi desligado.")
                elif(self.states[1].ventilador is True and turnOn is True):
                    print("O ventilador do quarto já está ligado.")
            else:
                print("Não existe essa funcionalidade para o quarto.")

        #states[2] - Banheiro
        if(ambience == 'banheiro'):
            if(functionality == 'lâmpada'):
                if(self.states[2].lampada is False and turnOff is True):
                    print("As luzes do banheiro já estão apagadas.")
                elif(self.states[2].lampada is False and turnOn is True):
                    self.states[2].lampada = True
                    print("Acenderam-se as luzes do banheiro.")
                elif(self.states[2].lampada is True and turnOff is True):
                    self.states[2].lampada = False
                    print("Apagaram-se as luzes do banheiro.")
                elif(self.states[2].lampada is True and turnOn is True):
                    print("As luzes do banheiro já estão acesas.")
            else:
               print("Não existe essa funcionalidade para o banheiro.")
        
        #states[3] - Cozinha
        if(ambience == 'cozinha'):
            if(functionality == 'lâmpada'):
                if(self.states[3].lampada is False and turnOff is True):
                    print("As luzes da cozinha já estão apagadas.")
                elif(self.states[3].lampada is False and turnOn is True):
                    self.states[3].lampada = True
                    print("Acenderam-se as luzes da cozinha.")
                elif(self.states[3].lampada is True and turnOff is True):
                    self.states[3].lampada = False
                    print("Apagaram-se as luzes da cozinha.")
                elif(self.states[3].lampada is True and turnOn is True):
                    print("As luzes da cozinha já estão acesas.")
            else:
               print("Não existe essa funcionalidade para a cozinha.")
    
    def statusManager(self,processedLine, dic):
        functionality, ambience = self.actionManager(processedLine)
        for token in processedLine:
            if(functionality == 'lâmpada'):
                if(ambience == 'cozinha'):
                    if(self.states[3].lampada is False):
                        print("As luzes da cozinha estão desligadas.")
                        return
                    else:
                        print("As luzes da cozinha estão acesas.")
                        return
                
                elif(ambience == 'banheiro'):
                    if(self.states[2].lampada is False):
                        print("As luzes do banheiro estão desligadas.")
                        return
                    else:
                        print("As luzes do banheiro estão acesas.")
                        return

                elif(ambience == 'quarto'):
                    if(self.states[1].lampada is False):
                        print("As luzes do quarto estão desligadas.")
                        return
                    else:
                        print("As luzes do quarto estão acesas.")
                        return
                
                elif(ambience == 'sala'):
                    if(self.states[0].lampada is False):
                        print("As luzes da sala estão desligadas.")
                        return
                    else:
                        print("As luzes da sala estão acesas.")
                        return

            elif(functionality == 'ventilador'):             
                if(ambience == 'quarto'):
                    if(self.states[1].ventilador is False):
                        print("O ventilador do quarto está desligado.")
                        return
                    else:
                        print("O ventilador do quarto está ligado.")
                        return

                elif(ambience == 'sala'):
                    if(self.states[0].ventilador is False):
                        print("O ventilador da sala está desligado.")
                        return
                    else:
                        print("O ventilador da sala está ligado.")
                        return
                else:
                    print("Não existe tal funcionalidade.")
                    return
            elif(functionality == 'tv'):
                if(ambience == 'sala'):
                    if(self.states[0].televisao is False):
                        print("A televisão da sala está desligada.")
                        return
                    else:
                        print("A televisão da sala está ligada.")
                        return
                else:
                    print("Não existe tal funcionalidade.")
                    return

def main():
    recognizer = intentionRecognizer()
    while True:
        print("Digite a frase a ser reconhecida: ")
        text = input()
        recognizer.recognizer(text.lower())
        time.sleep(3)
        os.system('clear')

main()