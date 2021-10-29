#include <iostream>
#include <functional>
#include <vector>
#include <fstream>
#include <iomanip>  
using namespace std;

class Labochka1 {
private:
	/*Исследовать процедуру дискретизации синусоидального сигнала u(t) с
частотой F Гц. Длительность наблюдения сигнала 10/F секунд. Написать программу, которая позволит:*/
	double pi = 3.14159265359;
	double f1 = 1;//1
	ofstream fout;
	double F = 1; // Частота F = 1
	double step;
	double interval1 = 10 / F; // Длительность наблюдения сигнала 10/F секунд.
	double interval2 =  0;
public:

	double  U1(double t) {
		return sin(2 * pi * f1 * t);
	}

	vector<pair<double, double>> kotelnikov(vector<pair<double, double>> fun, double dt) {
		vector<pair<double, double>> tmp(fun.size() * (this->step / dt));
		for (int i = 0; i < tmp.size(); i++) {
			double sum = 0;
			double t = i * dt;
			for (int j = 0; j < fun.size(); j++) {
				double k = pi * (t / this->step - j); 

				if (k == 0) {
					sum += fun[j].second;// изначальный сигнал - он же U(n*Td)
				}
				else {
					sum += fun[j].second * (sin(k) / k); //(sin(k) / k)-интерполяционным рядом Котельникова
				}

			}
			tmp[i].first = t;
			tmp[i].second = sum;
		}
		return tmp;
	}


	vector<pair<double, double>> discretiz() { 
		vector<pair<double, double>> tmp((this->interval1 - this->interval2) / this->step);
		for (int i = 0; i < tmp.size(); i++) {
			tmp[i].first = this->interval2 + (this->step * i);
			tmp[i].second = U1(tmp[i].first);
		}
		return tmp;
	}


	void Sample_formation() {
		cout << "Ряд Котельникова" << endl;
		fout << fixed << setprecision(15);
		double masdts[] = { 1.5, 1.75, 2, 3, 1000 }; // частоты для дискретизации 
		int size = 5;
		this->f1 = this->F;
		for (int i = 0; i < size; i++) {
			/*1 сформировать выборки отсчетов u(i)[n] (результаты дискретизации)исследуемого сигнала с частотами дискретизации f(i)d равными:*/
				this->step = 1 / (masdts[i] * this->F);
				vector<pair<double, double>>initial_signal = discretiz();
				std::string result = "outFirst";
				result += (char)(49 + i);
				result += ".txt";
				fout.open(result);

				for (auto i : initial_signal) {
					fout << i.first << " " << i.second << "\n";
				}

				fout.close();
				/*рименить ряд Котельникова (1.73) для восстановления исходного
сигнала по его дискретным отсчетам с помощью формулы (1.72).
*/
				std::string result1 = "result";
				vector<pair<double, double>> kotel_sig = kotelnikov(initial_signal, 1 / (10*(masdts[i] * F)));
				//if (i == 1) {
				result1 += (char)(49 + i);
				result1 += ".txt";
				fout.open(result1);
				for (auto i : kotel_sig) {
					fout << i.first << " " << i.second << "\n";
				}
				fout.close();
			
			
	
		}
	}
};


int main() {
	setlocale(LC_ALL, "Russian");
	Labochka1 a;
	a.Sample_formation();
	return 0;
}