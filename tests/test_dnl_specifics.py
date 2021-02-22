import pytest
import datefinder
from datetime import datetime
import sys
import logging

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)

today = datetime.today()

@pytest.mark.parametrize(
    ("input_text", "expected_date", "first"),
    [
        ("Tuesday Jul 22, 2014", datetime(2014, 7, 22), "day"),
        ("At December 31, 2017", datetime(2017, 12, 31), "day"),
        ("Mär 13 2000", datetime(2000, 3, 13), "day"),
        ("jan. 1, 2018 1", datetime(2018, 1, 1), "day"),
        ("Jan. 1", datetime(2021, 1, 1), "day"),

        ("2.81", None, "day"),
        ("12.81", None, "day"),
        ("123.81", None, "day"),
        ("2,81", None, "day"),
        ("12,81", None, "day"),
        ("123,81", None, "day"),
        ("12,383", None, "day"),

        ("80,108", None, "day"),
        ("(12)", None, "day"),
    ]

)
def test_dnl_date_strings(input_text, expected_date, first):
    for return_date in datefinder.find_dates(input_text, first=first, strict=True):
        assert return_date == expected_date