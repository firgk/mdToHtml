import os
from deffer import mdtox

def convert_md_to_html(md_file, html_file, output_path,source_path):
    if mdtox(source_path+md_file).to_html(output_path + html_file):
        print(f'已将 {source_path+md_file} 转换为 {output_path + html_file}')
    else:
        print(f'转换 {source_path+md_file} 为 {output_path + html_file} 时出现问题')


def create_html_index(output_path, html_files):
    index_content = """<html><body>
    <body><html>
    <style>
    /* 给链接添加样式 */
    a {
        color: #0066cc;
        /* 链接颜色 */
        text-decoration: none;
        /* 去除下划线 */
        font-weight: bold;
        /* 加粗字体 */
        transition: color 0.3s;
        /* 添加颜色过渡效果 */
    }

    /* 鼠标悬停时改变链接颜色 */
    a:hover {
        color: #004080;
        /* 鼠标悬停时的颜色 */
    }

    /* 设置段落间距 */
    p {
        text-align: left;
        /* 文本居中显示 */
        padding-left: 250px;
        margin: 10px 0;
        /* 顶部和底部边距为10像素 */
    }
    h1{
        padding-left: 200px;
    }
</style>
<h1>整理的计算机笔记</h1>
    <ul>"""
    for html_file in html_files:
        index_content += f'<li><a href="{html_file}">{html_file}</a></li>'
    index_content += "</ul></body></html>"

    with open(os.path.join(output_path, 'index.html'), 'w') as index_file:
        index_file.write(index_content)

def main():
    source_path = "md\\"
    output_path = "html\\"
    print(source_path)
    print(output_path)
    html_files = []
    for file in os.listdir(source_path):
        if file.endswith('.md'):
            html_file = file.replace('.md', '.html')
            convert_md_to_html(file, html_file, output_path,source_path)
            html_files.append(html_file)

    create_html_index(output_path, html_files)

if __name__ == '__main__':
    main()