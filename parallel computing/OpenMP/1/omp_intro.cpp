#include <omp.h>
#include <iostream>
using namespace std;

int main()
{
	omp_set_num_threads(6);

	#pragma omp parallel num_threads(4)
	{ 
		printf("Hello World!\n"); 
	}


}

