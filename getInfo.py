import requests 
from bs4 import BeautifulSoup
import re

def extract_social_links(soup):
    social_links = []
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if 'facebook.com' in href or 'linkedin.com' in href:
            social_links.append(href)
    return social_links

def extract_emails(soup):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    emails = re.findall(email_pattern, soup.get_text())
    return emails

def extract_contacts(soup):
    contact_pattern = r'[\+\d\s-]+'
    contacts = re.findall(contact_pattern, soup.get_text())
    return contacts

def get_website_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        social_links = extract_social_links(soup)
        emails = extract_emails(soup)
        contacts = extract_contacts(soup)

        print("Social links:")
        for link in social_links:
            print(link)

        print("\nEmail addresses:")
        for email in emails:
            print(email)

        print("\nContact details:")
        for contact in contacts:
            print(contact)

    else:
        print("Failed to fetch website content.")

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    get_website_info(website_url)
