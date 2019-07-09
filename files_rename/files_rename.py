import os

def rename(path, num=1):
    filelist = os.listdir(path) #读取绝对路径/home/yyy/EAST-master/datase/text'/×××.xxx
    
    filelist = sorted(filelist)
    Newdir = 'txt'
    if not os.path.exists(Newdir):
        os.makedirs(Newdir) #检查目录newdir是否存在，不存在则创建新的目录
    for files in filelist:
        Olddir = os.path.join(path, files) #读取组合路径，path+files
        if os.path.isdir(Olddir):
            continue
        filename = os.path.splitext(files)[0]#分离扩展名和文件类型
        filetype = os.path.splitext(files)[1]
        if 'img_' + str(num) == filename:
            num = num + 1
            continue
        New_name = 'img_' + str(num) + filetype
        os.system("cp "  + Olddir+ ' '+ os.path.join(Newdir, New_name )) #终端实行cp Olddir  os.path.join(Newdir,New_name)
        num = num + 1

if __name__ == "__main__":
    path = '/home/yyy/EAST-master/datase/txt_train'
    num = 1
    rename(path,num)
