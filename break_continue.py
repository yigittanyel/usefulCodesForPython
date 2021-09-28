#break
text="hello"
for val in text:
    if val=="l":
        break
    print(val)
print("End of the text") # h e end of the text

#continue

text="hello"
for val in text:
    if val=="l":
        continue
    print(val)
print("End of the text") # h e o end of the text