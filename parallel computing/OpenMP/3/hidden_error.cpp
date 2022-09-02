#include <omp.h>
#include <iostream>
#include <windows.h>
using namespace std;

int main()
{
	int rank, k;
	cout << "Enter number of threads:\n";
	cin >> k;

	#pragma omp parallel num_threads(k) private(rank)
	{
		//printf("Thread %d started\n", omp_get_thread_num());
		rank = omp_get_thread_num();
		printf("I am %d thread.\n", rank);
	}
}
