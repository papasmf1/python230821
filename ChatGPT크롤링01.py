import os
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def crawl_blog_data(search_keyword, num_pages):
    wb = Workbook()
    ws = wb.active
    ws.append(["Blog Name", "Blog Post URL", "Post Date"])

    for page in range(1, num_pages + 1):
        base_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 10}"
        response = requests.get(base_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            blog_results = soup.find_all("li", class_="sh_blog_top")

            for result in blog_results:
                blog_name = result.find("a", class_="sh_blog_title").text
                blog_post_url = result.find("a", class_="sh_blog_title")['href']
                post_date = result.find("span", class_="sub_time").text

                ws.append([blog_name, blog_post_url, post_date])
        else:
            print(f"Failed to retrieve the page {page}.")

    # Save Excel file
    save_path = os.path.join("C:\\work", f"{search_keyword}_blog_data.xlsx")
    wb.save(save_path)
    print(f"Data saved to {save_path}")

# Replace 'your_search_keyword' with the desired keyword
search_keyword = input("Enter the search keyword: ")
num_pages = 5  # Adjust the number of pages as needed
crawl_blog_data(search_keyword, num_pages)
