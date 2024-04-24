import psycopg2
import pygame
import time
import random

def create_tables():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS "user" (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS user_score (
        user_id INT REFERENCES "user"(user_id),
        level INT,
        score INT,
        CONSTRAINT user_score_pk PRIMARY KEY (user_id, level)
    );
    """)
    conn.commit()

def get_user(username):
    cur.execute("SELECT user_id FROM \"user\" WHERE username = %s;", (username,))
    result = cur.fetchone()
    return result

def create_user(username, cur):
    cur.execute("INSERT INTO \"user\" (username) VALUES (%s) RETURNING user_id;", (username,))
    conn.commit()
    return cur.fetchone()[0]

def get_user_level(user_id):
    cur.execute("SELECT level FROM user_score WHERE user_id = %s ORDER BY level DESC LIMIT 1;", (user_id,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        return None

def save_score(user_id, level, score):
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s);", (user_id, level, score))
    conn.commit()

if __name__ == '__main__':
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="raikhan1", port=5432)
    cur = conn.cursor()

    create_tables()

    username = input("Enter your username: ")
    user = get_user(username)
    if user:
        user_id = user[0]
        print(f'Welcome back, {username}! Your current level is {get_user_level(user_id)}')
    else:
        user_id = create_user(username, cur)
        print(f'User {username} created successfully!')

    snake_speed = 9

    window_x, window_y = 720, 480

    pygame.init()

    pygame.display.set_caption('Raikhan\'s Snake game')
    game_window = pygame.display.set_mode((window_x, window_y))

    fps = pygame.time.Clock()

    snake_position = [100, 50]
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 204)
    pink = (255, 51, 255)

    snake_body = [[100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
                ]
    fruit_positions = [[random.randrange(1, (window_x//10)) * 10,
                        random.randrange(1, (window_y//10)) * 10]]

    direction = 'RIGHT'
    change_to = direction

    score = 0
    level = 1  # Initialize level

    def show_score_and_level(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render(f'Score: {score}  Level: {level}', True, color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

    def game_over():
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render(
            f'Your Score is : {score}          Level: {level}', True, green)
        save_score(user_id, level, score)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))

        if score == 20:
            while len(fruit_positions) < 4:
                fruit_positions.append([random.randrange(1, (window_x//10)) * 10,
                                        random.randrange(1, (window_y//10)) * 10])

        fruit_eaten = False
        for i, fruit_position in enumerate(fruit_positions):
            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                score += 10
                fruit_eaten = True
                del fruit_positions[i]
                break

        if not fruit_eaten:
            snake_body.pop()
        else:
            if len(fruit_positions) < 4:
                fruit_positions.append([random.randrange(1, (window_x//10)) * 10,
                                        random.randrange(1, (window_y//10)) * 10])

        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, white,
                            pygame.Rect(pos[0], pos[1], 10, 10))

        for fruit_position in fruit_positions:
            pygame.draw.rect(game_window, white, pygame.Rect(
                fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        show_score_and_level(1, pink, 'times new roman', 20)

        if score >= level * 20:  
            level += 1
            snake_speed += 1  

        pygame.display.update()

        fps.tick(snake_speed)
