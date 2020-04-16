import pygame
import random
import auto_py_to_exe

# released on 10/4/20
print('\nRelive the classic TIC_TAC_TOE in all new Black&Blue XD')
print('Developer- sivangbagri@gamil.com')
pygame.init()
WIDTH = 570
HEIGHT = 580
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Black&Blue')
colours = [(0, 255, 255), (192, 192, 192)]
screen.fill(random.choice(colours))
sound = pygame.mixer.Sound('tickles.wav')

# Rects
first = pygame.draw.rect(screen, (255, 0, 0), (50, 50, 150, 150))  # side_difference =160
second = pygame.draw.rect(screen, (255, 0, 0), (210, 50, 150, 150))
third = pygame.draw.rect(screen, (255, 0, 0), (370, 50, 150, 150))

fourth = pygame.draw.rect(screen, (255, 0, 0), (50, 210, 150, 150))
fifth = pygame.draw.rect(screen, (255, 0, 0), (210, 210, 150, 150))
sixth = pygame.draw.rect(screen, (255, 0, 0), (370, 210, 150, 150))

seventh = pygame.draw.rect(screen, (255, 0, 0), (50, 370, 150, 150))
eight = pygame.draw.rect(screen, (255, 0, 0), (210, 370, 150, 150))
nine = pygame.draw.rect(screen, (255, 0, 0), (370, 370, 150, 150))

turn = 'player1'

first_open = second_open = third_open = fourth_open = fifth_open = sixth_open = seventh_open = eight_open = nine_open = True

