// water.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <vector> 
#include <string> 
#include <fstream> 
#include <iostream> 

using namespace std;

int main()
{
	ifstream infile("water.txt");
	ofstream outfile("out.txt", ios::app);
	 double w;
	if (!infile.is_open())
	{
		cout << "未成功打开文件" << endl;
	}
	while (infile>>w)
	{
		outfile << w;
		outfile << endl;
	}
	infile.close();
	outfile.close();
	cout << "执行结束！" << endl;
	system("pause");
	return 0;
}