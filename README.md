# jogoteca-flask-python

Project to study Flask microframework Python

Flask version: 1.0.2

# How to test the aplication 

* Install the Flask :
    pip3 install flask==1.0.2

* Config the environments variables:

    For Linux and Mac:

        export FLASK_APP=jogoteca.py flask
        export FLASK_ENV=development
    
    For Windows cmd, use set instead of export:

        set FLASK_APP=jogoteca.py flask
        set FLASK_ENV=development

    For Windows PowerShell, use $env: instead of export:

        $env:FLASK_APP = "jogoteca.py flask"
        $env:FLASK_ENV = "development"

* Run the application:

    flask run

    By default, the flask application run in 5000 port. But if you want change this, execute the command:

    flask run --port=5555

############################################################

 * Serving Flask app "jogoteca.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 324-329-849
 * Running on http://127.0.0.1:5555/ (Press CTRL+C to quit)
 
 ############################################################
