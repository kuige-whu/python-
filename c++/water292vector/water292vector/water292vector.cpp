// water292vector.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include <string>
#include <vector>
#include <fstream>  //文件流库函数

using namespace std;

int main()
{
	ifstream infile("water.txt");
	ofstream outfile("out0.1.txt", ios::app);
	vector<double> s;
	int i = 0;
	double wv;
	if (!infile.is_open())
	{
		cout << "未成功打开文件" << endl;
	}
	while (infile >> wv)
	{
		s.push_back(wv);
	}
	cout << "非比例调节上下限" << endl;
	cout << s[0] * (2.994e-22) << endl << s[99] * (2.994e-22) << endl;

	//调试版vector
	/*while (i <292)
	{
		wv = 292 - i;
		s.push_back(wv);

		i++;
	}*/


	cout << "请输入地面大气绝对湿度，单位g/m^3" << endl;
	cout << "然后按Ctrl+'Z'+Enter结束循环" << endl;
	double dam,WV, tg;
	while (cin >> dam)
		WV = dam * 1000 / (2.994E-19); //一千米高度上每平方厘米的水分子数；
		
	//调试版WV=dam;
	tg = WV;   //target
	

	int it=0;
	if (tg <= s[1] && tg >= s[99]) //高度上限10km
	{
		for (int k = 1; k < 99; ++k) 
		{
			if (tg <= s[k] && tg > s[k + 1])
				it = k;
			
		}
		cout<<"匹配高度：" <<it*0.1<<"km"<< endl;
		for (int i=0 ;i!=292;++i)
		{
			if (i < 292 - it)
				s[i] = s[i + it];
			else
				s[i] = 0;
		}
	}
	//比例调节
	else 
	{
		cout << "scaling:";  //调节因子
		double scale = tg / s[0];
		cout << scale<< endl<<"tg:"<<tg<<endl<<"s[0]:"<<s[0]<<endl;
		for (auto &i : s)
			i = scale*i;
	}
	double sum=0,SUMWV=0;
	for (int i = 0; i<292; ++i)
	{
		outfile << s[i];//将容器内的数据输出来，数据量292个
		outfile << endl;
		sum += s[i];
	}
	SUMWV = sum*(2.994e-19)*(1e-5) ;
	cout << "整层大气可降水量:"<<SUMWV <<"cm"<< endl;
	infile.close();
	outfile.close();
	system("pause");
    return 0;
}

