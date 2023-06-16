import requests
from bs4 import BeautifulSoup
import csv
uf = 'https://www.gumtree.com.au/s-office-chairs/page-{}/c21006'
#records = []
records = []
for x in range(1,50):
    fomatted_url = uf.format(x)
    #url = ('https://www.gumtree.com.au/s-office-chairs/page-4/c21006')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    # make the request and get the HTML content
    response = requests.get(fomatted_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(response)
    div_tags = soup.find('div', class_='user-ad-collection-new-design')
    second_div_tag = div_tags.next_sibling

    if second_div_tag is None:
        #print('1')
        tables = div_tags.find('div', {'class': 'user-ad-collection-new-design__wrapper--row'})
        a_tags = tables.find_all('a')
        for x in a_tags:
            # tag for price, location and posted date
            key_details = x.find('div', {'class': 'user-ad-row-new-design__main-content'})
            title = key_details.find('p', {'class': 'user-ad-row-new-design__title'})
            desc = key_details.find('div')
            desconly = desc.find('p')

            prl = x.find('div', {'class': "user-ad-row-new-design__right-content"})
            price = prl.find('span')
            loc = prl.find('div', {'class': 'user-ad-row-new-design__location'})
            posted = prl.find('p')
            print(title.text,price.text,loc.text,posted.text)
            az = x.get('href')
            base='https://www.gumtree.com.au'
            final=base + az
            data = title.text,price.text, loc.text, posted.text, final
            records.append(data)
            '''with open('ssd_data2.csv', 'w', newline='',encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Title', 'Price', 'Location', 'Date'])  # Write column headers
                writer.writerows(records)'''


    else:
        tables = second_div_tag.find('div', {'class': 'user-ad-collection-new-design__wrapper--row'})
        a_tags = tables.find_all('a')

        for x in a_tags:
            # tag for price, location and posted date
            key_details = x.find('div', {'class': 'user-ad-row-new-design__main-content'})
            title = key_details.find('p', {'class': 'user-ad-row-new-design__title'})
            desc = key_details.find('div')
            desconly = desc.find('p')

            prl = x.find('div', {'class': "user-ad-row-new-design__right-content"})
            price = prl.find('span')
            loc = prl.find('div', {'class': 'user-ad-row-new-design__location'})
            posted = prl.find('p')
            # print(price.text,loc.text,posted.text)
            az = x.get('href')
            base='https://www.gumtree.com.au'
            final=base + az
            print(title.text, price.text, loc.text, posted.text)
            #print(title.text, price.text, loc.text, posted.text)
            data = title.text,price.text, loc.text, posted.text, final
            records.append(data)
            #print(records,'^^^^^')
            """with open('gt_test.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Title', 'company', 'location', 'postdate', 'extractdate', 'summary', 'joburl'])
                writer.writerows(records)"""
with open('ssd_data11.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Price', 'Location', 'Date', 'URL'])  # Write column headers
    writer.writerows(records)
