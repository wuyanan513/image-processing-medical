def get_ct_file(main_path):
    ctpath = []
    # 遍历该文件夹下的所有目录或者文件
    for root, s_dirs, _ in os.walk(main_path, topdown=True):  # 获取 train文件下各文件夹名称
        for sub_dir in s_dirs:
            i_dir = os.path.join(root, sub_dir) # 获取各类的文件夹 绝对路径
            img_list = os.listdir(i_dir)                    # 获取类别文件夹下所有png图片的路径
            for i in range(len(img_list)):
                if img_list[i].endswith('.gz'):
                    path = os.path.join(i_dir, img_list[i])
                    ctpath.append(path)
    return ctpath
