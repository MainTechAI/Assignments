#include <omp.h>
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    #pragma omp parallel num_threads(n)
    {
        printf("[%d]: parallel region (start)\n", omp_get_thread_num());

        #pragma omp sections
        {
            #pragma omp section
            {
                printf("[%d]: came in section 1\n", omp_get_thread_num());
            }
            #pragma omp section
            {
                printf("[%d]: came in section 2\n", omp_get_thread_num());
            }
            #pragma omp section
            {
                printf("[%d]: came in section 3\n", omp_get_thread_num());
            }
        }

        //printf("[%d]: parallel region (end)\n", omp_get_thread_num());

    }

    return 0;
}
