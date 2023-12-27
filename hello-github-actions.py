import os

def main():
    user = os.getenv('USER')
    print(f'Hello from Github Actions {user}')

if __name__ == '__main__':
    main()
