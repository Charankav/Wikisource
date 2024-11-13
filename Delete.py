import pywikibot

def format_poetry(page_title):
    site = pywikibot.Site('ar', 'wikisource')
    page = pywikibot.Page(site, page_title)
    
    # Read the plain lines from the page
    text = page.text
    
    # Split the text into lines
    lines = text.split('\n')
    
    # Add \\ at the end of each odd line (1-based index), ignoring <noinclude> tags
    formatted_lines = []
    for i, line in enumerate(lines):
        if '<noinclude>' not in line and '</noinclude>' not in line:
            if i % 2 == 0:  # Odd lines (0-based index, so even index means odd line in 1-based)
                line += ' \\'
        formatted_lines.append(line)
    
    # Join the lines and wrap with the {{أبيات}} template
    formatted_text = '{{أبيات|\n' + '\n'.join(formatted_lines) + '\n}}'
    
    # Save the formatted text back to the page
    page.text = formatted_text
    page.save('Formatted poetry using {{أبيات}} template with line breaks on odd lines, excluding tags.')

# Replace 'Qaseedath Burda.pdf/9' with the title of the page you want to format
format_poetry('صفحة:Qaseedath Burda.pdf/9')
