from lungmask import mask  #lungmask refer:https://github.com/JoHof/lungmask
import SimpleITK as sitk
import os

if __name__ == '__main__':
    img_path = os.listdir('./data2snii')
    for img in img_path:
        input_path=os.path.join('data2snii',img)
        input_image = sitk.ReadImage(input_path)
        segmentation = mask.apply(input_image) 
        new_mask_img1 = sitk.GetImageFromArray(segmentation)
        new_mask_img1.SetDirection(input_image.GetDirection())
        new_mask_img1.SetOrigin(input_image.GetOrigin())
        new_mask_img1.SetSpacing(input_image.GetSpacing())
        new_file_path = './data2slung'
        path = os.path.join(new_file_path,img)
        sitk.WriteImage(new_mask_img1, path)
