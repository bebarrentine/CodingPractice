# Final Capstone Project

# Things to be sure to include in this project in addition to the basics:

# 1. Data structures
# 2. Classes
# 3. Functions (COMPLETE)
# 4. Decorators
# 5. Generators
# 6. Advanced modules (COMPLETE)
# 7. Web scraping (COMPLETE)
# 8. Images
# 9. Handling of PDFs or CSV files
# 10. Emails
# 11. GUIs

import requests
import bs4
import re

# I'm utilizing the SEC EDGAR database for this project.
# Here is an excellent resource that is guiding me through this: https://www.codeproject.com/Articles/1227268/Accessing-Financial-Reports-in-the-EDGAR-Database

company = input('Enter the name of the company: ')
def find_cik(company):
    result = requests.get('https://www.sec.gov/edgar/searchedgar/cik.htm').text
    ciksoup = bs4.BeautifulSoup(result, 'html.parser')

    # now use requests.post to find a CIK for any company. Reference https://stackoverflow.com/questions/23001678/python-beautiful-soup-form-input-parsing/32074666 for help.

    cik_action = ciksoup.find('form', action='/cgi-bin/cik_lookup').get('action')
    cik_search_url = 'https://www.sec.gov' + cik_action
    cik_dict = {a['name']: a.get('value', '') for a in ciksoup.find_all('input', {'name': True})}
    print(cik_search_url)
    print(cik_dict)
    cik_dict['company'] = company
    print(cik_dict)

    result2 = requests.post(cik_search_url, data=cik_dict).text
    company_cik_soup = bs4.BeautifulSoup(result2, 'html.parser')
    #alist = company_cik_soup.find_all('a')
    #print(alist)
    company_and_cik_list = [result2.split('\n')[i] for i in range(len(result2.split('\n')) - 1) if
                            result2.split('\n')[i].split()[0] == '<a']
    # for i in range(len(result2.split('\n'))):
    #   if result2.split('\n')[i].split()[0] == '<a'
    #      companylist.append(result2.split(''))
    print(result2.split('\n'))
    print(len(result2.split('\n')))
    print(result2.split('\n')[0].split()[0])
    print(company_and_cik_list)
    companylist = [element.split('   ')[1] for element in company_and_cik_list]
    print(companylist)

    #x = input('Enter the name of the company: ')
    # y = input('How many search results would you like to yield? (maximum of 100): ')

    n = 0
    for i, element in enumerate(companylist):
        if company.upper() in companylist[i]:
            n += 1
            print(str(i) + ' ' + companylist[i])

    if n == 0:
        print('There were no matches for your search.')
    elif n > 0:
        y = int(input('\nPlease enter the number associated with the company of your inquiry: '))
        print(company_and_cik_list)
        pattern = r'\d{10}'
        cik = str(re.search(pattern, company_and_cik_list[y]).group())
        print(cik)
        return cik

cik = find_cik(company)
print(cik)
# reference url: 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001065088&type=10-K&dateb=20160101&count=10'
form_type = input('Enter the form you would like to obtain information about: ')
year = int(input('Enter the year: '))
def get_links(cik, type, year):
    #print(find_cik)
    EdgarStr = requests.get(f'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type={type}&dateb={year + 1}0101&count=10').text
    soup = bs4.BeautifulSoup(EdgarStr, 'html.parser')

    taglist = soup.find_all('a', id='documentsbutton')
    linklist = ['https://www.sec.gov' + tag['href'] for tag in taglist]
    return linklist

def get_htm():
    docstrings = [requests.get(get_links(cik, form_type, year)[i]).text for i in range(len(get_links(cik, form_type, year)))]
    souplist = [bs4.BeautifulSoup(docstrings[i], 'html.parser') for i in range(len(docstrings))]
    taglist2 = [souplist[i].find_all('a') for i in range(len(souplist))]
    print(taglist2)

    m = 0
    htm_list = []
    for j in range(len(taglist2[0])):
        if str(year) in taglist2[0][j].getText():
            for i in range(len(taglist2[0])):
                if '.htm' in taglist2[0][i].getText():
                    m += 1
                    print('https://www.sec.gov' + taglist2[0][i]['href'])
                    htm_list.append('https://www.sec.gov' + taglist2[0][i]['href'])
            break



    if m == 0:
        print(f'There is no {form_type} form available for {year}.')

    print(htm_list[0])
    return htm_list[0]

get_links(cik, form_type, year)
form_htm = get_htm()

# Use classes to create methods to generate any metric the user wishes to know

result3 = requests.get(form_htm).text
formsoup = bs4.BeautifulSoup(result3, 'lxml')
toc = []
b = formsoup.find_all('td', {'valign': 'bottom', 'align': 'right'})
number_text_list = []
for i in range(len(b)):
    number_text_list.append(str(b[i].getText()).strip())
print(number_text_list)
#c = formsoup.find_all('td', {'valign': 'top'})
#print(b)
#print(c)
#c_text_list = [c[i].getText() for i in range(len(c))]
#net_sales_indices = [i for i, x in enumerate(c_text_list) if 'Net sales' in x]
#print(c_text_list)
#print(net_sales_indices)
#for i in net_sales_indices:
 #   print(c_text_list[i+1])
