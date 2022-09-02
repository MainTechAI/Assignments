#include <omp.h>
#include <iostream>
using namespace std;

int main()
{
	int n, k, t, l, r, range, sum = 0;
	cout << "Number of threads = ";
	cin >> k;
	cout << "Sum numbers from 1 to ";
	cin >> n;

	#pragma omp parallel num_threads(k) reduction(+:sum) private(t,l,r,range)
	{
		t = omp_get_thread_num() + 1;

		if (n % k == 0) {
			range = n / k;
			l = 1 + (range * (t-1)); 
			r = l + range;
			// DEBUG
			//printf("[%d] l=%d, r=%d\n", t-1, l, r); 
			
			for (int i = l; i < r; i++)
			{
				sum += i;
			}
			printf("[%d]: Sum = %d\n", omp_get_thread_num(), sum);

		}
		else{
			range = (n / k) + 1;
			l = 1 + (range * (t - 1));
			r = l + range; if (r > n + 1) r = n + 1;
			// DEBUG
			//printf("[%d] l=%d, r=%d\n", t-1, l, r); 

			for (int i = l; i < r; i++)
			{
				sum += i;
			}
			printf("[%d]: Sum = %d\n", omp_get_thread_num(), sum);
		}
	}

	printf("Sum = %d", sum);


	return 0;
}
