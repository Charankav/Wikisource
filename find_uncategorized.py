import pywikibot

def find_uncategorized_pages(limit=100):
    site = pywikibot.Site('ml', 'wikipedia')  # Malayalam Wikipedia

    # Get a generator for the first 'limit' pages in the main namespace
    gen = site.allpages(namespace=0, total=limit)

    uncategorized_pages = []

    for page in gen:
        # Check if the page has no categories
        if not page.categories():
            uncategorized_pages.append(page)

    return uncategorized_pages

def main():
    # Set the limit to 100 pages
    limit = 100

    uncategorized_pages = find_uncategorized_pages(limit)

    if uncategorized_pages:
        print(f"Uncategorized Pages (limit {limit}):")
        for page in uncategorized_pages:
            print(f"- {page.title()}")
    else:
        print("No uncategorized pages found.")

if __name__ == "__main__":
    main()
