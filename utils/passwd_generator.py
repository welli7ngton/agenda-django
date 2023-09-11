import string
import random


def characters():

    special = "!@#$%&*-_+?/"

    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        special
    )
    return list(characters)


def generate_passwd(characters: list[str]):

    passwd = [
        characters[random.randint(0, len(characters) - 1)]
        for _ in range(0, 12)
        ]
    random_passwd = ''
    for i in passwd:
        random_passwd += i

    print(random_passwd)


foo = characters()

generate_passwd(foo)
