1. 问题描述：
根据文件后缀名,对文件进行分类，生成的文件设定朔源名称xxx.xxx.test.py etc.

2.解答步骤：
（1）文件结构
--projectName--
                         |
------------------data
		|
-----------------------dataDir(NAMED AS "rootDir")
				             |
-------------------------------------------------------EXTENSION_TYPE_Dir(NAMED AS "docx" etc.)
									 |
--------------------------------------------------------------------------------------------------------corresponding docs (the name be changed to xxx.xxx.test.py etc.)

-------------------------------------------------------Origin data (To be processed)
	
---------------------src
		 |
		 main.py(processing step 1,2,3)

(2)mian.py -> Processing step:
1, func iter_files():
	input: ''rootDir'' (dataDir）#遍历dataDir下所有文件夹的所有文件（Origin data (To be processed)）
	return extension_list, fullname_list, filename_list 
2,func create_folder:
	input： extension_list
	return None
3, func move_docs_and_rename()：
	input:extension_list, fullname_list, filename_list 
	STEP 3.1 : copy:  shutil.copy(src,tar)
		src in fullname_list
		tar in extensions
	SSTP 3.2 :rename: os.rename(src,tar)
		src in path=shutil.copy(src,tar)
		tar in fullname_list

初期考虑：python os 模块（文件操作）；shutil（文件拷贝）
查看文档：
1. https://docs.python.org/3.6/library/shutil.html
2. https://docs.python.org/3.6/library/shutil.html
涉及: python内置os模块（对目录或文件的新建，对文件以及目录的路径操作）、shutil模块（高等级的目录或文件的移动/复制/打包/压缩/解压等操作）
