import argparse

def main():
    parser = argparse.ArgumentParser(
            prog='pygit'
            description='my own simple git implementation')

    args = parser.parse_args()

    print(args)
