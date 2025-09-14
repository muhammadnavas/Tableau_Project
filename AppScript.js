function fetchGitHubRepoStats() {
  var username = "muhammadnavas";
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("GitHubData");
  if (!sheet) {
    sheet = SpreadsheetApp.getActiveSpreadsheet().insertSheet("GitHubData");
  }
  sheet.clear();

  // Headers
  sheet.appendRow([
    "Repo Name", "Language", "Stars", "Forks", "Watchers",
    "Open Issues", "Total Commits", "Merge Commits", "URL"
  ]);

  var headers = {
    "Accept": "application/vnd.github.v3+json"
    // For higher rate limit, add: "Authorization": "token YOUR_PERSONAL_ACCESS_TOKEN"
  };

  // Fetch repositories
  var page = 1;
  while (true) {
    var url = "https://api.github.com/users/" + username + "/repos?per_page=100&page=" + page;
    var response = UrlFetchApp.fetch(url, { "method": "get", "headers": headers });
    if (response.getResponseCode() != 200) break;

    var repos = JSON.parse(response.getContentText());
    if (repos.length == 0) break;

    for (var i = 0; i < repos.length; i++) {
      var repo = repos[i];
      var repoName = repo.name;
      var totalCommits = 0;
      var mergeCommits = 0;
      var commitsPage = 1;

      // Fetch commits in pages
      while (true) {
        var commitsUrl = "https://api.github.com/repos/" + username + "/" + repoName + "/commits?per_page=100&page=" + commitsPage;
        var commitsResponse = UrlFetchApp.fetch(commitsUrl, { "method": "get", "headers": headers });
        if (commitsResponse.getResponseCode() != 200) {
          totalCommits = "N/A";
          mergeCommits = "N/A";
          break;
        }

        var commits = JSON.parse(commitsResponse.getContentText());
        if (commits.length == 0) break;

        totalCommits += commits.length;
        mergeCommits += commits.filter(c => c.commit.message.includes("Merge")).length;
        commitsPage++;
      }

      sheet.appendRow([
        repoName,
        repo.language,
        repo.stargazers_count,
        repo.forks_count,
        repo.watchers_count,
        repo.open_issues_count,
        totalCommits,
        mergeCommits,
        repo.html_url
      ]);
    }

    page++;
  }
}
