#!/usr/bin/python
# coding: utf-8

def hello(lang="en"):
    cad = "Hello World!"

    if lang == "de":
        cad = "Hallo Welt!"
    elif lang == "es":
        cad = "Hola Mundo!"
    elif lang == "fr":
        cad = "Bonjour Monde!"
    elif lang == "it":
        cad = "Ciao Mondo!"
    elif lang == "pr":
        cad = "Ola Mundo!"
    elif lang == "ru":
        cad = u'привет мир'
    elif lang == "ef":
        cad = "Hofolafa Mufundofo!"

    print cad

if __name__ == "__main__":
    import sys
    try:
        lan = sys.argv[1]
    except IndexError:
        lan = "en"
    hello(lang=lan)
