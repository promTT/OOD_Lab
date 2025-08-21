print("*** Reading E-Book ***")
text, highlight = input("Text , Highlight : ").split(",")
n = '[' + highlight + ']'
print(text.replace(highlight, n))