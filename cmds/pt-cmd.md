# 压测命令
sudo mount -t nfs 10.40.46.23:/mnt/WXEC0018 /mnt/WXEC0018
https://wiki.yitu-inc.com/pages/viewpage.action?pageId=547095220
## 准备数据

/mnt/WXEC0018

prepare/prepare_tool_215/prepare_image_flow/这个目录下执行
python3 prepare_image_flow.py 10.40.88.49
sudo python3 Create_Imageflow_Device.py 10.40.88.182
## 执行脚本
sudo python3 Create_Imageflow_Device.py 10.40.88.182
sudo python3 Create_Imageflow_Device.py 10.40.55.163
~/fpsaber/test/test_tool_215/image_flow_test
./.pyenv/versions/3.7.1/bin/python3.7 face_batchImport_7030_aio.py 10.40.88.182 admin admin123 280 900 face_image scenario_image

建库
sudo ../image_flow_test/.pyenv/versions/3.7.1/bin/python3.7 image_loader_test.py 10.40.88.182 40 0

汇聚 meta
python3 image_flow_sendfeature_face_9060_auto.py 10.40.88.49 admin admin123 2000 90 /mnt/WXEC0018/data/others_1w

./.pyenv/versions/3.7.1/bin/python3.7 image_flow_sendfeature_face_7030_auto.py 10.40.88.182 admin admin123 285 900 /mnt/WXEC0018/data/others_1w scenario_image

汇聚人脸人体 大d小图
./.pyenv/versions/3.7.1/bin/python3.7  image_flow_sendfeature_facebody_7030_auto.py 10.40.88.182 admin admin123 285 900 /mnt/WXEC0018/data/others_1w scenario_image


 ../image_flow_test/.pyenv/versions/3.7.1/bin/python3.7 retrieval_face_auto.py 10.40.88.182 admin admin123 2 90 /mnt/WXEC0018/data/others_1w 18

 ../image_flow_test/.pyenv/versions/3.7.1/bin/python3.7 retrieval_track_backend_auto.py 10.40.88.182 admin admin123 1 900 /mnt/WXEC0018/data/others_1w 18
 
 /yitu/hobbit_data/jfyin/ssd/pvc_storage




python3 lsk_feature_import.py 10.40.88.49 5000000

sudo retrieval_face_auto.py 10.40.88.49 admin admin123 20 90 /mnt/WXEC0018/data/others_1w 18



python3 image_flow_longtcp_auto.py 10.40.88.49 admin admin123 100 90 /mnt/WXEC0018/data/others_1w 

python3 face_batchImport_9060_aio.py 10.40.88.49 admin admin123 700 90 face_image scenario_image

python3 image_flow_sendfeature_face_9060_auto.py 10.40.88.49 admin admin123 285 900 /mnt/WXEC0018/data/others_1w scenario_image

python3 retrieval_track_backend_auto.py 10.40.88.49 admin admin123 1 900 /mnt/WXEC0018/data/others_1w 18