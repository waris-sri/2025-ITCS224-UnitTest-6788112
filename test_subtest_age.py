import unittest
from age import categorize_by_age


class TestAgeWithSubTest(unittest.TestCase):
    def test_age_categories(self):
        categories = [
            ("Child", range(0, 10)),
            ("Adolescent", range(10, 19)),
            ("Adult", range(19, 66)),
        ]
        print()
        for category, ages in categories:
            for age in ages:
                with self.subTest(category=category, age=age):
                    result = categorize_by_age(age)
                    print(f"{age} is considered as a {category}.")
                    self.assertEqual(result, category)
            print("=" * 50)


if __name__ == "__main__":
    unittest.main(verbosity=2)
