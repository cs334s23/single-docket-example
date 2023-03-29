# Regulations.gov Search
The regulations.gov search has the ability to search
all comments and even the text in files attached to comments for a word.  
The regulations.gov search also has the ability to search for words that are similar to the word that is searched.  
Searching for 'immigration' will also return results for 'immigrant'.
The Regulations.gov search also returns results for tokens that are numbers and email addresses.

# Extracted Text

Extracted text sometimes counts the same word multiple times.  
This is because words have punctuation around them.


# Run Word Counter Code
Run the command below in the root of the project directory.

```
python3 counter/main.py
```
This will create a csv file in the root named 'results.txt'. This file has two columns:  
word (the string word found in the text), and  
count (the number of times the word has been found in the docket).
