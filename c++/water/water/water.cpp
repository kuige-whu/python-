// water.cpp : �������̨Ӧ�ó������ڵ㡣
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
		cout << "δ�ɹ����ļ�" << endl;
	}
	while (infile>>w)
	{
		outfile << w;
		outfile << endl;
	}
	infile.close();
	outfile.close();
	cout << "ִ�н�����" << endl;
	system("pause");
	return 0;
}