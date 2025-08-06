import requests
import plotly.express as px

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

repo_links, stars, hover_texts = [],[],[]
for repo_dict in response_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f'<a href="{repo_url}">{repo_name}</a>'
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f'{owner}<br>{description}'
    hover_texts.append(hover_text)

title = 'Most Starred Python Repos on Github'
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, 
             y=stars, 
             hover_name=hover_texts,
             title=title,
             labels=labels)
# fig.update(title_font_size=28,
#            xaxis_title_font_size=20,
#            yaxis_title_font_size=20)
fig.show()