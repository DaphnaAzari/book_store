from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

def test_book_list_contains_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

# passing in a playwrite object: (page: Page)
def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    # we need to store an h1 tag variable:
    h1 = page.locator("h1")
    expect(h1).to_contain_text("Daphna's Book Store")

#Playwright gives my test function a page object automatically
# this represents a browser tab that Playwright controls for us
def test_correct_list_of_books(page: Page):
    # tells the browser to visit that URL 
    # This is why Flask server needs to run separately
    # Playwright doesn't run the app for us
    # it just visits it like a real user would 
    # If nothing is running on port 5001 this line fails immediately
    page.goto("http://127.0.0.1:5001/books")
    # we need to store an h1 tag variable:
    # books = page.locator("li")
    expected_books = [
      'The Gruffalo by Julia Donaldson released in 23/03/1999',
      'Ada Twist, Scientist by Andrea Beaty released in 6/09/2016',
      'The Girl Who Drank the Moon by Kelly Barnhill released in 9/08/2016',
      'Dragons in a Bag by Zetta Elliott released in 23/10/2018'
    ]
    #this line just calls an all_inner_text method, 
    # Which will always fetch the current state of the page of book (defines online 20)
    # actual_books = books.all_inner_texts()

    #compares the two lists:
    # assert actual_books == expected_books
    #instead changed to this so I don't need to keep up adding books every time!:
    # Books displayed on the webpage

    #this grabs all the books:
    actual_books = page.locator("li").all_inner_texts()


    # Get books from the database
    

    assert expected_books[0] in actual_books
    assert expected_books[1] in actual_books
    assert expected_books[2] in actual_books
    assert expected_books[3] in actual_books



def test_add_new_book(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    all_h2 = page.locator("h2").all()
    # second_h2 =page.locator("h2").nth(1)
    expect(all_h2[0]).to_contain_text("Books")
    expect(all_h2[1]).to_contain_text("Add Books:")
    # expect(second_h2).to_contain_text("Add Books:")
    books = page.locator('li')
    # expected_books = [
    #   'The Gruffalo by Julia Donaldson released in 23/03/1999',
    #   'Ada Twist, Scientist by Andrea Beaty',
    #   'The Girl Who Drank the Moon by Kelly Barnhill',
    #   'Dragons in a Bag by Zetta Elliott'
    # ]
    page.get_by_placeholder("Title").fill("Lost and Found")
    page.get_by_placeholder("Author").fill("Oliver Jeffers")
    page.get_by_placeholder("Release date").fill("05/09/2005")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]
    assert new_book == "Lost and Found by Oliver Jeffers released in 05/09/2005"



