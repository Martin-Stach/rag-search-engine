import argparse
from lib.search_utils import load_movies
from lib.keyword_search import keyword_search

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    movies = load_movies()

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")
            result = keyword_search(movies, args.query)
            for i, res in enumerate(result, 1):
                if i >= 6:
                    print(f"...")
                    break
                print(f"{i}. {res}")
                
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()
