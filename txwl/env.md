KV
> ssh linuxadmin@10.40.46.26 -p 18022 
fp
> ssh linuxadmin@10.40.55.163 -p 18022
ragnaros
> ssh yituadmin@10.40.86.174 -p 18022    Yitu@123

kv 10.40.40.122
kv 10.40.88.113

   {
      # FP Node 的 IP 列表, 可以有多台
      "ip": ["10.40.86.174"],
      # 选填，如果不设置服务器的ip则不需要填写
      "real_ip": ["192.168.1.3-6"],
      # 端口,选填，默认是18022
      "port" : 18022,d
      # 账号，选填，默认是 yituadmin
      "user": "yituadmin",
      # 密码, 必填
      "pass": "Yitu@123",
      # 物理网卡名称，设置虚拟ip时需要绑定的网卡名
      "net_interface": "eth0",
      # k8s 集群下机器所属子网的子网掩码,ntp服务会用到,选填,默认值是 255.255.255.0
      "netmask":"255.255.255.0",
      # 选填，所有机器的网关， 如果不设置服务器的ip则不需要填写
      "gateway": "192.168.1.1",
      # 标明服务器的类型,可以为gpu,cpu
      "type": "gpu"
    }

    kubectl label nodes wxeg0102 fp.k8s.machine.Lucifron=true
    kubectl label nodes wxeg0102 fp.k8s.machine.Majordomo=true
    kubectl label nodes wxeg0102 fp.k8s.machine.Lucifron-
wxeg0010
    kubectl label nodes wxeg0010 fp.k8s.machine.Lucifron=true
    kubectl label nodes wxeg0010 fp.k8s.machine.Majordomo=true

    
    python3 image_flow_longtcp_auto.py 10.40.46.26 admin admin123 10 600 /mnt/WXEC0018/data/others_1w



kubectl describe pod xxx | grep qos -i