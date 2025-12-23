def no_of_words(text):
    l=text.split()
    return len(l)

def count_characters(text):
    word_count={}
    for p in text:
        p=p.lower()
        if p.isalpha():
            if(not p in word_count):
                word_count[p]=1
            else:
                word_count[p]+=1
    return word_count
