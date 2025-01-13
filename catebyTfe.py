import os
import shutil

# 设置pcap文件所在的目录
pcap_directory = r'D:\data\pcap2graph\tcp'

# 设置类别文件夹的父目录
categories_directory = r'D:\data\pcap2graph\cate'

# 定义类别和对应的文件
categories = {
    'Audio-Streaming':r'D:\data\CATE\ISCX-Tor\CATE_ISCX_Tor_Audio-Streaming.txt',
    'Browsing':r'D:\data\CATE\ISCX-Tor\CATE_ISCX_Tor_Browsing.txt',
    'Chat': r'D:\data\CATE\ISCX-Tor\CATE_ISCX_Tor_Chat.txt',
    'Mail': r'D:\data\CATE\ISCX-Tor\CATE_ISCX_Tor_Mail.txt',
    'File': r'D:\data\CATE\ISCX-Tor\CATE_ISCX_Tor_File.txt',
    'P2P': r'D:\data\CATE\ISCX-Tor\CATE_ISCX_Tor_P2P.txt',
    'Video-Streaming': r'D:\data\CATE\ISCX-Tor\CATE_ISCX_Tor_Video-Streaming.txt',
    'VoIP': r'D:\data\CATE\ISCX-Tor\CATE_ISCX_Tor_VoIP.txt',
}

# 确保类别文件夹存在
for category in categories:
    category_path = os.path.join(categories_directory, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# 读取文件名列表并分类
category_files_directory = r'D:\data\CATE\ISCX-Tor'  # 实际存放txt类别文件的路径
for category, filename in categories.items():
    file_path = os.path.join(category_files_directory, filename)  # 构建完整的文件路径
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            files_in_category = file.read().splitlines()

        for pcap_file in files_in_category:
            source_file = os.path.join(pcap_directory, pcap_file)
            if os.path.isfile(source_file):
                destination_file = os.path.join(categories_directory, category, pcap_file)
                shutil.copy(source_file, destination_file)
                print(f'Moved: {pcap_file} to {category}')
            else:
                print(f'File not found: {pcap_file}')
    else:
        print(f'Category file not found: {file_path}')