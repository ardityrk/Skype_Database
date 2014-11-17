__author__ = 'ardi'

import sqlite3
import html
import datetime
import sys
import requests

def get_all_links_from_history():
    with sqlite3.connect("main.db") as connection:
        c = connection.cursor()
        chat = c.execute("SELECT body_xml,author,timestamp FROM Messages where body_xml like '%a href%'")

        with open('links.html', 'w', encoding="UTF-8") as f:
            f.write('<html>'+'\n')
            f.write('<table style="width:100%">'+'\n')
            f.write('<tr>')
            f.write('<th>Person</th>'+'\n')
            f.write('<th>URL</th>'+'\n')
            f.write('<th>Date</th>'+'\n')
            f.write('</tr>'+'\n')
            for row in chat:
                f.write('<tr>')
                f.write('<td>'+row[1]+'</td>')
                body_xml = row[0]
                pretty_link = body_xml[body_xml.find("href")+6:body_xml.find(">")-1]

                response = requests.get(pretty_link)
                page_content = response.text
                if page_content.find("<title>")<0:
                    title = "NO TITLE"
                else:
                    title = page_content[page_content.find("<title>")+7:page_content.find("</title>")]

                f.write('<td>'+title+" "+pretty_link+'</td>')
                f.write('<td>'+str(row[2])+'</td>')
                f.write('</tr>')
            f.write('</table>')
            f.write('</html>'+'\n')

if __name__ == '__main__':
    get_all_links_from_history()
