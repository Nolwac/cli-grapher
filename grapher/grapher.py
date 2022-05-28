from urllib.request import urlopen
import json
from urllib.error import URLError
from cache import CacheControl
from termgraph.module import Data, BarChart, Args, Colors
from datetime import datetime


cache = CacheControl("data.json")
DATE_FORMAT = "%d-%m-%Y"


def fetch_data(url: str = "http://sam-user-activity.eu-west-1.elasticbeanstalk.com/") -> dict:
    data = cache.load_data()
    if data is not None:
        return data
    try:
        response = urlopen(url)
        data = json.loads(response.read())
        cache.cache_data(data)
        return data
    except URLError as e:
        print(e)


def draw_chart(data: list[int], labels: list[str], title: str = "Bar Chart of Number of user per day") -> None:
    data = Data(data, labels)
    chart = BarChart(
        data,
        Args(
            title=title,
            colors=[Colors.Red, Colors.Magenta],
            space_between=True,
        ),
    )
    chart.draw()


def binary_search(value: datetime, array: list[str], kind: str = "start") -> int:
    start_index = 0
    length = len(array)
    end_index = length - 1
    midpoint = 0
    while start_index <= end_index:
        midpoint = (end_index + start_index) // 2
        if value == datetime.strptime(array[midpoint], DATE_FORMAT):
            return midpoint
        elif value > datetime.strptime(array[midpoint], DATE_FORMAT):
            start_index = midpoint + 1
            if kind == "start":
                midpoint = midpoint + 1
        else:
            end_index = midpoint - 1
            if kind == "end":
                midpoint = midpoint - 1
    return midpoint


def filter_data(
    data: list[int], data_keys: list[str], start_date: datetime, end_date: datetime
) -> tuple[list[int], list[str]]:
    # a more optimized algorithm would be to search for the start date and end date
    # using binary search algorithm since, the dates are orderd.
    # The binary tree will be modified such that if the start or end date is not found, then the
    # index of the closest date to it will be returned
    # until a date greater than the end date is reached
    # the search will take logarithmic time, O(logN), where N is length of data.

    # check if range is valid
    if start_date > end_date:
        print("no data of date in that range: start date must be less than or equal to end date")
        return [], []
    # find start date by binary search
    start_index = binary_search(start_date, data_keys, kind="start")
    end_index = binary_search(end_date, data_keys, kind="end")
    return data[start_index : end_index + 1], data_keys[start_index : end_index + 1]
