#coding=utf-8
'''
1.描述：
根据文件后缀名,对文件进行分类
    输入: 文件夹A的绝对路径
    输出: (1). 在输入A同级目录下,生成新文件夹A_reorganize,
    (2)新文件夹中根据A中的文件后缀,建立不同的下一级文件夹example：???.???/a.avi,（3）并将对应类型的文件复制到该子文件夹下

    1.(1)遍历根目录下所有文件（文件树） 方法：os.walk() --> 通过在目录树中游走输出在目录中的文件名，向上或者向下(参数）;(2)返回文件名：os.path.splitext(“path”)-->分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作
    2.创建：1.which 目录（！！） 2.创建文件夹 3. 路径copy（匹配which目录）

'''
import time,os,shutil
import argparse

def add_parser_model_arguments(parser=None):
    if parser is None:
        parser = argparse.ArgumentParser()
    parser.add_argument('--rootDir', type=str, default='../data/spider-master',
                            help='input dataDir')
    parser.add_argument(
                        '--Dir_name',type=str,default='spider-master',
                        help='the name of the Dir which contains the docs to be processed'
                        )
    return parser

def iter_files(rootDir):
    # 遍历根目录
    start = time.time()
    count = 0

    file_fullname_list=[]
    file_name_list=[]
    file_extension_list=[]

    print('-------start loading document------')
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            count+=1

            file_fullname = os.path.join(root, file)
            file_name = os.path.splitext(file)[0]  # 读取文件名
            file_extension = os.path.splitext(file)[1]  # 读取文件后缀名
            # print("文件名:", file_name)
            # print("文件后缀名:", file_extension)

            file_extension_list.append(file_extension.lstrip('.'))
            file_fullname_list.append(file_fullname)
            file_name_list.append(file_name)

    return file_extension_list,file_fullname_list,file_name_list,start,count

def create_folder(file_extension_list):
    os.chdir(rootDir) #切换当前文件path （重要）
    for extensions in file_extension_list:
        if not extensions == '':  #是否没有后缀名
            if not os.path.exists(extensions):
                os.mkdir(extensions)  # 如果工作目录下不存在以当前扩展名命名的文件夹则创建该文件夹（默认属性为0777）

def move_docs_and_rename(dirname,file_extension_list,file_fullname_list,file_name_list):
    current_path=os.getcwd()
    for extensions,fullnames,file_name in zip(file_extension_list,file_fullname_list,file_name_list):
        if file_name=='.DS_Store':
            print('ignore exist .DS_Store ')
        else:
            try:
                tar_path = os.path.join(current_path, extensions)
                src_path=os.path.join(current_path,dirname+fullnames.split(dirname)[-1])
                # print(tar_path,src_path)
                copied_path=shutil.copy(src_path,tar_path)
                alter_name = src_path.replace('\\', '.')
                # print(fullnames)
                print(alter_name)
                # # print(fullnames,alter_name)
                alter_path = os.path.join(tar_path, alter_name)
                print(alter_path)
                print(copied_path)
                try:
                    os.rename(copied_path,alter_path)
                except FileNotFoundError :
                    print("FileNotFound:",alter_name)


            except shutil.SameFileError as e:
                print('file exist, info: ',e)
            except IsADirectoryError as i:
                print("there is a dictionary")
            except FileNotFoundError:
                print("the classification is already done")

if __name__ == '__main__':
    #add args :  # run in terminal ->
    # python main.py --rootDir=''  default ='../data/spider-master'\
                   # --Dir_name='' default ='spider-master'
    parser = add_parser_model_arguments()
    args = parser.parse_args()
    rootDir=args.rootDir
    Dirname=args.Dir_name

    #steps : 1. iter_file  2. create dir ; 3.copy and rename
    file_extension_list,file_fullname_list,file_name_list,start_time,files_count=iter_files(rootDir)
    create_folder(file_extension_list)
    move_docs_and_rename(Dirname,file_extension_list,file_fullname_list,file_name_list)

    #count for time
    total_time = time.time() - start_time
    print("程序运行时间：%0.2f"%total_time)
    print("共处理文件：%d"%files_count)