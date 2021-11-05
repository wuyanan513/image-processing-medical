import vtk
import os
from tqdm import trange

def nii_2_mesh(filename_nii, filename_stl):
    """
    Read a nifti file including a binary map of a segmented organ with label id = label.
    Convert it to a smoothed mesh of type stl.
    filename_nii     : Input nifti binary map
    filename_stl     : Output mesh name in stl format
    label            : segmented label id
    """

    # read the file
    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(filename_nii)
    reader.Update()

    # apply marching cube surface generation
    surf = vtk.vtkDiscreteMarchingCubes()
    surf.SetInputConnection(reader.GetOutputPort())
    # surf.SetValue(0, label)  # use surf.GenerateValues function if more than one contour is available in the file
    surf.GenerateValues(3,0,2)
    surf.Update()

    # smoothing the mesh
    smoother = vtk.vtkWindowedSincPolyDataFilter()
    if vtk.VTK_MAJOR_VERSION <= 5:
        smoother.SetInput(surf.GetOutput())
    else:
        smoother.SetInputConnection(surf.GetOutputPort())
    smoother.SetNumberOfIterations(30)
    smoother.NonManifoldSmoothingOn()
    smoother.NormalizeCoordinatesOn()  # The positions can be translated and scaled such that they fit within a range of [-1, 1] prior to the smoothing computation
    smoother.GenerateErrorScalarsOn()
    smoother.Update()

    # save the output
    writer = vtk.vtkSTLWriter()
    writer.SetInputConnection(smoother.GetOutputPort())
    writer.SetFileTypeToASCII()
    writer.SetFileName(filename_stl)
    writer.Write()


if __name__ == '__main__':
    dir = r'I:\airway and lung field program\2-lungmask'
    gzFileNumber = 0  # 记录.c文件的个数为对应文件号

    for root, dirs, files in os.walk(dir):  # 遍历该文件夹
        for file in files:  # 遍历刚获得的文件名files
            (filename, extension) = os.path.splitext(file)  # 将文件名拆分为文件名与后缀
            if (extension == '.gz'):  # 判断该后缀是否为.gz文件
                filename_nii = os.path.join(root,file)
                filename_stl = filename_nii.split('.')[0].replace('nii','stl') + '.stl'
                gzFileNumber = gzFileNumber + 1  # 记录.c文件的个数为对应文件号
                nii_2_mesh(filename_nii, filename_stl)
                print(f' the processed number of file is {gzFileNumber}')
