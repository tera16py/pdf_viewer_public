import os

page_path = os.getcwd() + '/toppage.html'
base_file_path = os.getcwd() + '/pdfjs/web/'
base_href_path = 'http://localhost:8000/pdfjs/web/viewer.html?file='

ignore_files = ['.DS_Store', 'locale', 'images', 'compressed.tracemonkey-pldi-09.pdf', 'viewer.js.map', 'viewer.js', 'cmaps', 'viewer.html', 'viewer.css', 'debugger.js']

page_file = open(page_path, mode='w')
page_file.write('<meta http-equiv="content-type" charset="utf-8">\n')
page_file.write('<h1>論文一覧</h1>\n')
page_file.write('. <br>\n')


def insert_space(base_text, count):
    text = base_text
    for i in range(count):
        text = '&nbsp ' + text
    return text


def make_dir_list(file_path, href_path, depth):
    for file_name in os.listdir(file_path):
        if file_name in ignore_files:
            continue
        if os.path.isfile(file_path + file_name):
            link = '"' + href_path + file_name + '"'
            html_text = 'L <a href=' + link + '>' + file_name + '</a><br>\n'
            page_file.write(insert_space(html_text, depth))
        else:
            html_text = 'L ' + file_name + '<br>' + '\n'
            page_file.write(insert_space(html_text, depth))
            next_file_path = file_path + file_name + '/'
            next_href_path = href_path + file_name + '/'
            next_depth = depth + 1
            make_dir_list(next_file_path, next_href_path, next_depth)


make_dir_list(base_file_path, base_href_path, 0)
