# UTF-8  coding by HYJ X DeepSeek
import os
import shutil

# 要整理的文件夹路径（改成你自己的）
while True:
    target_dir = input("请输入要整理的文件夹路径：").strip()
    if os.path.exists(target_dir):
        break
    else:
        print("路径不存在，请重新输入！")
# 定义文件类型对应的文件夹名
file_types = {
    '.jpg': '图片', '.png': '图片', '.gif': '图片',
    '.pdf': '文档', '.docx': '文档', '.txt': '文档',
    '.exe': '程序', '.msi': '程序',
    '.py':'代码','.cpp':'代码'
}

# 遍历该文件夹下的所有文件
for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)
    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()
        if ext in file_types:
            target_folder = os.path.join(target_dir, file_types[ext])
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"移动: {filename} -> {target_folder}")
        if ext not in file_types:
            print("未找到对应类型")