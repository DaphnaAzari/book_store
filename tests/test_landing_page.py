from playwright.sync_api import Page, expect

# passing in a playwrite object: (page: Page)
def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/")
    # we need to store an h1 tag variable:
    h1 = page.locator("h1")
    expect(h1).to_have_text("Welcome to AceReads")
