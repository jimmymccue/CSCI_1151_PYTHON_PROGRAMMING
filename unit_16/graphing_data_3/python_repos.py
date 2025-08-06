import requests

url='https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
response = requests.get(url, headers=headers)
print(f'Staus Code: {response.status_code}')
response_dict = response.json()

# print(response_dict.keys())

print(f'Total Repo: {response_dict['total_count']} ')
print(f'Complete reults: {not response_dict['incomplete_results']}')

response_dicts = response_dict['items']
print(f'Repositories returned: {len(response_dict)}')

for repo_dict in response_dicts:
    print(f'\nName: {repo_dict['name']}')
    print(f'\nOwner: {repo_dict['owner']['login']}')
    print(f'\nStars: {repo_dict['stargazers_count']}')
    print(f'\nRepository: {repo_dict['html_url']}')
    print(f'Description: {repo_dict['description']}')