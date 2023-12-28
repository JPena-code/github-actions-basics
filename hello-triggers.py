import os


def main():
    language = os.getenv('LANGUAGE')
    user = os.getenv('USER')

    print(f'Hello "{user}" and your favorite language "{language}"')

if __name__ == '__main__':
    main()
