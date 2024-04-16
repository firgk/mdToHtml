from  deffer import *
if __name__ == '__main__':
    md_name = "example.md"
    html_name = "example.html"

    if(mdtox(md_name).to_html(html_name)):
        print('转换完成')