#include <omp.h>
#include <iostream>
using namespace std;

int main()
{
	int n, sum = 0;
	cout << "Sum numbers from 1 to ";
	cin >> n;

	#pragma omp parallel num_threads(2) reduction(+:sum)
	{
		if (omp_get_thread_num() == 0) {
			for (int i = 1; i <= n/2; i++)
			{
				sum += i;
			}
			printf("[%d]: Sum = %d\n", omp_get_thread_num(), sum);
		}
		else{
			for (int i = n/2+1; i <= n; i++)
			{
				sum += i;
			}
			printf("[%d]: Sum = %d\n", omp_get_thread_num(), sum);
		}
	}

	printf("Sum = %d", sum);
}
