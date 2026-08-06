from playwright.sync_api import Page, expect

# passing in a playwrite object: (page: Page)
def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    # we need to store an h1 tag variable:
    h1 = page.locator("h1")
    expect(h1).to_have_text("Daphna's Books")

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
    books = page.locator("li")
    expected_books = [
      'The Gruffalo by Julia Donaldson',
      'Ada Twist, Scientist by Andrea Beaty',
      'The Girl Who Drank the Moon by Kelly Barnhill',
      'Dragons in a Bag by Zetta Elliott'
    ]
    #this line just calls an all_inner_text method, 
    # Which will always fetch the current state of the page of book (defines online 20)
    actual_books = books.all_inner_texts()
    #compares the two lists:
    assert actual_books == expected_books