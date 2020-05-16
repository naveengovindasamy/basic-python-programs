punctuations = '''!()-[]{}:;;"\<>./?@#%^&*(_'''

my_str = "hello!!!, he said ---and went."

no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

print(no_punct)