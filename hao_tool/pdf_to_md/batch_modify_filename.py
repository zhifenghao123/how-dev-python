import os

def batch_modify_file_name(folder_path):
    # 获取文件夹中的所有文件名
    files = os.listdir(folder_path)

    # 遍历文件并重命名
    for file in files:
        # 检查文件是否是文件夹
        if os.path.isdir(os.path.join(folder_path, file)):
            continue

            # 构建新文件名
        new_file = file.replace('第01章_Linux下MySQL的安装与使用.', '1-')

        # 重命名文件
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_file))


if __name__ == '__main__':
    # 要修改的文件夹路径
    folder_path = '../dataset/pdf2md/第01章_Linux下MySQL的安装与使用'
    batch_modify_file_name(folder_path)
