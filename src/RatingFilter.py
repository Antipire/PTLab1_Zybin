from src.Types import RatingType


class RatingFilter:

    def __init__(self, data: RatingType) -> None:
        self.data = data
        self.filtered_rating = {}

    def filter_get_first_quantile(self) -> RatingType:
        rating: int
        for person, rating in self.data.items():
            if 76 < rating <= 100:
                self.filtered_rating[person] = rating

        return self.filtered_rating

    def filter_get_second_quantile(self) -> RatingType:
        rating: int
        for person, rating in self.data.items():
            if 50 < rating <= 75:
                self.filtered_rating[person] = rating

        return self.filtered_rating

    def filter_get_third_quantile(self) -> RatingType:
        rating: int
        for person, rating in self.data.items():
            if 25 < rating <= 50:
                self.filtered_rating[person] = rating

        return self.filtered_rating

    def filter_get_fourth_quantile(self) -> RatingType:
        rating: int
        for person, rating in self.data.items():
            if 0 < rating <= 25:
                self.filtered_rating[person] = rating

        return self.filtered_rating
