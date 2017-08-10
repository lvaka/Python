translate = input("Enter word for translation -> Pyglatin: ")
translate = translate.lower()
front = translate[0]

def lets_roll(counter, wrd_lngth, back):
    if counter < wrd_lngth:
        back = back + translate[counter]
        counter = counter + 1
        return lets_roll(counter, wrd_lngth, back)
    else:
        return back
back = lets_roll( 1, len(translate), "")
translate = back + front + "ay"
print ("################")
print (translate)
