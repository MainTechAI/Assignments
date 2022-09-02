#include "mpi.h"
#include <iostream>
using namespace std;


int main(int argc, char* argv[])
{
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    //printf("[%d/%d] started!\n", rank, size);

    int buf=0;
    int count = 1, tag = 0;
    
    if (rank == 0) {
        MPI_Send(&buf, count, MPI_INT, 1, tag, MPI_COMM_WORLD);
        printf("[%d] send 1st message - '%d' \n", rank, buf);
        MPI_Recv(&buf, count, MPI_INT, size-1, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("[%d] receive final message - '%d' \n", rank, buf);
    }
    else {
        MPI_Recv(&buf, count, MPI_INT, rank - 1, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        buf++;
        printf("[%d] receive message '%d' \n", rank, buf);
        if (rank == size - 1) {
            MPI_Send(&buf, count, MPI_INT, 0, tag, MPI_COMM_WORLD);
        }
        else {
            MPI_Send(&buf, count, MPI_INT, rank + 1, tag, MPI_COMM_WORLD);
        }
    }

    MPI_Finalize();
    
    return 0;
}
