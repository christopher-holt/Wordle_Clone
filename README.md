# Wordle_Clone
An interactive command line Wordle clone written in python

## Words used
The list of words were downloaded from https://www-cs-faculty.stanford.edu/~knuth/sgb.html and must be in the current working directory
```
$ wget -O five_letter_words.txt https://www-cs-faculty.stanford.edu/\~knuth/sgb-words.txt
```
## Demo
```
$ ./wordle.py                                                                                                                                                                
You have not played Wordle today!
Please enter a guess: audio
['a-', 'u', 'd-', 'i-', 'o-']   1
Please enter a guess: stern
['a-', 'u', 'd-', 'i-', 'o-']
['S', 'T', 'e-', 'r-', 'n']   2
Please enter a guess: stuns
['a-', 'u', 'd-', 'i-', 'o-']
['S', 'T', 'e-', 'r-', 'n']
['S', 'T', 'U', 'N', 's']   3
Please enter a guess: stunt
['a-', 'u', 'd-', 'i-', 'o-']
['S', 'T', 'e-', 'r-', 'n']
['S', 'T', 'U', 'N', 's']
['S', 'T', 'U', 'N', 'T']   4
Right Answer in 4 guesses!
$
```
## Records
records.csv is a flat file storing all the records of the previous worlde answers. If it does not exist, it will be generate in the current working directory
