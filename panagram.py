def main():
    english = list("The quick brown fox jumps over the lazy dog")
    german = list("Zwölf Boxkämpfer jagen Viktor quer über den großen Sylter Deich")
    turkish = list("Pijamalı hasta yağız şoföre çabucak güvendi")

    english = [x.strip().lower() for x in english if len(x) > 0]
    german = [x.strip().lower() for x in german if len(x) > 0]
    turkish = [x.strip().lower() for x in turkish if len(x) > 0]

    words = ['Fix', 'Foo bar', 'Oranienburger Straße', 'Jägermeister', 'çubuk', 'çwiß']

    for word in words:
        langs = []
        if matches(word, english):
            langs.append('English')
        
        if matches(word, german):
             langs.append('German')
        
        if matches(word, turkish):
            langs.append('Turkish')
        
        print(word, langs)

def matches(word, lang):
    for x in word:
        if len(x.strip()) == 0:
            continue
        
        if x.lower() not in lang:
            return False
    return True

if __name__ == '__main__':
    main()