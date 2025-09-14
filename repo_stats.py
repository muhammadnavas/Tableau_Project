import requests
import csv

username = 'muhammadnavas'
headers = {'Accept': 'application/vnd.github.v3+json'}

repo_data = []
page = 1
per_page = 100

print("Fetching repository data...")

while True:
    url = f'https://api.github.com/users/{username}/repos?per_page={per_page}&page={page}'
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching page {page}. Status code:", response.status_code)
        break

    repos = response.json()
    if not repos:
        break

    for repo in repos:
        repo_name = repo['name']

        # Count total commits
        total_commits = 0
        merge_commits = 0
        commits_page = 1

        while True:
            commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits?per_page=100&page={commits_page}"
            commits_response = requests.get(commits_url, headers=headers)
            if commits_response.status_code != 200:
                total_commits = 'N/A'
                merge_commits = 'N/A'
                break

            commits = commits_response.json()
            if not commits:
                break

            total_commits += len(commits)
            merge_commits += sum(1 for c in commits if 'Merge' in c['commit']['message'])
            commits_page += 1

        repo_data.append([
            repo_name,
            repo['language'],
            repo['created_at'],
            repo['updated_at'],
            total_commits,
            merge_commits,
            repo['stargazers_count'],
            repo['forks_count'],
            repo['watchers_count'],
            repo['open_issues_count'],
            repo['default_branch'],
            repo['pushed_at'],
            repo['html_url']
        ])
    page += 1

csv_file = 'github_repos_total_commits.csv'

with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Name', 'Language', 'Created At', 'Updated At',
        'Total Commits', 'Merge Commits',
        'Stars', 'Forks', 'Watchers', 'Open Issues',
        'Default Branch', 'Last Push', 'URL'
    ])
    writer.writerows(repo_data)

print(f"CSV '{csv_file}' created successfully with {len(repo_data)} repositories.")