toc_pattern = r'[(]?\d+[.,]?\d*'
#print(b[10].getText())
#print(type(b[10].getText()))
#print(re.findall(toc_pattern, b[10]))
for i in range(len(b)):
    if re.search(toc_pattern, b[i].getText()):
        toc.append(re.search(toc_pattern, b[i].getText()).group())
#print(toc)
#print(formsoup.find_all('b'))
#for i in range(len(formsoup.find_all('b'))):
 #   if str(formsoup.find_all('b')[i]).strip() == 'CONSOLIDATED STATEMENTS OF OPERATIONS':
  #      print(repr(str(formsoup.find_all('b')[i]).strip()))

# The code directly below (ending with 'print(ptag)') works!
plist = formsoup.find_all('p')
#print(plist)
#for i in range(len(plist)):
 #   if 'CONSOLIDATED' in str(plist[i]):
  #      print(plist[i])

l=0
for i in range(len(plist)):
    for p in plist[i].descendants:
        if 'CONSOLIDATED STATEMENTS OF OPERATIONS' == str(p).strip():
            l += 1
            ptag = plist[i]
            break

if l > 0:
    print(ptag)

v = 0
for i in range(len(plist)):
    for p in plist[i].descendants:
        if 'CONSOLIDATED BALANCE SHEETS' == str(p).strip():
            v += 1
            ptag2 = plist[i]
            break

if v > 0:
    print(ptag2)

n = 0
for i in range(len(plist)):
    for p in plist[i].descendants:
        if "CONSOLIDATED STATEMENTS OF SHAREHOLDERS" and 'EQUITY 'in str(p).strip():
            n += 1
            ptag3 = plist[i]
            break

if n > 0:
    print(ptag3)

n = 0
for i in range(len(plist)):
    for p in plist[i].descendants:
        if "CONSOLIDATED STATEMENTS OF CASH FLOWS" == str(p).strip():
            n += 1
            ptag4 = plist[i]
            break

if n > 0:
    print(ptag4)

n = 0
for i in range(len(plist)):
    for p in plist[i].descendants:
        if "See accompanying Notes to Consolidated Financial Statements." == str(p).strip():
            n += 1
            ptag5 = plist[i]
            break

if n > 0:
    print(ptag5)

z = 0
statements_of_operations = []
balance_sheets = []
shareholders_equity = []
cash_flows = []


y = statements_of_operations
x = ptag
for sibling in x.next_siblings:
    if sibling == ptag2:
        x = ptag2
        y = balance_sheets
        break
    elif 'NavigableString' not in str(type(sibling)):
        for number in sibling.descendants:
            if re.search(toc_pattern, str(number).strip()):
                if len(re.search(toc_pattern, str(number).strip()).group()) > 2 or re.search(toc_pattern, str(number).strip()).group() == 0:
                    if re.search(toc_pattern, str(number).strip()).group() in number_text_list:
                        z += 1
                        y.append(re.search(toc_pattern, str(number).strip()).group())

for sibling in x.next_siblings:
    if sibling == ptag3:
        x = ptag3
        y = shareholders_equity
        break
    elif 'NavigableString' not in str(type(sibling)):
        for number in sibling.descendants:
            if re.search(toc_pattern, str(number).strip()):
                if len(re.search(toc_pattern, str(number).strip()).group()) > 2 or re.search(toc_pattern, str(number).strip()).group() == 0:
                    if re.search(toc_pattern, str(number).strip()).group() in number_text_list:
                        z += 1
                        y.append(re.search(toc_pattern, str(number).strip()).group())

for sibling in x.next_siblings:
    if sibling == ptag4:
        x = ptag4
        y = cash_flows
        break
    elif 'NavigableString' not in str(type(sibling)):
        for number in sibling.descendants:
            if re.search(toc_pattern, str(number).strip()):
                if len(re.search(toc_pattern, str(number).strip()).group()) > 2 or re.search(toc_pattern, str(number).strip()).group() == 0:
                    if re.search(toc_pattern, str(number).strip()).group() in number_text_list:
                        z += 1
                        y.append(re.search(toc_pattern, str(number).strip()).group())

for sibling in x.next_siblings:
    if sibling == ptag5:
        break
    elif 'NavigableString' not in str(type(sibling)):
        for number in sibling.descendants:
            if re.search(toc_pattern, str(number).strip()):
                if len(re.search(toc_pattern, str(number).strip()).group()) > 2 or re.search(toc_pattern, str(number).strip()).group() == 0:
                    if re.search(toc_pattern, str(number).strip()).group() in number_text_list:
                        z += 1
                        y.append(re.search(toc_pattern, str(number).strip()).group())
if z > 0:
    print(statements_of_operations)
    print(balance_sheets)
    print(shareholders_equity)
    print(cash_flows)

#while z < 4:
 #   for sibling in ptag.next_siblings:
  #      z += 1
   #     print(repr(sibling))
