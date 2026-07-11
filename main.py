"""
main.py
--------
Command-line entry point for the Career Guidance System.

Run this file to interactively enter your skills, interests, and
education level, and receive a ranked list of recommended careers.

Usage:
    python main.py
"""

from src.matcher import CareerGuidanceSystem, UserProfile

VALID_EDUCATION_LEVELS = ["diploma", "bachelors", "masters", "mba", "phd"]


def get_list_input(prompt: str) -> list:
    raw = input(prompt).strip()
    if not raw:
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


def get_education_input() -> str:
    while True:
        edu = input(
            f"Your education level ({'/'.join(VALID_EDUCATION_LEVELS)}): "
        ).strip().lower()
        if edu in VALID_EDUCATION_LEVELS:
            return edu
        print(f"Please enter one of: {', '.join(VALID_EDUCATION_LEVELS)}")


def print_recommendations(recommendations: list) -> None:
    print("\n" + "=" * 60)
    print("TOP CAREER RECOMMENDATIONS")
    print("=" * 60)

    if not recommendations or recommendations[0]["match_percent"] == 0:
        print("No strong matches found. Try adding more skills or interests.")
        return

    for rank, career in enumerate(recommendations, start=1):
        print(f"\n{rank}. {career['title']}  ({career['match_percent']}% match)")
        print(f"   Industry       : {career['industry']}")
        print(f"   Description    : {career['description']}")
        print(f"   Matched Skills : {', '.join(career['matched_skills']) or 'None'}")
        print(f"   Matched Interests: {', '.join(career['matched_interests']) or 'None'}")
        print(f"   Avg. Salary    : {career['average_salary_inr']}")
        print(f"   Growth Outlook : {career['growth_outlook']}")

    print("\n" + "=" * 60)


def main():
    print("=" * 60)
    print("  CAREER GUIDANCE SYSTEM")
    print("  Get personalized career recommendations based on your")
    print("  skills, interests, and education.")
    print("=" * 60 + "\n")

    skills = get_list_input("Enter your skills (comma-separated): ")
    interests = get_list_input("Enter your interests (comma-separated): ")
    education = get_education_input()

    profile = UserProfile(skills=skills, interests=interests, education=education)
    system = CareerGuidanceSystem()
    recommendations = system.recommend(profile, top_n=5)

    print_recommendations(recommendations)


if __name__ == "__main__":
    main()
