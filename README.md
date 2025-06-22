This Python script automates applying to LinkedIn jobs using the Easy Apply feature. It logs into LinkedIn, searches for jobs based on a specified job title and location, applies filters like experience level and Easy Apply only, then iterates through job listings to submit applications automatically.


1.Features:

- Logs into LinkedIn with your email and password

- Searches jobs by title and location

- Applies Easy Apply filter and experience level filter

- Iterates over jobs and submits applications with provided phone number

- Skips complex/multi-step applications automatically

- Handles pagination and continues applying on multiple pages

2.USAGE:

- Update the script with your LinkedIn credentials, phone number, desired job title, and location
Run the script
- If a CAPTCHA appears, solve it manually and press Enter on terminal to continue.


3. Assumptions & Limitations:

-Only supports simple Easy Apply jobs:
The script handles only single-step Easy Apply forms. Multi-step or complex applications (with multiple pages or extra questions) are skipped automatically.

-Manual CAPTCHA solving required:
The script does not bypass LinkedIn CAPTCHA or other anti-bot measures. You must solve CAPTCHA manually if prompted.

-Static element locators:
The script uses hard-coded XPath and CSS selectors which may break if LinkedIn changes its site layout.

-Basic error handling:
Handles some common Selenium exceptions but may fail on unexpected page behaviors or network issues.

-No resume upload:
This version assumes your profile is complete on LinkedIn and your resume is already uploaded. It does not upload a resume or cover letter automatically.

Ethical use only:
Use responsibly and according to LinkedIn’s terms of service. Avoid spammy or excessive applications.
