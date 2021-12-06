# Write a function rightJustify(word) that takes in a word as argument and 
# return a word with leading spaces so that the last letter of the word is in column 50 of the display.
def rightJustify(word):
	return format(word,">50s")
word=input("Enter The word to add leading space : ")
print(rightJustify(word))