# 8 - Faça um programa em Python que funcione como um tradutor bidirecional inteligente entre os idiomas português e inglês.

from deep_translator import GoogleTranslator
import langid

langid.set_languages(['pt','en'])

def traducao_dua_via(texto):
    idioma, precisao = langid.classify(texto)

    match idioma:
        case 'pt':
            return GoogleTranslator(source='pt', target='en').translate(texto)
        case 'en':
            return GoogleTranslator(source='en', target='pt').translate(texto)
        case _:
            return 'Não consegue traduzir'
    
text = input('Digite o texto que queres traduzir: ')

print(f'Texto normal: {text} e texto traduzido: {traducao_dua_via(text)}')