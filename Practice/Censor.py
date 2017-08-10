def censor(text, word):
##censors the word out of block of text. Does not account for punctuation
    wordlist = []
    bleep = ""
    
    for letter in word: ##Creates the censored word
        bleep += "*"
        
    wordlist = text.split()    ##Splits text into a list

    for search in range(len(wordlist)): ##Searches the wordlist for word to censor
        if wordlist[search] == word:    ##if it finds the word, replace
            wordlist[search] = bleep

    return " ".join(wordlist)  ##Joins the list back together into a string

print (censor("hahahahahaha erere dope cope", "dope"))
