# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as file:
        text = file.read()
    
    return text


def count_words():
    text = read_file_content("./story.txt")

    return {txt: text.count(txt) for txt in text}
