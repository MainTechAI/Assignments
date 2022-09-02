#include <omp.h>
#include <iostream>
using namespace std;

int main()
{
    omp_set_num_threads(4);

    int n;
    cin >> n;
    int val;

    int** a = new int* [n];
    for (int i = 0; i < n; ++i)
        a[i] = new int[n];

    int** b = new int* [n];
    for (int i = 0; i < n; ++i)
        b[i] = new int[n];
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> val;
            a[i][j] = val;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> val;
            b[i][j] = val;
        }
    }

    int** c = new int* [n];
    for (int i = 0; i < n; ++i)
        c[i] = new int[n];

    
    #pragma omp parallel
    {
        #pragma omp for
        for (int i = 0; i < n; i++) {
            for (int m = 0; m < n; m++) {
                int sum = 0;
                for (int j = 0; j < n; j++) {
                    sum += a[i][j] * b[j][m];
                    //printf("%d %d %d - %d \n", i, m, j, omp_get_thread_num());
                }
                c[i][m] = sum;
            }
        }
    } 


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << c[i][j] << " ";
        }
        cout << endl;
    }


    return 0;
}