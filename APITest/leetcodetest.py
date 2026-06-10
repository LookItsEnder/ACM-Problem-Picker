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
        response = requests.post(url, json={"query": query, "variables": variables})
        response.raise_for_status()
        data = response.json()
        submissions = data.get("data", {}).get("recentSubmissionList", [])
        #print(submissions)
        if not submissions:
            print(f"No recent submissions found or user '{username}' does not exist.")
            return False
        for sub in submissions:
            if sub["titleSlug"] == problem_slug and sub["statusDisplay"] == "Accepted":
                return True
        return False
    except requests.exceptions.RequestException as e:
        print(f"Network or API Error: {e}")
        return False

# --- Example Usage ---
# user = "Look_Its_Ender"          # Replace with target username
# problem = "two-sum"         # Replace with target problem slug
# solved = has_user_solved(user, problem)

# if solved:
#     print(f"{user} has solved '{problem}' recently!")
# else:
#     print(f"{user} has not solved '{problem}' yet!")