clear all
clc
input_path =  'E:\paper1\实验用的数据\data';
pw = genpath(input_path);    
length_p = size(pw,2);  
path = {};  
temp = [];
for k = 1:length_p 
    if pw(k) ~= ';'
        temp = [temp pw(k)];
    else
        temp = [temp '\'];
        path = [path ; temp];
        temp = [];
    end 
end
clear p length_p temp; 
file_num = size(path,1);   
D = {};
for i = 1:file_num
    formatSpec = '%4.2f%% is finished! \n';
%     fprintf(formatSpec,i/file_num*100);
    file_path = path{i};  
    img_path_list=dir(strcat(file_path,'*.DCM'));
    img_num = length(img_path_list);
    if isempty(img_path_list)
        continue;
    end
  
    for j = 1:1
        image_name = img_path_list(j).name;
%          pick_pro = strfind(image_name,'???ù');
%         if pick_pro
%             continue;
%         end
%       name1 = image_name(1:10);
      ImageName = strcat(file_path,image_name);
      C(j,:) = infodcm(ImageName);

    end
    
    D = [D;C];
    C = {};
end
name = {'PatientID','Gender','PatientName','AccessionNumber','PatientBirthDate',...
    'Age','SliceThickness','KVP','XrayTubeCurrent',...
   'PixelSpacing','Manufacturer','Exposure','AcquisitionDate'};
xlswrite('data1.xlsx',name,'sheet1','A1');
xlswrite('data1.xlsx',D,'sheet1','A2');
Infom = cell(5,10);
function C = infodcm(str)
%     str = ['Image',num2str(i),'.dcm'];
% str = 'CT.1.2.156.14702.1.1005.128.2.202001201125531458469.dcm';
info = dicominfo(str);
if ~isfield(info,'PatientID')
    info.PatientID = '0';
end
if ~isfield(info,'PatientSex')
    info.PatientSex = '0';
end
if ~isfield(info,'PatientBirthDate')
    info.PatientBirthDate = '0';
end
if ~isfield(info,'PatientAge')
    info.PatientAge = '0';
end
if ~isfield(info,'SliceThickness')
   info.SliceThickness = '0';
end
if ~isfield(info,'KVP')
    info.KVP = '0';
end
if ~isfield(info,'XrayTubeCurrent')
    info.XrayTubeCurrent = '0';
end
if ~isfield(info,'PixelSpacing')
    info.PixelSpacing = '0';
end
if ~isfield(info,'Manufacturer')
    info.Manufacturer = '0';
end
if ~isfield(info,'Exposure')
    info.Exposure = '0';
end
if ~isfield(info,'AcquisitionDate')
    info.AcquisitionDate = '0';
end
s = struct('PatientID',info.PatientID,'PatientName',info.PatientName.FamilyName,'AccessionNumber',info.AccessionNumber,'Gender',info.PatientSex,'PatientBirthDate',...
    info.PatientBirthDate,'Age',info.PatientAge,'SliceThickness',info.SliceThickness,'KVP',info.KVP,'XrayTubeCurrent',info.XrayTubeCurrent,...
    'PixelSpacing',info.PixelSpacing(1),'Manufacturer',info.Manufacturer,'Exposure',info.Exposure,'AcquisitionDate',info.AcquisitionDate);
C = struct2cell(s);
C = C';
end

