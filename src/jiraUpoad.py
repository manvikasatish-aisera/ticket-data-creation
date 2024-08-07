from jira import JIRA

def uploadJiraTicket(ticketInfo):
    #ticketInfo --> get all info needed for issue_dict from here
    
    # Replace with your Jira instance, username, and API token
    jira_options = {'server': 'https://your-jira-instance.atlassian.net'}
    jira = JIRA(options=jira_options, basic_auth=('your_username', 'your_api_token'))

    # Create a new issue
    issue_dict = {
        'project': {'key': 'PROJECT_KEY'},
        'summary': 'My first Jira issue',
        'description': 'This is the description of the issue',
        'issuetype': {'name': 'Bug'}
    }
    new_issue = jira.create_issue(fields=issue_dict)
    print('New issue created: {}'.format(new_issue))