#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@Author : Huizhi Xu
@File : process_xml.py
@Time : 2024/02/23 21:13:26
@Desc : 
'''
from bs4 import BeautifulSoup



def get_metadata(soup):
    # Extract the title
    title = soup.find('titleStmt').find('title', type='main').text.strip()

    # Extract the authors
    authors = []
    author_elements = soup.find_all('author')
    for author_element in author_elements:
        forename_element = author_element.find('forename', type='first')
        forename = forename_element.text.strip() if forename_element else ""
        surname = author_element.find('surname').text.strip()
        authors.append(f"{forename} {surname}")

    # Extract the organizations and affiliations
    organizations = []
    affiliations = []
    org_elements = soup.find_all('orgName', type='institution')
    for org_element in org_elements:
        organizations.append(org_element.text.strip())

    aff_elements = soup.find_all('affiliation')
    for aff_element in aff_elements:
        org_names = aff_element.find_all('orgName', type='institution')
        org_texts = [org_name.text.strip() for org_name in org_names]
        affiliations.append(", ".join(org_texts))

    # Extract the DOI and MD5
    doi = soup.find('idno', type='DOI').text.strip()
    md5 = soup.find('idno', type='MD5').text.strip()

    # Extract the language
    language = soup.find('teiHeader').get('xml:lang')

    # Print the extracted information
    print('Title:', title)
    print('Authors:', ", ".join(authors))
    print('Organizations:', ", ".join(organizations))
    print('Affiliations:', "\n".join(affiliations))
    print('DOI:', doi)
    print('MD5:', md5)
    print('Language:', language)



def get_paragraphs(soup):

    # Extract the paragraphs
    paragraphs = []
    p_elements = soup.find_all('p')
    for p_element in p_elements:
        paragraph = p_element.text.strip()
        paragraphs.append(paragraph)

    # Print the extracted paragraphs
    # print('Paragraphs:')
    # for i, paragraph in enumerate(paragraphs):
        
    #     print(f"-------第{i}段paragraph----------------------")
    #     print(paragraph)
    return paragraphs


def get_sections(soup):

    # Find the <abstract> element
    abstract = soup.find('abstract')

    # Extract the introduction section
    introduction = abstract.find('p').text

    # Extract the experimental section if it exists
    experimental = ""
    for p in soup.find_all('p'):
        if "experimental" in p.text.lower():
            experimental = p.text
            break

    # Extract the result and discussion section if it exists
    result_discussion = ""
    for p in soup.find_all('p'):
        if "results" in p.text.lower() or "discussion" in p.text.lower():
            result_discussion = p.text
            break

    # Extract the conclusion section
    conclusion = soup.find_all('p')[-1].text

    # Print the extracted sections
    print("Introduction:")
    print(introduction)
    print("\nExperimental:")
    print(experimental)
    print("\nResults and Discussion:")
    print(result_discussion)
    print("\nConclusion:")
    print(conclusion)

if __name__ == "__main__":
    # Read the XML file
    with open('data/grobid_data/catal9121069.xml', 'r', encoding='utf-8') as file:
        xml_content = file.read()


    # Parse the XML using BeautifulSoup
    soup = BeautifulSoup(xml_content, 'xml')

    # get_metadata(soup)
    # paragraphs = get_paragraphs(soup)
    sections = get_sections(soup)
  



