import pywikibot

# Define the site and page
site = pywikibot.Site('ar', 'wikisource')
page = pywikibot.Page(site, 'مستخدم:Akbarali/Tests/arsource')

# Fetch the page content
text = page.text

# Split the text into lines
lines = text.splitlines()

# Add the template markers
if lines:
    lines[0] = '{{أبيات|' + lines[0]
    lines[-1] = lines[-1] + '}}'

# Join the lines back into a single string
new_text = '\n'.join(lines)

# Save the updated content back to the page
page.text = new_text
page.save(summary='Added template markers to the first and last lines')
