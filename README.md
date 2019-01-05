![simplinnovation](https://4.bp.blogspot.com/-f7YxPyqHAzY/WJ6VnkvE0SI/AAAAAAAADTQ/0tDQPTrVrtMAFT-q-1-3ktUQT5Il9FGdQCLcB/s350/simpLINnovation1a.png)

# Basic CRUD: Flask & MySQL

1. Activate __MongoDB__ server:
    
    ```bash
    $ cd C:\Program Files\MongoDB\Server\3.6\bin
    $ mongod
    ```
    
    Open new terminal & type again:
    
    ```bash
    $ cd C:\Program Files\MongoDB\Server\3.6\bin
    $ mongo
    ```

    __[OPTIONAL]__ You can create a database & collection first, or let our Flask application do this later. If you wanna create db & col first, do these on Mongo:

    ```bash
    > use lin_flask
    > db.createUser({user:'lintang', pwd:'1234', roles:['readWrite', 'dbAdmin']})
    > db.createCollection('users')
    ```

#

2. Clone this repo. Insert your __database URI__ to database.yaml file, then install all the packages needed. In this project I'm using __flask__, __flask_cors__ & __pymongo__:
    ```bash
    $ git clone https://github.com/LintangWisesa/CRUD_Flask_MongoDB.git
    $ cd CRUD_Flask_MongoDB
    $ pip install flask flask_cors pymongo
    ```

#

3. Run the server file. Make sure your MongoDB server is still running. Your application server will run locally at __*http://localhost:5000/*__ :
    ```bash
    $ python app.py
    ```

#

4. Give a request to the server. You can use __Postman__ app:
    
    __See the opening screen (*home.html*)__
    ```bash
    GET /
    ```

    __Post a data to database:__ 
    ```bash
    POST /data
    body request: {name:"x", age:"y"}
    ```
    __Get all data & specific data by MongoDB ObjectId:__
    ```bash
    GET /data
    GET /data/{:id}
    ```
    __Update a data by MongoDB ObjectId__:
    ```bash
    PUT /data/{:id}
    body request: {name:"x", age:"y"}
    ```
    __Delete a data by MongoDB ObjectId:__
    ```bash
    DELETE /data/{:id}
    ```

#

6. Enjoy your code! 😎👌

## See also:

- [Basic CRUD: Flask & MySQL](https://github.com/LintangWisesa/CRUD_Flask_MySQL)
- [Basic CRUD: Flask & PostgreSQL](https://github.com/LintangWisesa/CRUD_Flask_PostgreSQL)
- [Basic CRUD: Flask & MongoDB](https://github.com/LintangWisesa/CRUD_Flask_MongoDB)

#

#### Lintang Wisesa :love_letter: _lintangwisesa@ymail.com_

[Facebook](https://www.facebook.com/lintangbagus) | 
[Twitter](https://twitter.com/Lintang_Wisesa) |
[Google+](https://plus.google.com/u/0/+LintangWisesa1) |
[Youtube](https://www.youtube.com/user/lintangbagus) | 
:octocat: [GitHub](https://github.com/LintangWisesa) |
[Hackster](https://www.hackster.io/lintangwisesa)