#include "omp.h"
#include <iostream>

#define CHUNKSIZE 100
#define N     1000

main ()  {

  int i, chunk, tid,nthreads;

  float a[N], b[N], c[N];
  
  /* Some initializations */
  for (i=0; i < N; i++)
    a[i] = b[i] = i * 1.0;
  
  chunk = CHUNKSIZE;
  
#pragma omp parallel shared(a,b,c,chunk) private(i,tid) 
  {

  tid = omp_get_thread_num();

  if (tid == 0) {

    nthreads = omp_get_num_threads();
    std::cout<<"Number of threads ="<<nthreads<<std::endl;
	    
  }

  #pragma omp for schedule(dynamic,chunk) nowait
    for (i=0; i < N; i++)
      c[i] = a[i] + b[i];
  
    }  /* end of parallel section */

}
