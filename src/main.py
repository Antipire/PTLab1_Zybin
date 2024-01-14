import argparse
import sys
from src.CalcRating import CalcRating
from src.TextDataReader import TextDataReader
from src.RatingFilter import RatingFilter


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = TextDataReader()
    students = reader.read(path)
    print(f"Students: {students}")
    rating = CalcRating(students).calc()

    sorted_students = dict(sorted(rating.items(), key=lambda item: item[1]))
    print("Sorted students with rating: ", sorted_students)
    filtered_rating = RatingFilter(rating).filter_get_second_quantile()
    print("Rating: ", filtered_rating)


if __name__ == "__main__":
    main()
