# FlashCards
A flashcard app created for the "100 Days of Code - The Complete Python Pro Bootcamp".  Makes use of Pandas and Tkinter.

The initial project made use of 101 popular French words. To modify the app, I created a csv file of the 2000 most popular German words.
The program can be switched between French and German by setting the LANGUAGE constant to either "German" or "French" and by setting the FILE_LANGUAGE constant to "german" or "french".

Initially the words are selected from the entire data set. After the first use, a csv file called "words_to_learn.csv" is created containing only the words that the user hasn't seen or doesn't know. In this way, the user doesn't have to keep seeing words that they already know.

The data comes from github user hermitdave. 

PS There are some strange translations owing to Google Translate and odd spellings from the hermitdave data set. hermitdave's data set also includes names. 
