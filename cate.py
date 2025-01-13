import os
import shutil


def classify_files(source_folder, target_folder):
    # 确保目标文件夹存在
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)


    # 创建类别文件夹
    categories = {
        'Audio':['audio'],
        'Browsing':['browsing'],
        'Chat': ['chat'],
        'File': ['ftps', 'sftp', 'file'],
        'Mail': ['mail'],
        'P2P': ['p2p'],
        'Video': ['youtube', 'spotify', 'vimeo','netflix'],
        'VoIP': ['voip']
    }
    category_folders = {}
    for category in categories:
        category_folder = os.path.join(target_folder, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        category_folders[category] = category_folder


    # 遍历源文件夹中的文件
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_lower = file.lower()  # 将文件名转换为小写，以实现不区分大小写的匹配
            found_category = False  # 标记是否找到文件所属类别
            for category, keywords in categories.items():
                for keyword in keywords:
                    if keyword in file_lower:
                        destination_folder = category_folders[category]
                        found_category = True
                        break
                if found_category:
                    break


            if not found_category:
                continue  # 如果文件不包含上述关键词，跳过该文件


            # 构建源文件和目标文件的完整路径
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_folder, file)


            # 复制文件
            try:
                shutil.copy(source_file, destination_file)
                print(f'Moved {file} to {destination_folder}')
            except Exception as e:
                print(f'Failed to move {file}: {e}')


if __name__ == "__main__":
    # 请将这里的路径修改为你实际的文件夹地址
    source_folder = 'D:/data/pcap2graph/tcp'
    target_folder = 'D:/data/pcap2graph/cate'
    classify_files(source_folder, target_folder)