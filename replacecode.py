import pywikibot

site = pywikibot.Site('ml', 'wikipedia')  # Malayalam Wikipedia
site.login()

# Read page titles from replace.txt
with open('replace.txt', 'r', encoding='utf-8') as file:
    page_titles = file.read().splitlines()

# Search and replace for each page title
search_term = 'മുസ്ലിം'
replace_term = 'മുസ്‌ലിം'

for title in page_titles:
    page = pywikibot.Page(site, title)
    page_text = page.text
    updated_text = page_text.replace(search_term, replace_term)

    # Edit the page with the updated text
    page.text = updated_text
    page.save(summary='അക്ഷരപിശക് ശരിയാക്കൽ')
