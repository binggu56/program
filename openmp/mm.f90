      program main

      use omp_lib
      
      implicit real*8(a-h,o-z)

      integer*4, parameter :: N=600

      real*8 A(N,N),B(N,N),C(N,N)

      wtime = omp_get_wtime()

      write(*,*) '  Available processors: ', omp_get_num_procs()
      write(*,*) '  Available threads     ', omp_get_max_threads()
!      write(*,*) '  Threads in use        ', omp_get_num_threads()

      
      !$omp parallel do 
      do i=1,N
!        !$omp parallel do 
        do j=1,N
          a(i,j) = 1d0
          b(i,j) = 4d0
          c(i,j) = a(i,j)+b(i,j)
        enddo
!        !$omp end parallel do
      enddo
      !$omp end parallel do
      

        wtime = omp_get_wtime() - wtime
        write(*,*) ' Wtime = ', wtime
        write(*,*) ' Matrix C =', (c(1,j),j=1,4)
      stop 
      end
