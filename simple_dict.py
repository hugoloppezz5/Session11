d = {}
eng_to_spa = {"one":"uno", "two":"dos", "three":"tres"}
eng_to_spa["pineapple"] = "pina"
eng_to_spa.update({"yes":"si"})
sentence = "one two three pineapple"
words = sentence.split()
translation = ""
for word in words:
    translation += eng_to_spa[word] + " "
print(f"{sentence} translates to: {translation}")