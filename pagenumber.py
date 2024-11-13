import pywikibot

# Set the site to Malayalam Wikisource
site = pywikibot.Site('ml', 'wikisource')

# Loop through pages 16 to 30
for i in range(16, 31):
    # Set the correct page title
    page_title = f'താൾ:സുവിശേഷം-ഭാഷാഗാനം.pdf/{i}'
    page = pywikibot.Page(site, page_title)

    # Set the content as the incrementing page number (starting from 12)
    page_number = i - 4  # This will give 12 for page 16
    content = f'<div style="text-align: center;">{page_number}</div>'

    # Check if the page exists
    if page.exists():
        # If the page exists, add content at the top
        new_content = content + "\n" + page.text
        page.text = new_content
        page.save(f"Added page number {page_number} at the top center")
    else:
        # If the page does not exist, create it with the content
        page.text = content
        page.save(f"Created page and added page number {page_number} at the top center")
        print(f"Page '{page_title}' was created.")
