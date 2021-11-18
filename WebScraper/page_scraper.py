from io import StringIO
from bs4 import BeautifulSoup

def get_page_data(soup, url):
    '''Scrape the transcript data for a given lecture video and write its content to data.txt'''

    timestamps = []
    timestamp_btns = soup.find_all('button', class_='timestamp')

    for timestamp in timestamp_btns:
        timestamps.append(timestamp.find(text=True, recursive=False))

    paragraphs = []

    phrases = soup.find_all('div', class_='phrases')

    for phrase in phrases:
        text = ''
        for sentence in phrase.select('span.cds-143.css-v4ktz5.cds-145'):
            text += sentence.get_text(strip=True) + ' '
        paragraphs.append(text)

    # print(len(timestamps) == len(paragraphs))  # Should be equal

    '''data.txt consists of lines in the format: paragraph##timestamp##url (where ## is the delimeter)'''
    with open('data.txt', 'a') as df:
        for i in range(len(timestamps)):
            df.write(paragraphs[i] + '##' + timestamps[i] + '##' + url.strip())
            df.write('\n')