// water292vector.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include<iostream>
#include <string>
#include <vector>
#include <fstream>  //�ļ����⺯��

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
		cout << "δ�ɹ����ļ�" << endl;
	}
	while (infile >> wv)
	{
		s.push_back(wv);
	}
	cout << "�Ǳ�������������" << endl;
	cout << s[0] * (2.994e-22) << endl << s[99] * (2.994e-22) << endl;

	//���԰�vector
	/*while (i <292)
	{
		wv = 292 - i;
		s.push_back(wv);

		i++;
	}*/


	cout << "����������������ʪ�ȣ���λg/m^3" << endl;
	cout << "Ȼ��Ctrl+'Z'+Enter����ѭ��" << endl;
	double dam,WV, tg;
	while (cin >> dam)
		WV = dam * 1000 / (2.994E-19); //һǧ�׸߶���ÿƽ�����׵�ˮ��������
		
	//���԰�WV=dam;
	tg = WV;   //target
	

	int it=0;
	if (tg <= s[1] && tg >= s[99]) //�߶�����10km
	{
		for (int k = 1; k < 99; ++k) 
		{
			if (tg <= s[k] && tg > s[k + 1])
				it = k;
			
		}
		cout<<"ƥ��߶ȣ�" <<it*0.1<<"km"<< endl;
		for (int i=0 ;i!=292;++i)
		{
			if (i < 292 - it)
				s[i] = s[i + it];
			else
				s[i] = 0;
		}
	}
	//��������
	else 
	{
		cout << "scaling:";  //��������
		double scale = tg / s[0];
		cout << scale<< endl<<"tg:"<<tg<<endl<<"s[0]:"<<s[0]<<endl;
		for (auto &i : s)
			i = scale*i;
	}
	double sum=0,SUMWV=0;
	for (int i = 0; i<292; ++i)
	{
		outfile << s[i];//�������ڵ������������������292��
		outfile << endl;
		sum += s[i];
	}
	SUMWV = sum*(2.994e-19)*(1e-5) ;
	cout << "��������ɽ�ˮ��:"<<SUMWV <<"cm"<< endl;
	infile.close();
	outfile.close();
	system("pause");
    return 0;
}

