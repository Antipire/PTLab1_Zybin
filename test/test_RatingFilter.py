from src.CalcRating import CalcRating
from src.Types import DataType, RatingType
from src.RatingFilter import RatingFilter
import pytest


class TestRatingFilter:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 70),
                    ("русский язык", 70),
                    ("программирование", 70),
                    ("литература", 70)
                ]
        }

        filtered_rating = {
            "Петров Игорь Владимирович": 70
        }

        return data, filtered_rating

    def test_init_filter_rating(self, input_data: tuple[RatingType, RatingType]) -> None:
        filter_rating = RatingFilter(input_data[0])
        assert input_data[0] == filter_rating.data

    def test_filter_second_quantile(self, input_data: tuple[DataType, RatingType]) -> None:
        calc_rating = CalcRating(input_data[0]).calc()
        filter_rating = RatingFilter(calc_rating).filter_get_second_quantile()

        assert pytest.approx(filter_rating) == input_data[1]

