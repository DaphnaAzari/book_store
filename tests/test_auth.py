from app import app
from database_connection import DatabaseConnection
from playwright.sync_api import Page
from login_helper import login , failed_login

# This file is testing login, when hitting sessions endpoint with valid credentials client is redirected to books. 

def test_auth_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    response = client.post('/sessions', data={
        'username': 'test',
        'password': '1234'
    })

    assert response.status_code == 302
    # this assertion might be new to you :)
    assert response.headers['Location'].endswith('/books')

def test_fail_auth_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    response = client.post('/sessions', data={
        'username': 'test',
        'password': '12345'
    })

    assert response.status_code == 302
    # this assertion might be new to you :)
    assert response.headers['Location'].endswith('/sessions/new')

def test_auth_playwright(page: Page):
    login(page)
    assert page.url == "http://localhost:5001/books"

def test_failed_auth_playwright(page: Page):
    failed_login(page)
    assert page.url == "http://localhost:5001/sessions/new"