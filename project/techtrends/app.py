import sqlite3

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
import logging
from werkzeug.exceptions import abort
dbCount=0
# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    count_dbConnection()
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()

    connection.close()
    return post

# Function to get title of a post using its ID
def get_title(post_id):
    connection = get_db_connection()
    title = connection.execute('SELECT title FROM posts WHERE id = ?',
                              (post_id,)).fetchone()
    connection.close()
    return title[0]

#Function to count posts
def count_posts():
    connection = get_db_connection()
    postcount=connection.execute('SELECT count(*) FROM posts').fetchone()

    connection.close()
    return postcount[0]

# Define the Flask application

# Count active db connections
def count_dbConnection():
    dbCounts=+1
    return dbCounts

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        ## log line
        app.logger.info('Sorry this Article does not exist please choose an other one!')
        return render_template('404.html'), 404
    else:
        ## log line
        title =get_title(post_id)
        app.logger.info('Main request successfull Article:  %s retrieved!', title)
        return render_template('post.html', post=post)


# Define the About Us page
@app.route('/about')
def about():
    ## log line
    app.logger.info('About US page is retreived!')
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()
            ## log line
            app.logger.info('New Article:  %s hsd been created!', title)
            return redirect(url_for('index'))

    return render_template('create.html')
# add healthz endpoint that shell return following two information
# http 200 status code
# json response containing result:ok - healthy message
@app.route('/healthz')
def healthz():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    return response
# add metrics endpoint that returns the number of db_connections, and post_count
@app.route('/metrics')
def metrics():
    dbcounts=count_dbConnection()
    print(dbcounts)
    postcounts=count_posts()
    #automatisere das zaehlen db conenction und post count
    response = app.response_class(
        response=json.dumps({"db_connection_count":dbcounts, "post_count":postcounts}),
        status=200,
        mimetype='application/json'
    )
    return response
# start the application on port 3111
if __name__ == "__main__":
   ## stream logs to app.log file
   logging.basicConfig( format = '%(levelname)-8s %(asctime)s %(message)s',
                        level = logging.DEBUG,
                        datefmt = '%Y-%m-%d %H:%M:%S')

   app.run(host='0.0.0.0', port='3111')
