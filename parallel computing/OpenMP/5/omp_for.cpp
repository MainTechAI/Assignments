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

	#pragma omp parallel num_threads(k) reduction(+:sum)
	{
		#pragma omp for
		for (int i = 1; i <= n; i++) {
			printf("[%d] %d\n", omp_get_thread_num(), i);
			sum += i;
		}

	}

	printf("Sum = %d", sum);

	return 0;
}
