```
python版本
	这里选择的是python2.7。
	因为pyinstaller在这个版本下能正常运行。其他版本不行和其他的py2exe的方法都不靠谱（亲自测试过）
	py2exe的工具，请参考https://stackoverflow.com/questions/14165398/a-good-python-to-exe-compiler


操作过程
	运行'pyinstaller <name.py>' 千万不要加--onefile参数，不然不好吧需要的文件加进去  如：pyinstaller simple.py
	进入path_to\dist\name 目录下 把需要的文件都复制到这里就可以了。 如：path_to\dist\simple
	cmd 进入到path_to\dist\name  如: cd path_to\dist\simple
	在cmd下运行生成的exe文件 如：simple.exe
	根据提示把所需要的问题件都复制过去，就可以了。
```
