%#const tot_exe=10.
%#const num_exe=10.
%#const type=open.

exercise(0..(tot_exe-1)).

num(0..(num_exe-1)).

num_exe {exe_test(type,0..(tot_exe-1),0..(num_exe-1))} num_exe.

:- exe_test(T,N1,M), exe_test(T,N2,M), N1!=N2.

:- exe_test(T,N,M1), exe_test(T,N,M2), M1!=M2.

:- exe_test(T1,N,M), exe_test(T2,N,M), T1!=T2.