font = pygame.font.Font('fonts/LTYPEB.ttf', 50)
go_text = font.render('GAME OVER!', True, (255, 255, 0))
font_2 = pygame.font.Font('fonts/LTYPEB.ttf', 15)
copy = font_2.render('By SHIVANG', True, (0, 0, 0))
reset = font_2.render('Press SPACE to restart!', True, (0, 0, 0))
draw = True
run = True
score = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(random.choice(colours))
                score = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                first_open = second_open = third_open = fourth_open = fifth_open = sixth_open = seventh_open = eight_open = nine_open = True
                first = pygame.draw.rect(screen, (255, 0, 0), (50, 50, 150, 150))  # side_difference =160
                second = pygame.draw.rect(screen, (255, 0, 0), (210, 50, 150, 150))
                third = pygame.draw.rect(screen, (255, 0, 0), (370, 50, 150, 150))

                fourth = pygame.draw.rect(screen, (255, 0, 0), (50, 210, 150, 150))
                fifth = pygame.draw.rect(screen, (255, 0, 0), (210, 210, 150, 150))
                sixth = pygame.draw.rect(screen, (255, 0, 0), (370, 210, 150, 150))

                seventh = pygame.draw.rect(screen, (255, 0, 0), (50, 370, 150, 150))
                eight = pygame.draw.rect(screen, (255, 0, 0), (210, 370, 150, 150))
                nine = pygame.draw.rect(screen, (255, 0, 0), (370, 370, 150, 150))

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if first.collidepoint(pos) and first_open:
                sound.play()

                if turn == 'player1':
                    score[0][0] = 1
                    first_new = pygame.draw.rect(screen, (0, 0, 128), (50, 50, 150, 150))
                    turn = 'player2'
                else:
                    score[0][0] = 2
                    pygame.draw.rect(screen, (0, 0, 0), (50, 50, 150, 150))
                    turn = 'player1'
                first_open = False
            if second.collidepoint(pos) and second_open:
                sound.play()

                if turn == 'player1':
                    score[0][1] = 1
                    second_new = pygame.draw.rect(screen, (0, 0, 128), (210, 50, 150, 150))
                    turn = 'player2'
                else:
                    score[0][1] = 2
                    pygame.draw.rect(screen, (0, 0, 0), (210, 50, 150, 150))
                    turn = 'player1'
                second_open = False

            if third.collidepoint(pos) and third_open:
                sound.play()

                if turn == 'player1':
                    score[0][2] = 1
                    third_new = pygame.draw.rect(screen, (0, 0, 128), (370, 50, 150, 150))
                    turn = 'player2'
                else:
                    score[0][2] = 2

                    pygame.draw.rect(screen, (0, 0, 0), (370, 50, 150, 150))
                    turn = 'player1'
                third_open = False

            if fourth.collidepoint(pos) and fourth_open:
                sound.play()
                if turn == 'player1':
                    score[1][0] = 1
                    fourth_new = pygame.draw.rect(screen, (0, 0, 128), (50, 210, 150, 150))
                    turn = 'player2'
                else:
                    score[1][0] = 2
                    pygame.draw.rect(screen, (0, 0, 0), (50, 210, 150, 150))
                    turn = 'player1'
                fourth_open = False

            if fifth.collidepoint(pos) and fifth_open:
                sound.play()
                if turn == 'player1':
                    score[1][1] = 1
                    fifth_new = pygame.draw.rect(screen, (0, 0, 128), (210, 210, 150, 150))
                    turn = 'player2'
                else:
                    score[1][1] = 2
                    pygame.draw.rect(screen, (0, 0, 0), (210, 210, 150, 150))
                    turn = 'player1'
                fifth_open = False

            if sixth.collidepoint(pos) and sixth_open:
                sound.play()
                if turn == 'player1':
                    score[1][2] = 1
                    sixth_new = pygame.draw.rect(screen, (0, 0, 128), (370, 210, 150, 150))
                    turn = 'player2'
                else:
                    score[1][2] = 2
                    pygame.draw.rect(screen, (0, 0, 0), (370, 210, 150, 150))
                    turn = 'player1'
                sixth_open = False

            if seventh.collidepoint(pos) and seventh_open:
                sound.play()
                if turn == 'player1':
                    score[2][0] = 1
                    seventh_new = pygame.draw.rect(screen, (0, 0, 128), (50, 370, 150, 150))
                    turn = 'player2'
                else:
                    score[2][0] = 2
                    pygame.draw.rect(screen, (0, 0, 0), (50, 370, 150, 150))
                    turn = 'player1'
                seventh_open = False

            if eight.collidepoint(pos) and eight_open:
                sound.play()
                if turn == 'player1':
                    score[2][1] = 1
                    eight_new = pygame.draw.rect(screen, (0, 0, 128), (210, 370, 150, 150))
                    turn = 'player2'
                else:
                    score[2][1] = 2
                    pygame.draw.rect(screen, (0, 0, 0), (210, 370, 150, 150))
                    turn = 'player1'
                eight_open = False

            if nine.collidepoint(pos) and nine_open:
                sound.play()

                if turn == 'player1':
                    score[2][2] = 1
                    nine_new = pygame.draw.rect(screen, (0, 0, 128), (370, 370, 150, 150))
                    turn = 'player2'
                else:
                    score[2][2] = 2
                    pygame.draw.rect(screen, (0, 0, 0), (370, 370, 150, 150))
                    turn = 'player1'
                nine_open = False
            if ((score[0][0] == 1 and score[0][1] == 1 and score[0][2] == 1) or (
                    score[1][0] == 1 and score[1][1] == 1 and score[1][2] == 1) or (
                        score[2][0] == 1 and score[2][1] == 1 and score[2][2] == 1)) or (
                    score[0][0] == 2 and score[1][0] == 2 and score[2][0] == 2) or (
                    score[0][1] == 2 and score[1][1] == 2 and score[2][1] == 2) or (
                    score[0][2] == 2 and score[1][2] == 2 and score[2][2] == 2) or (
                    score[0][0] == 1 and score[1][0] == 1 and score[2][0] == 1) or (
                    score[0][1] == 1 and score[1][1] == 1 and score[2][1] == 1) or (
                    score[0][2] == 1 and score[1][2] == 1 and score[2][2] == 1) or (
                    score[0][0] == 2 and score[0][1] == 2 and score[0][2] == 2) or (
                    score[1][0] == 2 and score[1][1] == 2 and score[1][2] == 2) or (
                    score[2][0] == 2 and score[2][1] == 2 and score[2][2] == 2) or (
                    score[0][0] == 1 and score[1][1] == 1 and score[2][2] == 1) or (
                    score[0][0] == 2 and score[1][1] == 2 and score[2][2] == 2) or (
                    score[0][2] == 1 and score[1][1] == 1 and score[2][0] == 1) or (
                    score[0][2] == 2 and score[1][1] == 2 and score[2][0] == 2):
                screen.blit(go_text, (WIDTH / 2 - 150, HEIGHT / 2 - 30))
                screen.blit(copy, (WIDTH / 2 - 50, HEIGHT - 17))
                screen.blit(reset, (WIDTH / 2 - 80, HEIGHT - 35))

    pygame.display.update()
