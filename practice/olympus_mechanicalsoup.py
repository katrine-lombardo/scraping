import mechanicalsoup

# Create a browser instance to request URL
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)

# Inspect the .soup attribute to view HTML
login_html = login_page.soup

# Return a lost of all form elements on the page and set input values
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# Submit the form
profiles_page = browser.submit(form, login_page.url)

# Programmatically obtain the URL for each link on the /profiles page
base_url = "http://olympus.realpython.org"
links = profiles_page.soup.select("a")
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")

# Display the title of the current page to determine that you’ve been redirected
# to the /profiles page
print(profiles_page.soup.title)
