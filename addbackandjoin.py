import pywikibot

# Define the site and page
site = pywikibot.Site('ar', 'wikisource')
page = pywikibot.Page(site, 'مستخدم:Akbarali/Tests/arsource')

# Fetch the page content
text = page.text

# Split the text into lines
lines = text.splitlines()

# Process the lines to add "\\" at the end of odd lines and join even lines
new_lines = []
for i in range(0, len(lines), 2):
    if i + 1 < len(lines):
        new_lines.append(lines[i] + '\\\\ ' + lines[i + 1])
    else:
        new_lines.append(lines[i] + '\\\\')

# Join the lines back into a single string
new_text = '\n'.join(new_lines)

# Save the updated content back to the page
page.text = new_text
page.save(summary='Formatted lines with "\\\\" at the end of odd lines and joined even lines')
