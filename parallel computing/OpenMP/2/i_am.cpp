#include <omp.h>
#include <iostream>
using namespace std;

int main()
{
	int k;
	cout << "Enter number of threads:\n" ;
	cin >> k;

	cout << ("Only even numbers? y/n\n");
	char type;
	cin >> type;

	#pragma omp parallel num_threads(k)
	{
		if (type == 'y')
		{
			if (omp_get_thread_num() % 2 == 0)
			{
				printf("I am %d thread from %d threads!\n", omp_get_thread_num(), omp_get_num_threads());
			}	
		}
		else
		{
			printf("I am %d thread from %d threads!\n", omp_get_thread_num(), omp_get_num_threads());
		}
			
	}
}
