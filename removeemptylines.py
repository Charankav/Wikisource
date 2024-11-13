import pywikibot

# Define the site and page
site = pywikibot.Site('ar', 'wikisource')
page = pywikibot.Page(site, 'صفحة:Qaseedath Burda.pdf/3')

# Fetch the page content
text = page.text

# Remove empty lines
new_text = '\n'.join([line for line in text.splitlines() if line.strip()])

# Save the updated content back to the page
page.text = new_text
page.save(summary='Removed empty lines')
