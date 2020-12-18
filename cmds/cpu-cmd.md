查看cpu 类型 
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c


查看gpu使用
watch -n 10 nvidia-smi
nvidia-smi -l 1