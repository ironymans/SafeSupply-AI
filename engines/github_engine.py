import requests
from requests.help import info

def check_github_repo(repo_url):
    risks = []

    if not repo_url:
        return []

    try:
        # extract owner/repo from url
        parts = repo_url.replace("https://github.com/", "").split("/")
        owner = parts[0]
        repo = parts[1]

        api = f"https://api.github.com/repos/{owner}/{repo}"
        r = requests.get(api)
        data = r.json()

        stars = data.get("stargazers_count", 0)
        forks = data.get("forks_count", 0)
        issues = data.get("open_issues_count", 0)

        # ---- Risk rules ----
        if stars < 10:
            risks.append("Very low GitHub stars")

        if forks < 5:
            risks.append("Very low forks count")

        if issues > 50:
            risks.append("Too many open issues")

        return risks

    except:
        return {
    "author": info.get("author"),
    "version": info.get("version"),
    "releases": len(data.get("releases", {})),
    "github": info.get("project_urls", {}).get("Source")
}