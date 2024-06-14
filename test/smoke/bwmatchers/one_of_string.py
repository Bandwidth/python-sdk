from typing import Any

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from hamcrest.core.matcher import Matcher


class IsOneOfString(BaseMatcher[Any]):
    def __init__(self, equalsAnyString: Any) -> None:
        self.object = equalsAnyString

    def _matches(self, item: Any) -> bool:
        if isinstance(self.object, list):
            return  item in self.object
        return False

    def describe_to(self, description: Description) -> None:
        nested_matcher = isinstance(self.object, Matcher)
        description.append_description_of("one of ")
        if nested_matcher:
            description.append_text("<")
        description.append_description_of(self.object)
        if nested_matcher:
            description.append_text(">")


def is_one_of_string(obj: Any) -> Matcher[Any]:
    """Matches expected string is in a given list.

    :param obj: The object to compare against as the expected value.

    This matcher compares the evaluated object to ``obj`` for a match."""
    return IsOneOfString(obj)
