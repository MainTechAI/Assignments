#include <omp.h>
#include <iostream>
using namespace std;

int main()
{
	int n, k, sum = 0;
	cout << "Number of threads = ";
	cin >> k;
	cout << "Sum numbers from 1 to ";
	cin >> n;

	#pragma omp parallel num_threads(k) 
	{
		#pragma omp for
		for (int i = 1; i <= n; i++) {
			#pragma omp atomic
			sum += i;
		}
	}

	printf("Sum = %d", sum);

	return 0;
}
