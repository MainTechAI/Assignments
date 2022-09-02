#include <omp.h>
#include <iostream>
using namespace std;

int main()
{
    int n;
    double part = 0.0, start, end;
    cin >> n;



    // Reduction
    start = omp_get_wtime();
    #pragma omp parallel reduction(+:part) 
    {
        #pragma omp for
        for (int i = 0; i <= (n - 1); i++)
        {
            double x = (i + 0.5) / n;
            part += 4 / (1 + (x * x));
        }
    }
    end = omp_get_wtime();

    cout.precision(17);
    cout << fixed << part / n << endl;
    cout.precision(3);
    cout << "(reduction) Time elapsed: " << fixed << end - start << endl;



    // Critical
    part = 0.0;
    start = omp_get_wtime();
    #pragma omp parallel
    {
        #pragma omp for
        for (int i = 0; i <= (n - 1); i++)
        {
            double x = (i + 0.5) / n;

            #pragma omp critical
            {
                part += 4 / (1 + (x * x));
            }
            
        }
    }
    end = omp_get_wtime();

    cout.precision(3);
    cout << "(critical) Time elapsed: " << fixed << end - start << endl;



    return 0;
}
