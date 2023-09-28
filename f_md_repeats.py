# Mantresh at github.com/mantreshkhurana authored the Markdown parser used here.
from markdown_worker import MarkdownParser

def md_repeats(file_location):
    """Returns a list of repeated words within an .md file. Shows how many times each individual word has been mentioned."""

    # Parsing an .md file into a string.
    parser = MarkdownParser(file_location)
    heading_to_search = 'Heading'
    result = parser.search_heading(heading_to_search)

    # Primitive way of separating individual words from different punctuation marks.
    result_1 = result.replace(',','')
    result_2 = result_1.replace('.','')
    result_3 = result_2.replace('-','')
    result_4 = result_3.replace('(','')
    result_5 = result_4.replace(')','')
    result_6 = result_5.replace('?','')
    result_7 = result_6.replace('!','')
    result_8 = result_7.replace(':','')
    result_9 = result_8.replace(';','')

    # Transforming a long string into a list with every new word forming a new list item.
    words = result_9.split()
    words_lwr = []

    # Every words being rewritten in lower case as checking for repeated elements in Python lists is case-sensitive.
    for x in words:
        words_lwr.append(x.lower())

    repeated_words = ['']
    for word in words_lwr:
        count = words_lwr.count(word)
        if count >= 2:
            repeated_words.append(f"{word} - {count}")
            while word in words_lwr:
                words_lwr.remove(word)
                                    
    repeated_words_sort = sorted(repeated_words, key=len)
    repeated_words_final = list(reversed(repeated_words_sort))
    return repeated_words_final