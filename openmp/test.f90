      program VEC_ADD_DO

      INTEGER N, CHUNKSIZE, CHUNK, I
      
      integer nthreads,tid, OMP_GET_NUM_THREADS, OMP_GET_THREAD_NUM  

      PARAMETER (N=100000) 

      PARAMETER (CHUNKSIZE=1000) 

      REAL*8 A(N), B(N), C(N)

!     Some initializations
      DO I = 1, N
        A(I) = I * 1.0
        B(I) = A(I)
      ENDDO

      CHUNK = CHUNKSIZE
        
!$OMP PARALLEL SHARED(A,B,C,CHUNK) PRIVATE(I,tid, NTHREADS)

      tid = OMP_GET_THREAD_NUM() 
      
      if (tid == 0) then 
        NTHREADS = OMP_GET_NUM_THREADS()
        write(*,*) 'Number of threads =', nthreads
      endif 

      do j=1,100
!$OMP DO SCHEDULE(static,CHUNK)
      DO I = 1, N
         C(I) = A(I)*A(i)/B(I)/B(i)/B(i)
      ENDDO
!$OMP END DO NOWAIT
      enddo 


!$OMP END PARALLEL

      END

