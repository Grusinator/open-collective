import os
from invoke import task
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

RESOURCE_GROUP = os.getenv("RESOURCE_GROUP")
LOCATION = os.getenv("LOCATION", "westeurope")
STORAGE_ACCOUNT = os.getenv("STORAGE_ACCOUNT")
APP_SERVICE_PLAN = os.getenv("APP_SERVICE_PLAN")
WEB_APP = os.getenv("WEB_APP")
DJANGO_SETTINGS_MODULE = os.getenv("DJANGO_SETTINGS_MODULE")
SECRET_KEY = os.getenv("SECRET_KEY")
     
@task
def deploy(c):
    c.run(f"az group create --name {RESOURCE_GROUP} --location {LOCATION}")
    c.run(f"az storage account create --name {STORAGE_ACCOUNT} --location {LOCATION} --resource-group {RESOURCE_GROUP} --sku Standard_LRS")
    c.run(f"az appservice plan create --name {APP_SERVICE_PLAN} --resource-group {RESOURCE_GROUP} --sku F1 --is-linux")
    result = c.run(f'az webapp create --resource-group {RESOURCE_GROUP} --plan {APP_SERVICE_PLAN} --name {WEB_APP} --runtime "PYTHON|3.9" --deployment-local-git', hide=True)
    git_url = result.stdout.strip().split()[-1]
    c.run(f'az webapp config set --resource-group {RESOURCE_GROUP} --name {WEB_APP} --startup-file "gunicorn --bind=0.0.0.0 --timeout 600 {DJANGO_SETTINGS_MODULE}.wsgi:application"')
    c.run(f"az webapp config appsettings set --resource-group {RESOURCE_GROUP} --name {WEB_APP} --settings SECRET_KEY='{SECRET_KEY}' DJANGO_SETTINGS_MODULE='{DJANGO_SETTINGS_MODULE}'")
    c.run(f"git remote add azure {git_url}")
    c.run("git add .")
    c.run('git commit -m "Deploy code"')
    c.run("git push azure main")
