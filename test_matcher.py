"""
test_matcher.py
-----------------
Basic unit tests for the Career Guidance System's matching engine.

Run with:
    python -m unittest discover tests
"""

import unittest
from src.matcher import CareerGuidanceSystem, UserProfile


class TestCareerGuidanceSystem(unittest.TestCase):

    def setUp(self):
        self.system = CareerGuidanceSystem()

    def test_careers_loaded(self):
        self.assertGreater(len(self.system.careers), 0)

    def test_strong_match_for_data_scientist_profile(self):
        profile = UserProfile(
            skills=["python", "statistics", "machine learning", "sql"],
            interests=["problem solving", "analytics", "research"],
            education="bachelors",
        )
        results = self.system.recommend(profile, top_n=3)
        top_titles = [r["title"] for r in results]
        self.assertIn("Data Scientist", top_titles)
        self.assertGreater(results[0]["match_percent"], 50)

    def test_empty_profile_returns_low_scores(self):
        profile = UserProfile(skills=[], interests=[], education="bachelors")
        results = self.system.recommend(profile, top_n=3)
        for r in results:
            self.assertLessEqual(r["match_percent"], 20)

    def test_recommend_respects_top_n(self):
        profile = UserProfile(
            skills=["python"], interests=["technology"], education="bachelors"
        )
        results = self.system.recommend(profile, top_n=2)
        self.assertEqual(len(results), 2)


if __name__ == "__main__":
    unittest.main()
