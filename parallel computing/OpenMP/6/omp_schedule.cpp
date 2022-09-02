#include <omp.h>
#include <iostream>
using namespace std;

int main()
{
    int const k = 4;
    int const n = 10;
    
    int Static[n],  Static1[n],  Static2[n];
    int Dynamic[n], Dynamic2[n];
    int Guided[n],  Guided2[n];


    #pragma omp parallel num_threads(k)
    {
        #pragma omp for schedule(static)
        for (int i = 0; i < n; ++i)
        {
            Static[i] = omp_get_thread_num();
        }
    }

    #pragma omp parallel num_threads(k)
    {
        #pragma omp for schedule(static, 1)
        for (int i = 0; i < n; ++i)
        {
            Static1[i] = omp_get_thread_num();
        }
    }

    #pragma omp parallel num_threads(k)
    {
        #pragma omp for schedule(static, 2)
        for (int i = 0; i < n; ++i)
        {
            Static2[i] = omp_get_thread_num();
        }
    }

    #pragma omp parallel num_threads(k)
    {
        #pragma omp for schedule(dynamic)
        for (int i = 0; i < n; ++i)
        {
            Dynamic[i] = omp_get_thread_num();
        }
    }

    #pragma omp parallel num_threads(k)
    {
        #pragma omp for schedule(dynamic, 2)
        for (int i = 0; i < n; ++i)
        {
            Dynamic2[i] = omp_get_thread_num();
        }
    }

    #pragma omp parallel num_threads(k)
    {
        #pragma omp for schedule(guided)
        for (int i = 0; i < n; ++i)
        {
            Guided[i] = omp_get_thread_num();
        }
    }

    #pragma omp parallel num_threads(k)
    {
        #pragma omp for schedule(guided, 2)
        for (int i = 0; i < n; ++i)
        {
            Guided2[i] = omp_get_thread_num();
        }
    }


    printf("------------------------------------------------------------------------------------------\n");
    printf("| Iteration |                            Schedule parameters                             |\n");
    printf("|   number  | static | static, 1 | static, 2 | dynamic | dynamic, 2 | guided | guided, 2 |\n");
    printf("------------------------------------------------------------------------------------------\n");

    for (int i = 0; i < n; ++i)
    {
        printf("|    %2d     |    %d   |     %d     |     %d     |    %d    |      %d     |    %d   |     %d     |\n",
                 i+1, Static[i], Static1[i], Static2[i], Dynamic[i], Dynamic2[i], Guided[i], Guided2[i]);
    }

    printf("------------------------------------------------------------------------------------------\n");


	return 0;
}
