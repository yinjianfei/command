http://docs.yitu-inc.com/nighthawk/rtd/fp-cell/release~2.2.0/in_field.html
http://docs.yitu-inc.com/nighthawk/rtd/opod-cell/1.5.4/rollback.html

https://wiki.yitu-inc.com/pages/viewpage.action?pageId=581234768
http://docs.yitu-inc.com/nighthawk/up/3.1.2/

{
   "hosts": [
     {
       "ip": ["10.40.550.163"],
       "real_ip": ["10.40.550.163"],
       "port": 18022,
       "user": "linuxadmin",
       "pass": "Hello=111!",
       "net_interface": "bond0",
       "netmask":"255.255.255.0",
       "gateway": "10.40.88.1",
       "type": "cpu",
       "master": true
     }
   ],
   "timezone": "Asia/Shanghai",
   "ntp_server": "10.40.550.163",
   "nighthawk_ip":"10.40.57.81",
   "k8s_storage_path": "/mnt/C_0_SSDRAID_0_PART1/pvc",
   "k8s_network_subnet": "18.244.0.0/12",
   "imagefs_available" : "15%",
   "nodefs_available" : "10%",
   "k8s_ha_enabled": false,
   "k8s_registry_urls":  [],
   "virtual_ip_deploy": false
}


{
   "hosts": [
     {
       "ip": ["10.40.88.49"],
       "real_ip": ["10.40.88.49"],
       "port": 18022,
       "user": "linuxadmin",
       "pass": "Hello=111!",
       "net_interface": "bond0",
       "netmask":"255.255.255.0",
       "gateway": "10.40.88.1",
       "type": "cpu",
       "master": true
     },
     {
       "ip": ["10.40.80.51"],
       "real_ip": ["10.40.80.51"],
       "port": 18022,
       "user": "linuxadmin",
       "pass": "Hello=111!",
       "net_interface": "bond0",
       "netmask":"255.255.255.0",
       "gateway": "10.40.80.1",
       "type": "gpu"
     }
   ],
   "timezone": "Asia/Shanghai",
   "ntp_server": "10.40.88.49",
   "nighthawk_ip":"10.40.57.81",
   "k8s_storage_path": "/mnt/C_0_SSDRAID_1_PART1/pvc",
   "k8s_network_subnet": "18.244.0.0/12",
   "imagefs_available" : "15%",
   "nodefs_available" : "10%",
   "k8s_ha_enabled": false,
   "k8s_registry_urls":  [],
   "virtual_ip_deploy": false
}
