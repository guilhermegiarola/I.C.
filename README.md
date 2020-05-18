# README
# Dependencies

This code requires Python3, numpy, Pandas and spaCy. If you already have Python3 and pip, you can get numpy, Pandas and spaCy via:
```
pip install numpy
pip install pandas
pip install spacy
```
To use this code, you should first copy it to your computer via
```
git clone https://github.com/guilhermegiarola/I.C..git
```

# Usage

Then, you can invoke it from the prompt, acessing it's location and invoking it as the following code:
```
python3 intentionRecognizerJSon.py "insert the name of the .csv file with the phrases (as in "document.csv") here"
```

# Datasets
The datasets shall follow a simple pattern. There are three columns: "Frase", "Implicito/Explicito" and "Funcionalidade Desejada".
The phrases to be added to the first column must be in portuguese and must be treated before using the software. It includes removing all accentuation, special characters and turn all uppercase letters, lowercase.
The second column must contain a word that corresponds to "implicito", if the phrase contains a implicit intention and "explicito", otherwise.
The last column must contain the desired function to be invoked when the phrase is recognized. For a list of the possible functions, just read the sample dataset in this repository.
