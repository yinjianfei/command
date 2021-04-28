# jmeter

../apache-jmeter-5.2.1/bin/jmeter -n -t meta-large-small.jmx -JthreadNum=20 -Jduration=100 -JconfigFile=parameters/param.csv -Jhost=10.40.88.49 -Jport=30084 -Jasync=true


../apache-jmeter-5.2.1/bin/jmeter -n -t meta.jmx -JthreadNum=1 -Jduration=10 -JconfigFile=parameters/param.csv -Jhost=127.0.0.1 -Jport=30084 -Jasync=true

../apache-jmeter-5.2.1/bin/jmeter -n -t alert_realtime.jmx  -Jduration=10000    