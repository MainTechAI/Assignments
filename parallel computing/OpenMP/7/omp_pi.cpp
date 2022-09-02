#include <omp.h>
#include <iostream>
using namespace std;

int main()
{
    int n;
    double part = 0.0;
    cin >> n;
   
    #pragma omp parallel reduction(+:part) 
    {
        #pragma omp for
        for (int i = 0; i < n; i++)
        {
            double x = (i + 0.5) / n;
            part += 4 / (1 + (x * x));
            //printf("[%d][%d] %f\n", i,omp_get_thread_num(),part );
        }
    }

    cout.precision(15);
    cout << fixed << part / n << endl;

    return 0;
}
