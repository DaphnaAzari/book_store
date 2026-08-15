from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

def login(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_placeholder("username").fill("test")
    page.get_by_placeholder("password").fill("1234")
    page.get_by_role("button").click()

def failed_login(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_placeholder("username").fill("test")
    page.get_by_placeholder("password").fill("12345")
    page.get_by_role("button").click()