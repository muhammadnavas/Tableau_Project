# 📊 GitHub Repository Data Visualization Using Tableau

## ✅ **Aim**
To fetch live GitHub repository data using the GitHub API, prepare it in Google Sheets, and visualize it in Tableau through KPIs, dashboards, and stories, demonstrating real-time data handling and interactive visualization.


## 📌 **Objectives**
1. Generate a GitHub personal access token and use it to collect live repository data.
2. Pull the data into Google Sheets using Apps Script.
3. Set up triggers that automatically update data at regular intervals.
4. Connect Google Sheets with Tableau Public.
5. Build KPI cards, charts, and graphs from the dataset.
6. Design a dashboard with interactive filters and comparative analysis.
7. Create a story summarizing the findings and insights from repository activity.


## 🛠 **Tools Used**
- **GitHub API** – for fetching real-time repository data (stars, forks, watchers, open issues, commits, merge commits).
- **Google Sheets with Apps Script** – for storing, refreshing, and managing data dynamically.
- **Tableau Public** – for visualization, dashboards, and storytelling.


## 📋 **Steps**

### **Step 1 – Generate API Token and Fetch Repository Data**
- Registered on GitHub and created a personal access token for API access.
- Built API requests to fetch repository information for the user `muhammadnavas`.
- Retrieved data like stars, forks, watchers, open issues, total commits, and merge commits.
- Handled API pagination to ensure all repositories and commits are fetched.

### **Step 2 – Store Data in Google Sheets**
- Created a new Google Sheet and opened Apps Script editor.
- Wrote a script to fetch repository data from GitHub and append it to the sheet.
- Structured the sheet with headers like:
  - Repo Name
  - Language
  - Stars
  - Forks
  - Watchers
  - Open Issues
  - Total Commits
  - Merge Commits
  - URL

### **Step 3 – Set Up Trigger for Automatic Updates**
- Configured a time-driven trigger in Apps Script to run the data fetching function periodically (e.g., daily).
- Ensured the sheet is cleared and repopulated with the latest data during each run.
- This setup ensures real-time updates without manual intervention.

### **Step 4 – Connect Google Sheets to Tableau**
- Opened Tableau Public and connected to the Google Sheets data source.
- Selected the `GitHubData` sheet and confirmed data import with correct column types.

### **Step 5 – Create KPI Cards and Charts**
- Created KPI cards to show total stars, forks, watchers, open issues, and commits across repositories.
- Designed bar charts to compare commits and merge commits among repositories.
- Used filters to segment repositories by language or contribution activity.

### **Step 6 – Build Dashboard**
- Arranged KPIs, charts, and graphs in a user-friendly layout.
- Integrated interactive filters to allow users to analyse data by repository or activity metrics.

### **Step 7 – Create Story**
- Added story points to explain insights such as:
  - The most active repositories by stars and commits.
  - Trends in contribution and merge activity.
  - Comparisons between different programming languages or projects.

### **Step 8 – Publish to Tableau Public**
- Saved the completed dashboard and story to Tableau Public.
- Generated a public link to share with peers and instructors.
- Submitted the link as part of the project report.


## 🔗 **URL Link**
[View the project on Tableau Public](https://public.tableau.com/app/profile/muhammad.navas/viz/shared/DRYDJG257)
