# programme-reporting-prototype
Media Suite Intern Project Summer 2018/19


## Developer Set-up

### Versions of Tools and Frameworks
1. Python 3.6
2. Postgres 9.5
3. Node 10.13.0
4. Docker (if deploying)
   
### Install Python and Db
1. Pull this project down from github
```bash
git clone https://github.com/mediasuitenz/programme-reporting-prototype.git
```

2. Create a virtual env. Recommended to use PyEnv and PipEnv see https://mediasuite.atlassian.net/wiki/spaces/SUITE/pages/319750201/Python+Guidelines
```bash
pipenv install
pipenv shell # activate this project's virtualenv
```

3. Create a database

Install postgres, for example using https://postgresapp.com/.

Create a database for the project. Create a user and give it all privileges on the database.

4. Create local copy of `.env`
```
cd .. && cp .env-example .env
```
And then update with relevant variables.

5. Setup database - this will drop/create schema, add tables, and run migrations
```
cd server/
python manage.py migrate
python manage.py createsuperuser
python manage.py create_roles
```

6. Populate database - this will seed the database with example data defined in the fixtures directory (risk_category is a lookup table and must be loaded first)
```
python manage.py loaddata risk_category.json
python manage.py loaddata student_first.json
python manage.py loaddata demo_data.json
```

NOTE: To update the fixture data with what is currently in the database use a command similar to:
```
python manage.py dumpdata | python -m json.tool > programmes/fixtures/demo_data.json
```

7. Install ember dependencies
```
cd ../client
npm install
```   

8. Install selenium chromedriver
```
cd ..
brew cask install chromedriver
``` 

**Launch backend!**
```
cd server
python manage.py runserver
```

**Launch frontend!**
```
cd ..
cd client
ember s
```

**Deployment**

1. Build the client -> Navigate to the client directory and run:
```
ember build --env=production
```

2. Create local copy of `.env`
```
cd .. && cp .env-example .env
```
And then update with relevant variables
Note: PG_HOST should be 'host.docker.internal' or the docker container wont be able to communicate with the psql DB

3. Build the Docker image:
```
docker build .
```

5. Run the docker off the created image and add the .env file to the container environment:
```
docker run -ti --env-file=.env -p 80:80 <image_id>
```
(defaulting to port 80)
