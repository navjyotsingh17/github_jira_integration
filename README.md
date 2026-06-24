# Jira Issue Automation using Python REST API

## Overview

This project demonstrates how to create Jira issues programmatically using the **Jira REST API** and Python. It authenticates securely using API tokens stored in environment variables and submits issue details such as summary, description, environment, project, and issue type to a Jira Cloud instance.

The project is intended as a practical example of API automation and showcases how repetitive project management tasks can be automated using Python.

---

## Features

* Create Jira issues automatically using the Jira REST API
* Secure authentication with Jira API Token
* Environment variables for protecting sensitive credentials
* JSON payload construction using Jira's API schema
* Simple and lightweight Python implementation
* Easy to extend for workflow automation and DevOps integrations

---

## Technologies Used

* Python 3
* Requests Library
* python-dotenv
* Jira Cloud REST API
* JSON
* REST APIs

---

## Project Structure

```text
github_jira_integration/
│
├── main.py              # Main application
├── .env                 # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Prerequisites

Before running the project, ensure you have:

* Python 3.9 or later
* A Jira Cloud account
* Jira API Token
* Project Key
* Issue Type ID

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/github_jira_integration.git
cd github_jira_integration
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
EMAIL_ID=your-email@example.com
JIRA_API_TOKEN=your_jira_api_token
```

These credentials are loaded securely using the **python-dotenv** package.

---

## How It Works

1. Loads credentials from the `.env` file.
2. Authenticates with Jira Cloud using Basic Authentication.
3. Builds the issue payload in JSON format.
4. Sends an HTTP POST request to the Jira REST API.
5. Prints the API response, including the created issue key if successful.

---

## Sample Request Payload

```json
{
  "project": {
    "key": "KAN"
  },
  "issuetype": {
    "id": "10046"
  },
  "summary": "Main order flow broken",
  "description": "Order entry fails when selecting supplier.",
  "environment": "UAT"
}
```

---

## API Endpoint Used

```http
POST /rest/api/3/issue
```

This endpoint creates a new issue in the specified Jira project.

---

## Sample Output

```json
{
    "id": "10001",
    "key": "KAN-15",
    "self": "https://your-domain.atlassian.net/rest/api/3/issue/10001"
}
```

---

## Security

This project follows secure development practices by:

* Storing credentials in environment variables
* Keeping secrets outside the source code
* Excluding the `.env` file from version control using `.gitignore`

---

## Future Enhancements

This project can be extended to support:

* GitHub Webhook integration
* Automatic Jira ticket creation from GitHub Issues
* Pull Request notifications
* Slack or Microsoft Teams integration
* Docker containerization
* GitHub Actions CI/CD pipeline
* Error logging and retry mechanisms
* Unit and integration testing

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* REST API Integration
* Python Automation
* HTTP Authentication
* JSON Data Handling
* Environment Variable Management
* Secure API Development
* DevOps Automation Concepts

---

## Author

Developed as a hands-on automation project to demonstrate API integration skills, Python development, and DevOps automation practices using the Jira Cloud REST API.
