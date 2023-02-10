import SimpleITK as sitk

# Dicom序列所在文件夹路径（在我们的实验中，该文件夹下有多个dcm序列，混合在一起）
file_path = "/data/jianjunming/BEOT/BEOT_1st/B/B13-5219998/"

# 获取该文件下的所有序列ID，每个序列对应一个ID， 返回的series_IDs为一个列表
series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(file_path)

# 查看该文件夹下的序列数量
nb_series = len(series_IDs)
print(nb_series)

# 通过ID获取该ID对应的序列所有切片的完整路径， series_IDs[0]代表的是第一个序列的ID
# 如果不添加series_IDs[0]这个参数，则默认获取第一个序列的所有切片路径
series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(file_path, series_IDs[0])

# 新建一个ImageSeriesReader对象
series_reader = sitk.ImageSeriesReader()

# 通过之前获取到的序列的切片路径来读取该序列
series_reader.SetFileNames(series_file_names)

# 获取该序列对应的3D图像
image3D = series_reader.Execute()

# 查看该3D图像的尺寸
print(image3D.GetSize())

# 将序列保存为单个的NRRD文件
sitk.WriteImage(image3D, 'img3D.nrrd')
