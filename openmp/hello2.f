      program main

      use omp_lib
      
      implicit real*8(a-h,o-z)

      wtime = omp_get_wtime()
      write(*,*) '  Available processors: ', omp_get_num_procs()
      write(*,*) '  Available threads     ', omp_get_max_threads()
      write(*,*) '  Threads in use        ', omp_get_num_threads()
!$omp parallel private ( id )
        id = omp_get_thread_num()
        write(*, *) 'Hello from process', id
        if ( id == 0 ) then
          write(*,*) '  Threads in use ', omp_get_num_threads()
        end if
!$omp end parallel
        wtime = omp_get_wtime() - wtime
        write(*,*) ' Wtime = ', wtime
      stop 
      end
