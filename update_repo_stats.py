import requests
import csv
from datetime import datetime

owner = "microsoft"
repo = "vscode"
filename = "vscode_repo_stats.csv"

url = f"https://api.github.com/repos/{owner}/{repo}"
headers = {}  # No token used

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)

data = response.json()

repo_name = data.get("full_name", "")
stars = data.get("stargazers_count", 0)
forks = data.get("forks_count", 0)
watchers = data.get("watchers_count", 0)
open_issues = data.get("open_issues_count", 0)
last_push = data.get("pushed_at", "")
fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(filename, "a", newline="") as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(["repo_name", "stars", "forks", "watchers", "open_issues", "last_push", "fetch_time"])
    writer.writerow([repo_name, stars, forks, watchers, open_issues, last_push, fetch_time])

print("Repo stats updated!")
