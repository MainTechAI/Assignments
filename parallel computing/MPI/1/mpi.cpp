#include "mpi.h"
#include <iostream>
using namespace std;


int main(int argc, char* argv[])
{
    int random_variable=5;
    printf("Start!\n");
    // Initialize the MPI execution environment 
    MPI_Init(&argc, &argv);

    int rank;
    // Determines the rank of the calling process in the communicator 
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int size;
    // Determines the size of the group associated with a communicator
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    printf("I am %d process from %d processes!\n", rank, size);

    // Terminates MPI execution environment 
    MPI_Finalize();

    printf("End!\n");

    return 0;
}
