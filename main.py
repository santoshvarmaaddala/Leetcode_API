from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

def get_user_details(username: str):
    query = {
        "query": """
        query userProfile($username: String!) {
            matchedUser(username: $username) {
                username
                profile {
                    realName
                    aboutMe
                    school
                    websites
                    countryName
                    company
                    ranking
                }
                submitStats {
                    acSubmissionNum {
                        difficulty
                        count
                        submissions
                    }
                }
            }
        }
        """,
        "variables": {"username": username}
    }
    response = requests.post(LEETCODE_GRAPHQL_URL, json=query)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from LeetCode")
    
    data = response.json()
    if "errors" in data:
        raise HTTPException(status_code=404, detail="User not found or access denied")
    
    return data["data"]["matchedUser"]

@app.get("/leetcode/{username}")
def read_user(username: str):
    try:
        user_details = get_user_details(username)
        return user_details
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/leetcode/{username}/rank")
def userGloabalRank(username: str):
    try:
        user_details = get_user_details(username)
        ranking = user_details["profile"]["ranking"]
        return {"username":username,"globalRanking":ranking}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
