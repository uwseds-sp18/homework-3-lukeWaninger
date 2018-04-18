import unittest
import homework3


class TestHomework(unittest.TestCase):
    def test_create_df(self):
        self.assertTrue(homework3.create_dataframe() is not None)

    def test_create_df_throws_as_expected(self):
        self.assertRaises(ValueError, homework3.create_dataframe, '-')

    def test_create_df_returns_rows(self):
        self.assertTrue(len(homework3.create_dataframe()) > 10)

    def test_column_names(self):
        self.assertTrue(sum(homework3.create_dataframe().columns == ["video_id", "category_id", "language"]) == 3)

    def test_composite_key(self):
        df = homework3.create_dataframe()
        a = df.shape[0]
        b = df.groupby(["video_id", "language", "category_id"]).apply(len).shape[0]
        self.assertTrue(a == b)

