#include "mpi.h"
#include <iostream>
using namespace std;


int main(int argc, char* argv[])
{
    MPI_Init(&argc, &argv);

    int buf, rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int count = 1, tag = 0;

    if (rank == 0) {
        buf = 1234;
        MPI_Send(&buf, count, MPI_INT, 1, tag, MPI_COMM_WORLD);
    }
    else if (rank == 1) {
        MPI_Recv(&buf, count, MPI_INT, 0, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("receive message '%d' \n", buf);
    }
 
    MPI_Finalize();
    return 0;
}
