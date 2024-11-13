import pywikibot

# Define the site and the page
site = pywikibot.Site('ar', 'wikisource')
page = pywikibot.Page(site, 'مستخدم:Akbarali/Tests')

# Current text of the page
text = page.text

# Split the text into individual lines
lines = text.splitlines()

# Create a new list to store the rearranged lines
new_lines = []

# Iterate over the lines in pairs
for i in range(0, len(lines), 2):
    if i + 1 < len(lines):
        # Add the first line with the "\\" at the end and the second line right after
        new_line = lines[i].strip() + "\\\\" + lines[i+1].strip()
        new_lines.append(new_line)
    else:
        # In case there's an odd number of lines, add the last line without pairing
        new_lines.append(lines[i].strip())

# Join the rearranged lines back into a single string
new_text = '\n'.join(new_lines)

# Save the new text to the page
page.text = new_text
page.save(summary="Rearranged poetry lines with '\\\\' formatting")
