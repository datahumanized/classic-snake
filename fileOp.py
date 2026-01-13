
high_score = int(input("Input your high score: "))

with open('score.txt', mode = 'r') as file:
    content = int(file.read())
print(f"Previous high sore: {content:,}")


if high_score > int(content):
    with open('score.txt', mode='r+') as file:

        file.write(f"{high_score}")