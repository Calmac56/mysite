import os, django, requests, json
from datetime import datetime
from dateutil.parser import parse

from pprint import pprint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from mysiteapp.models import Projects, Language

# creates a requests session
def connect_github():
    try:
        with open('github.key') as f:
            github_token = f.read().strip()
    except:
        print("github.key not found")
        exit(0)

    session = requests.session()
    session.auth = ('Calmac56', github_token)
    return session

# gathers a dictionary containing all the repos
def get_repositories(session):
    return json.loads(session.get("https://api.github.com/user/repos").content)

# gathers all the projects and returns a dictionary
def get_projects(repos, session):
    theprojects = {}
    for repo in repos:
        if not repo['private'] and repo['owner']['id'] == 60009981:
            theprojects[repo['id']] = {
                'name' : repo['name'],
                'desc' : repo['description'],
                'url' : repo['html_url'],
                'date_c' : parse(repo['created_at']),
                'date_u' : parse(repo['updated_at']),
                'main_lang' : repo['language'],
                'langs' : json.loads(session.get(repo['languages_url']).content), # language:size(bytes)
                'stars' : int(repo['stargazers_count']),
                'watchers' : int(repo['watchers_count'])
            }
            print(theprojects)
    return theprojects

# cleans DB of projects which have been removed from the repoistory
def clean_projects(theprojects):
    db_projects = Projects.objects.all()
    for project in db_projects:
        if not int(project.projid) in theprojects:
            print(project)
            project.delete()

# gathers all languages used and returns a set
def get_languages(theprojects):
    languages = set()
    for project in theprojects:
        for lang in theprojects[project]['langs']:
            languages.add(lang)
    return languages

# adds langauges to the database
def add_languages(languages):
    for language in languages:
        Language.objects.get_or_create(name = language)[0].save()
        print(f"-- Added {language}")

# adds projects to the database (edits them if they already exist)
def add_projects(theprojects):
    for project in theprojects:
        if theprojects[project]['main_lang']:
            if theprojects[project]['main_lang'].lower() in ('css'):
                theprojects[project]['main_lang'] = "HTML"

        if not theprojects[project]['desc']:
            theprojects[project]['desc'] = "No description."

        language = Language.objects.get_or_create(name = theprojects[project]['main_lang'])[0]

        project_obj = Projects.objects.get_or_create(projid = str(project))[0]
        project_obj.name = theprojects[project]['name']
        project_obj.info = theprojects[project]['desc']
        project_obj.url = theprojects[project]['url']
        project_obj.datecreated = theprojects[project]['date_c']
        project_obj.lastmodified = theprojects[project]['date_u']
        project_obj.language = language
    
        project_obj.save()

        print(f"-- Added {theprojects[project]['name']}")

# populates the database by running the two methods above
def populate(languages, theprojects):
    print("- Adding Languages to DB")
    add_languages(languages)
    print("- Finished Adding Languages")
    print("- Adding Projects to DB")
    add_projects(theprojects)
    print("- Finished Adding Projects")

# main method running all the code
def main():
    print("Starting script...")
    session = connect_github()
    repos = get_repositories(session)
    theprojects = get_projects(repos, session)
    print("- Removing Deleted Projects")
    clean_projects(theprojects)
    print("- Finsihed Removing Deleted Projects")
    languages = get_languages(theprojects)
    populate(languages, theprojects)
    print("Script finished.")

if __name__ == '__main__':
   main()