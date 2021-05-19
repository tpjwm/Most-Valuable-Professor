# Most Valuable Professor
This was a semester long project for CS 411: Database Systems

This website is similar to rate my professor in the way that it displays useful information for students looking for courses

It differs in the way that it is backed strongly by [data](https://github.com/wadefagen/datasets/tree/master/gpa) produced by the university

# Details
Details about this project, including design, features, dataflow, and more, are located in the project report pdf in this repository

## Requirements
```
python >= 3.5
```

## Getting started
```bash
git clone https://github.com/tpjwm/Most-Valuable-Professor.git
cd Most-Valuable-Professor
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP = app
flask run
```

## Setting up GCP
Create a `app.yaml` file in the root folder with the following content:
```yaml
runtime: python38 # or another supported version

instance_class: F1

env_variables:
  MYSQL_USER: <user_name> # please put in your credentials
  MYSQL_PASSWORD: <user_pw> # please put in your credentials
  MYSQL_DB: <database_name> # please put in your credentials
  MYSQL_HOST: <database_ip> # please put in your credentials

handlers:
# Matches requests to /images/... to files in static/images/...
- url: /img
  static_dir: static/img

- url: /script
  static_dir: static/script

- url: /styles
  static_dir: static/styles
```

Setting up the deployment
```bash
curl https://sdk.cloud.google.com | bash
gcloud components install app-engine-python
gcloud config set project #PROJECT-NAME
gcloud auth login
gcloud app deploy
```
# Credits
* [Pratik](https://github.com/pratik139patel/Personal-Projects.git) - Backend, Database implementation
* [Michael](https://github.com/mharty2) - Backend, Database implementation
* [Dimitar](https://github.com/tpjwm) - Backend, Frontend
* [Omar](https://github.com/omarn33) - Frontend, Design
