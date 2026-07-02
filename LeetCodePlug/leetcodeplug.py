import requests

def has_user_solved(username: str, problem_slug: str) -> bool:
    """
    Checks if a LeetCode user has successfully solved a specific problem.
    :param username: The LeetCode handle (e.g., "blank_user")
    :param problem_slug: The URL slug of the problem (e.g., "two-sum")
    """
    url = "https://leetcode.com/graphql/"
    
    query = """
    query recentSubmissionList($username: String!, $limit: Int!) {
        recentSubmissionList(username: $username, limit: $limit) {
            titleSlug
            statusDisplay
        }
    }
    """
    
    variables = {
        "username": username,
        "limit": 2000
    }
    
    try:
        #print(query)
        response = requests.post(url, json={"query": query, "variables": variables})
        response.raise_for_status()
        data = response.json()
        submissions = data.get("data", {}).get("recentSubmissionList", [])
        #print(submissions)
        if not submissions:
            #No recent submissions found or user '{name}' does not exist.
            return -1
        for sub in submissions:
            if sub["titleSlug"] == problem_slug and sub["statusDisplay"] == "Accepted":
                return 1
        return 0
    except requests.exceptions.RequestException as e:
        print(f"Network or API Error: {e}")
        return -2

