import requests
import csv
from datetime import datetime

# GitHub username
username = 'muhammadnavas'

# Optional: Add your personal access token here if needed (for higher rate limits)
# token = 'YOUR_PERSONAL_ACCESS_TOKEN'
# headers = {
#     'Authorization': f'token {token}'
# }

headers = {
    'Accept': 'application/vnd.github.v3+json'
}

# List to store all repositories data
repo_data = []

# Pagination setup
page = 1
per_page = 100  # maximum allowed by GitHub API

print("Fetching repository data...")

while True:
    url = f'https://api.github.com/users/{username}/repos?per_page={per_page}&page={page}'
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to fetch data. Status code:", response.status_code)
        print(response.json())
        break

    repos = response.json()
    
    if not repos:
        print("All repositories fetched.")
        break

    for repo in repos:
        repo_data.append([
            repo['name'],
            repo['stargazers_count'],
            repo['forks_count'],
            repo['watchers_count'],
            repo['open_issues_count'],
            repo['pushed_at']
        ])
    
    print(f"Page {page} fetched with {len(repos)} repositories.")
    page += 1

# CSV file path
csv_file = 'github_repos.csv'

# Write data to CSV
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Stars', 'Forks', 'Watchers', 'Open Issues', 'Last Push'])
    writer.writerows(repo_data)

print(f"\nCSV file '{csv_file}' created successfully with {len(repo_data)} repositories.")
