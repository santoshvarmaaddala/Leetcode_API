﻿# LeetCode API with FastAPI

This project provides a FastAPI-based API to fetch user details from LeetCode, including their global ranking and total problems solved.

## Features

- Fetch LeetCode user profile details.
- Fetch the global ranking of a LeetCode user.
- Fetch the total number of problems solved by a LeetCode user, categorized by difficulty.

## Endpoints

### Get User Profile

- **URL**: `/leetcode/{username}`
- **Method**: `GET`
- **Description**: Fetches the complete profile details of a LeetCode user.
- **Response**:
  ```json
  {
      "username": "user123",
      "profile": {
          "realName": "User Name",
          "aboutMe": "About the user",
          "school": "User's School",
          "websites": ["website1", "website2"],
          "countryName": "Country",
          "company": "User's Company",
          "ranking": 12345
      },
      "submitStats": {
          "acSubmissionNum": [
              {
                  "difficulty": "All",
                  "count": 100,
                  "submissions": 150
              },
          ]
      }
  }

# Installation
### 1.Clone the repository:
```sh
git clone https://github.com/yourusername/leetcode-api.git
cd leetcode-api
```
### 2.Create a virtual environment and activate it:
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```
### 3.Install the dependencies:
```sh
pip install -r requirements.txt
```
### 4.Run the FastAPI app:
```sh
uvicorn main:app --reload
```
### 5.Access the API documentation at:
    http://localhost:8000/docs
    or
    http://localhost:8000/redoc

## Dependencies
    FastAPI
    requests
    uvicorn
## License
This project is licensed under the MIT License. See the LICENSE file for details.
