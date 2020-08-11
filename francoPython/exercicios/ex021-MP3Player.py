import pygame

pygame.mixer.init()
pygame.init()

resposta = input('\nDeseja ligar o MP3? (sim/nao): ')

while resposta not in 'simSIMsSnaoNAOnN':
    resposta = input('Opção Inválida. Deseja ligar o MP3? (sim/nao): ')

if resposta in 'simSIMsS':

    musica = input('Qual música deseja tocar? ')

    if musica == 'houdini':
        pygame.mixer.music.load('../music/houdini.mp3')
        print('Tocando "Houdini - Foster the People"')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()

    elif musica == 'dance monkey':
        pygame.mixer.music.load('../music/dancemonkey.mp3')
        print('Tocando "Dance Monkey - Tones and I"')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()

    elif musica == 'photograph':
        pygame.mixer.music.load('../music/photograph.mp3')
        print('Tocando "Photograph - Ed Sheeran"')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()

    elif musica == 'waste':
        pygame.mixer.music.load('../music/waste.mp3')
        print('Tocando "Waste - Foster the People"')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()

    elif musica == 'i wanna hold your hand':
        pygame.mixer.music.load('../music/iwannaholdyourhand.mp3')
        print('Tocando "I Wanna Hold Your Hand - The Beatles"')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()

elif resposta in 'naoNAOnN':
    print('MP3 Off')


