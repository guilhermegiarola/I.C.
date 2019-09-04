def encontraSubstring(phrase):
#Tentativas para o gerenciamento da lâmpada:

    if "luz" in phrase:
        if "acender" in phrase:
            return ("Acendeu a lâmpada.")
        elif "acende" in phrase:
            return ("Acendeu a lâmpada.")
        elif "liga" in phrase:
            return ("Acendeu a lâmpada.")
        elif "ligar" in phrase:
            return ("Acendeu a lâmpada.")
        elif "apagar" in phrase:
            return ("Desligou a lâmpada.")
        elif "desligar" in phrase:
            return ("Desligou a lâmpada.")
        elif "apague" in phrase:
            return ("Desligou a lâmpada.")
        elif "desligue" in phrase:
            return ("Desligou a lâmpada.")
    
#Tentativas para o gerenciamento do ventilador:
    if "ventilador" in phrase:
        if "liga" in phrase:
            return("Ligou o ventilador.")
        elif "ligue" in phrase:
            return("Ligou o ventilador.")
        elif "ligar" in phrase:
            return("Ligou o ventilador.")
        elif "desliga" in phrase:
            return("Desligou o ventilador.")
        elif "desligue" in phrase:
            return("Desligou o ventilador.")
        elif "desligar" in phrase:
            return("Desligou o ventilador.")
    
#Tentativas para o gerenciamento da televisão.
    if "televisão" in phrase:
        if " ligue " in phrase:
            return("Ligou a televisão.")
        elif " ligar " in phrase:
            return("Ligou a televisão.")
        elif " desligue " in phrase:
            return("Desligou a televisão.")
        elif " desligar " in phrase:
            return("Desligou a televisão.")
    if "tv" in phrase:
        if "ligue" in phrase:
            return("Ligou a televisão.")
        elif "ligar" in phrase:
            return("Ligou a televisão.")
        elif "desligue" in phrase:
            return("Desligou a televisão.")
        elif "desligar" in phrase:
            return("Desligou a televisão.")

#Tentativas para o gerenciamento do volume.
    if "volume" in phrase:
        if "aumenta" in phrase:
            return("Aumentou o volume.")
        elif "diminui" in phrase:
            return("Diminuiu o volume.")
    
#Tentativas para a mudança de canal.
    if "canal" in phrase:
        return("Mudou de canal.")
    else:
        return("Não foi encontrada a substring.")
    
def main():
    strings =   ["Ligar luz",
                "Ligar a luz",
                "Iluminar o ambiente",
                "Já está claro o dia!",
                "Vamos economizar energia?",
                "Casa, apague a luz",
                "O ar está muito parado",
                "Está muito quente aqui",
                "Que calor!",
                "Está muito barulho, desligue o ventilador",
                "Já chega de ventilador",
                "desligue o ventilador",
                "quero ver tv",
                "ligue a tv",
                "tv, ligar",
                "Agora vou dormir, desligue a tv",
                "Tchau tv",
                "Tv, desligue",
                "Não consigo ouvir",
                "Que barulho! Não consigo ouvir a tv",
                "televisão fale mais alto!",
                "Silêncio!",
                "Que barulho!",
                "Vai acordar o bebê!",
                "Que filme chato! Troque pra mim?",
                "Trocar canal",
                "Escolher outra programação"]
    
    for phrase in strings:
        print(encontraSubstring(phrase.lower()))
    
if __name__ == "__main__":
    main()
