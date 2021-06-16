import argparse
from bibliostream import BiblioStream
from database import Database


def main() -> None:
    # Create instance of argument parser
    parser = argparse.ArgumentParser(description="Pass database config")

    # Define argument for database config file path
    parser.add_argument("DatabaseConfigPath", metavar="path", type=str)

    # Parse provided argument from CLI
    args = parser.parse_args()

    if args.DatabaseConfigPath != None:
        # Create an instance of the Database
        db = Database(args.DatabaseConfigPath)
        bs = BiblioStream(db)
        print(bs.aggregate_movie_length("max"))
        bs.end_session()


if __name__ == "__main__":
    main()
