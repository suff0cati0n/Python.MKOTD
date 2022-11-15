from os import environ as env
from dotenv import load_dotenv
load_dotenv()

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    print('API_KEY:  {}'.format(env['TEST_KEY']))


if __name__ == '__main__':
    main()
