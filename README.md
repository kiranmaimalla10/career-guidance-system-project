Career Guidance System
A Python-based mini project that recommends suitable career paths to a user based on their skills, interests, and education level. The system uses a weighted matching algorithm against a curated career database and returns a ranked list of the best-fit careers with a percentage match score.
Features
Interactive command-line interface for entering skills, interests, and education
Weighted scoring algorithm (skills, interests, and education level all contribute to the final match)
Database of 20 careers spanning Technology, Business, Design, Finance, Engineering, Healthcare, Education, and Media
Top-N ranked recommendations with match percentage, matched skills/interests, average salary, and growth outlook
Clean, modular code separated into data, matching logic, and interface layers
Includes unit tests for the core recommendation engine
Tech Stack
Language: Python 3
Libraries: Standard library only (json, os, unittest) — no external dependencies required
Project Structure
career-guidance-system/
├── data/
│   └── careers.json        # Career database (skills, interests, education, salary, outlook)
├── src/
│   ├── __init__.py
│   └── matcher.py           # Core recommendation engine (UserProfile, CareerGuidanceSystem)
├── tests/
│   └── test_matcher.py      # Unit tests for the matching engine
├── main.py                  # CLI entry point
└── README.md
How It Works
The user enters a comma-separated list of skills and interests, plus their education level.
For every career in data/careers.json, the engine computes three sub-scores:
Skill match — fraction of the career's required skills the user has
Interest match — fraction of the career's associated interests the user shares
Education match — whether the user's education level fits the career's typical requirement
These are combined into a final weighted score:
final_score = (skill_score × 0.55) + (interest_score × 0.35) + (education_score × 0.10)
Careers are sorted by final score and the top 5 are displayed, along with which specific skills/interests matched.
Installation
git clone https://github.com/kiranmaimalla10/career-guidance-system-project.git
cd career-guidance-system-project
No external dependencies are required — only Python 3.7+.
Usage
Run the program from the project root:
python main.py
You'll be prompted for:
Enter your skills (comma-separated): python, machine learning, sql, statistics
Enter your interests (comma-separated): problem solving, research, analytics
Your education level (diploma/bachelors/masters/mba/phd): bachelors
Sample Output
============================================================
TOP CAREER RECOMMENDATIONS
============================================================

1. Data Scientist  (80.2% match)
   Industry       : Technology
   Description    : Analyzes complex datasets to extract insights and build predictive models that drive business decisions.
   Matched Skills : machine learning, python, sql, statistics
   Matched Interests: analytics, problem solving, research
   Avg. Salary    : 6-18 LPA
   Growth Outlook : High

2. Machine Learning Engineer  (40.8% match)
   ...
Running Tests
python -m unittest discover tests
Future Improvements
Add a web interface (Flask/Streamlit) for a more interactive experience
Expand the career database and support user-supplied datasets
Incorporate skill-gap analysis (what skills a user needs to learn for a target career)
Add personality/aptitude-based inputs alongside skills and interests
Deploy as a web app with persistent user profiles
Author
MSS Kiranmai GitHub: github.com/kiranmaimalla10/career-guidance-system-project
License
This project is open source and available for educational use.