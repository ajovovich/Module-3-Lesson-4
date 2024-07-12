#Task 1:Python Regular Expressions Deep Dive


import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(pattern, text)

filtered_emails = [email for email in emails if not email.endswith('@exclude.com')]

print(filtered_emails)
