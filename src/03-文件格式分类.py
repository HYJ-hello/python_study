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
    # 图片
    '.jpg': '图片', '.jpeg': '图片', '.png': '图片', '.gif': '图片', '.bmp': '图片', '.ico': '图片', '.svg': '图片', '.webp': '图片',
    # 文档
    '.pdf': '文档', '.docx': '文档', '.doc': '文档', '.txt': '文档', '.text': '文档', '.md': '文档', '.rtf': '文档', '.wps': '文档',
    # 表格
    '.xlsx': '表格', '.xls': '表格', '.csv': '表格', '.xlsm': '表格',
    # 演示文稿
    '.pptx': '演示文稿', '.ppt': '演示文稿',
    # 程序/可执行文件
    '.exe': '程序', '.msi': '程序', '.bat': '程序', '.cmd': '程序', '.sh': '脚本', '.app': '程序', '.deb': '安装包', '.rpm': '安装包',
    # 代码
    '.py': '代码', '.cpp': '代码', '.c': '代码', '.h': '代码', '.java': '代码', '.js': '代码', '.html': '网页', '.css': '代码', '.php': '代码',
    '.go': '代码', '.rs': '代码', '.swift': '代码', '.kt': '代码',
    # 压缩包
    '.zip': '压缩包', '.rar': '压缩包', '.7z': '压缩包', '.tar': '压缩包', '.gz': '压缩包', '.bz2': '压缩包', '.xz': '压缩包',
    # 视频
    '.mp4': '视频', '.avi': '视频', '.mov': '视频', '.wmv': '视频', '.flv': '视频', '.mkv': '视频', '.webm': '视频', '.m4v': '视频',
    # 音频
    '.mp3': '音频', '.wav': '音频', '.flac': '音频', '.aac': '音频', '.ogg': '音频', '.m4a': '音频',
    # 其他
    '.iso': '镜像', '.img': '镜像', '.dll': '系统文件', '.sys': '系统文件',
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
input("整理完成，按回车键退出...")