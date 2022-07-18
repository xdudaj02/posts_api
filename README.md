# Posts API
API for managing posts.

### Steps for setting up the project:
First clone the repository and then navigate inside it.
```shell
git clone https://github.com/xdudaj02/posts_api.git
cd posts_api
```

Then you need to install all the dependencies. Setting up a virtual 
environment beforehand is recommended.
```shell
pip install -r requirements.txt
```

Then you need to set up a database. The project uses a *sqlite3* database 
by default. If you wish to use a different database engine you can enter 
your database settings in the *settings.py* file by editing the `DATABASES` 
variable before running the following command.
```shell
python manage.py migrate
```

At last, you can start the development server.
```shell
python manage.py runserver 
```
