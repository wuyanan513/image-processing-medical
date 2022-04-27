from lungmask import mask  #lungmask refer:https://github.com/JoHof/lungmask
import SimpleITK as sitk
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
def save_itk(image, origin, spacing, filename):
	"""
	:param image: images to be saved
	:param origin: CT origin
	:param spacing: CT spacing
	:param filename: save name
	:return: None
	"""
	if type(origin) != tuple:
		if type(origin) == list:
			origin = tuple(reversed(origin))
		else:
			origin = tuple(reversed(origin.tolist()))
	if type(spacing) != tuple:
		if type(spacing) == list:
			spacing = tuple(reversed(spacing))
		else:
			spacing = tuple(reversed(spacing.tolist()))
	itkimage = sitk.GetImageFromArray(image, isVector=False)
	itkimage.SetSpacing(spacing)
	itkimage.SetOrigin(origin)
	sitk.WriteImage(itkimage, filename, True)

if __name__ == '__main__':
    main_path = r'C:\Users\Administrator\Desktop\exct09\train/'
    save_path = r'C:\Users\Administrator\Desktop\exct09\lungmasktrain/'
    img_path = os.listdir(main_path)
    img_path.sort()
    for img in img_path:
        input_path=os.path.join(main_path,img)
        input_image = sitk.ReadImage(input_path)
        a=input_image.GetSpacing()
        segmentation = mask.apply(input_image) 
        # new_mask_img1 = sitk.GetImageFromArray(segmentation)
        # new_mask_img1.SetDirection(input_image.GetDirection())
        # new_mask_img1.SetOrigin(input_image.GetOrigin())
        # new_mask_img1.SetSpacing(input_image.GetSpacing())
        # b = new_mask_img1.GetSpacing()
        new_file_path = save_path
        path = os.path.join(new_file_path, img)
        save_itk(segmentation,input_image.GetOrigin(),input_image.GetSpacing(),path)
