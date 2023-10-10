from src.main import get_path_from_arguments
import pytest


@pytest.fixture()
def correct_arguments_string() -> tuple[list[str], str]:
    return ["-p", "../data/data.yaml"], "../data/data.yaml"


@pytest.fixture()
def incorrect_arguments_string() -> list[str]:
    return ["../data/data.yaml"]


def test_get_path_from_correct_arguments(correct_arguments_string:
                                         tuple[list[str], str]) -> None:
    path = get_path_from_arguments(correct_arguments_string[0])
    assert path == correct_arguments_string[1]


def test_get_path_from_incorrect_arguments(
        incorrect_arguments_string) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(incorrect_arguments_string[0])
    assert e.type == SystemExit
