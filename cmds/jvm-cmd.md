jmap pid
jmap heap pid
jinfo pid
jstat -gc pid
pstree -p pid

jmap -dump:format=b,file=heapdump.phrof pid
jmap -dump:live,format=b,file=heapdump.hprof pid

-XX:-DoEscapeAnalysis -XX:+PrintGC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/mnt/C_0_SSDRAID_0_PART1/jfyin

