import unittest
from grapher import DATE_FORMAT, fetch_data, filter_data
from datetime import datetime


class TestGrapher(unittest.TestCase):
    def test_is_working(self):
        self.assertEqual(True, True)

    def test_fetch_data(self):
        data = fetch_data()
        self.assertTrue(isinstance(data, dict))

    def test_filter_data(self):
        data = fetch_data()
        filtered_data, labels = filter_data(
            list(data.values()),
            list(data.keys()),
            datetime.strptime("04-01-2022", DATE_FORMAT),
            datetime.strptime("09-01-2022", DATE_FORMAT),
        )
        self.assertTrue(len(labels) == 6)
        self.assertEquals(len(labels), len(filtered_data))


class TestGrapherCornerCases(unittest.TestCase):
    def setUp(self):
        self.data = {
            "01-11-2021": 200,
            "01-01-2022": 300,
            "02-01-2022": 500,
            "04-01-2022": 1300,
            "06-01-2022": 3000,
            "07-01-2022": 3500,
            "08-01-2022": 4000,
            "09-01-2022": 4500,
            "10-01-2022": 5000,
            "11-01-2022": 20000,
            "12-01-2022": 35000,
            "13-01-2022": 46000,
            "14-01-2022": 70000,
            "15-01-2022": 90000,
            "18-01-2022": 100000,
            "19-01-2022": 190000,
        }

    def test_end_date_not_in_data(self):
        data, labels = filter_data(
            list(self.data.values()),
            list(self.data.keys()),
            datetime.strptime("04-01-2022", DATE_FORMAT),
            datetime.strptime("16-01-2022", DATE_FORMAT),
        )
        self.assertTrue(len(labels) == 11)
        self.assertEquals(len(labels), len(data))
        self.assertFalse("18-01-2022" in labels)
        self.assertFalse("16-01-2022" in labels)
        self.assertTrue("15-01-2022" in labels)

    def test_start_date_not_in_data(self):
        data, labels = filter_data(
            list(self.data.values()),
            list(self.data.keys()),
            datetime.strptime("04-11-2021", DATE_FORMAT),
            datetime.strptime("12-01-2022", DATE_FORMAT),
        )
        self.assertTrue(len(labels) == 10)
        self.assertEquals(len(labels), len(data))
        self.assertFalse("01-11-2021" in labels)
        self.assertTrue("01-01-2022" in labels)
        self.assertTrue("12-01-2022" in labels)

    def test_start_and_end_date_not_in_data(self):
        data, labels = filter_data(
            list(self.data.values()),
            list(self.data.keys()),
            datetime.strptime("04-11-2021", DATE_FORMAT),
            datetime.strptime("17-01-2022", DATE_FORMAT),
        )
        self.assertTrue(len(labels) == 13)
        self.assertEquals(len(labels), len(data))
        self.assertFalse("01-11-2021" in labels)
        self.assertTrue("01-01-2022" in labels)
        self.assertTrue("12-01-2022" in labels)

        # for case when the end date and start date is same and both is not in data
        data, labels = filter_data(
            list(self.data.values()),
            list(self.data.keys()),
            datetime.strptime("17-01-2022", DATE_FORMAT),
            datetime.strptime("17-01-2022", DATE_FORMAT),
        )
        self.assertTrue(len(labels) == 0)
        self.assertEquals(len(labels), len(data))

        # for case the end date and start date are not in data and no data in the range
        data, labels = filter_data(
            list(self.data.values()),
            list(self.data.keys()),
            datetime.strptime("16-11-2022", DATE_FORMAT),
            datetime.strptime("17-01-2022", DATE_FORMAT),
        )
        self.assertTrue(len(labels) == 0)
        self.assertEquals(len(labels), len(data))


if __name__ == "__main__":
    unittest.main()
