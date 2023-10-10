import pydicom
import os
import tqdm
import xlwt

def extract_dicom_data(dicom_dir):
    tmp_list = []
    for dirpath, dirnames, filenames in os.walk(dicom_dir):
        if not dirnames:
            if "SE203" in dirpath:
                tmp_list.append(dirpath)
    return tmp_list

def get_listdir_dcm(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.ima' or os.path.splitext(file)[1] == '.dcm':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list

def loadFileInformation(filename):
    try:
        ds = pydicom.dcmread(filename)

        gender = ds.PatientSex if 'PatientSex' in ds else None
        age = ds.PatientAge if 'PatientAge' in ds else None
        kvp = ds.KVP if 'KVP' in ds else None
        slice_thickness = ds.SliceThickness if 'SliceThickness' in ds else None
        xray_tube_current = ds.XRayTubeCurrent if 'XRayTubeCurrent' in ds else None
        pixel_spacing = ds.PixelSpacing if 'PixelSpacing' in ds else None
        exposure = ds.Exposure if 'Exposure' in ds else None
        ct_scanner_manufacturer = ds.Manufacturer if 'Manufacturer' in ds else None
        pixel_size = pixel_spacing[0] if pixel_spacing else None

        return [filename,gender, age[:-1], kvp, slice_thickness, xray_tube_current, pixel_size, exposure, ct_scanner_manufacturer]
    except Exception as e:
        print(f"Error processing {filename}: {e}")

if __name__ == '__main__':
    # you can change the img_path (multiple sub_dir in the main dir is OK)
    img_path = r'H:\wanrendicom'
    img_list = extract_dicom_data(img_path)
    img_list.sort()
    # Creat a workbook in 'utf-8'
    workbook = xlwt.Workbook(encoding='utf-8')
    # Creat a worksheet named info
    worksheet = workbook.add_sheet('info') 
    # Adding headers to the first row
    headers = ["path","Gender", "Age", "kVp", "Slice Thickness", "X-ray Tube Current", "Pixel Size", "Exposure", "CT Scanner Manufacturer"]
    for idx, header in enumerate(headers):
        worksheet.write(0, idx, header)
    for i in tqdm.trange(1,len(img_list)):
        img_name = get_listdir_dcm(img_list[i])[0]
        information = loadFileInformation(img_name)
        for idx, item in enumerate(information):
            worksheet.write(i, idx, item)
    workbook.save('dicom_data.xls')
    print("Data extraction completed and saved to 'dicom_data.xls'")
