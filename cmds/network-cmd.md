# net cmd

cat /proc/sys/net/ipv4/tcp_fin_timeout
cat /proc/sys/net/ipv4/ip_local_port_range
cat /proc/sys/net/ipv4/tcp_tw_reuse
cat /proc/sys/net/ipv4/tcp_timestamps

sudo sysctl -w net.ipv4.tcp_fin_timeout=30
sudo sysctl -w net.ipv4.tcp_timestamps=1 
sudo sysctl -w net.ipv4.tcp_tw_reuse=1
sudo sysctl -w net.ipv4.ip_local_port_range="1024 65535"
sudo sysctl -w net.ipv4.tcp_timestamps=1 

cat /proc/sys/net/ipv4/ip_local_port_range
sudo sysctl -w net.ipv4.ip_local_port_range="1024 65535"

netstat -ano|grep TIME_WAIT|wc -l

watch cat /proc/net/dev 


nc -zvw1 18.240.1.100 29000

# tcp dump
apt-get install tcptump
tcpdump -i eno1 -vnn dst host X.X.X.X -n -w ping.pcap

#列出监听的端口列表
netstat -ntl
netstat -tunlp|grep


sudo netstat -tunlp|grep 21