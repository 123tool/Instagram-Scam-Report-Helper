import os
from datetime import datetime

def generate_report(username,country,reason):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/report_{username}.txt"

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"""
INSTAGRAM SCAM REPORT
==============================

Username : @{username}
Country  : {country}
Reason   : {reason}

Reported Date : {date}

Description:
This account is suspected of scam or fraudulent activity.
Please review the account and take appropriate action.

Reporter:
Anonymous User

==============================
"""

    with open(filename,"w") as f:
        f.write(content)

    return filename
