'''
coding = UTF-8
coding by HYJ & DeepSeek
'''


import requests
from bs4 import BeautifulSoup  # 用于解析 HTML
import csv                     # 用于保存数据到 CSV 文件

# 1. 让用户输入网址（不带 https://）
data = input("请输入网址（请勿带https://）")
url = 'https://' + data
print("请求网址为:", url)

# 2. 发送 HTTP 请求，获取网页内容
result = requests.get(url)
# 手动设置编码为 UTF-8（防止中文乱码）
result.encoding = 'utf-8'

# 3. 检查请求是否成功
print("状态码:", result.status_code)

# 如果状态码不是 200，说明可能出错，退出程序
if result.status_code != 200:
    print("请求失败，请检查网址或网络")
    exit()

# 4. 用 BeautifulSoup 解析 HTML 源码
soup = BeautifulSoup(result.text, 'html.parser')

# 5. 提取所有链接（<a> 标签且含有 href 属性）
links = []
for a in soup.find_all('a', href=True):
    text = a.get_text(strip=True)   # 链接文字（去掉首尾空白）
    href = a['href']                 # 链接地址
    if text:                         # 只保留有文字的链接
        links.append([text, href])

# 6. 把提取到的链接保存到 CSV 文件
csv_filename = '提取的链接.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['项目', '链接'])   # 写入表头
    writer.writerows(links)            # 写入所有链接

print(f"已提取 {len(links)} 条链接，保存到 {csv_filename}")

# 7. 可选：在屏幕上预览前 10 条链接
print("\n前5条链接预览：")
for text, href in links[:5]:
    print(f"{text} -> {href}")
input("按任意键退出")