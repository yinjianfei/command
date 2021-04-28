kubectl delete pod [pod name] --force --grace-period=0 -n [namespace]

kubectl get nodes --show-labels
kubectl label nodes <node-name> <label-key>=<label-value> 

kubectl label nodes wxeg0059 txwl.k8s.svc.api.master=true

kubectl label nodes fp-master txwl.k8s.svc.nginx.master=true
kubectl label nodes fp-master txwl.k8s.svc.web.master=true
kubectl label nodes fp-master txwl.k8s.svc.api.master=true
kubectl label nodes fp-master txwl.k8s.svc.distributor.master=true

然后分别看下website nginx txwl-api txwl-distributor的 deploy.yml deploy.tpl的nodeSelector是不是带有.master的

$ kubectl describe pod txwl-api-64496d97b-5qdx7|grep Node-Selectors

kubectl port-forward --address=0.0.0.0 kafka-0 39092:9092 -n middlewares


kubectl exec fp-website-deployment-7496c5fd5b-bdg88 -- sh -c 'printenv'|grep WITCHER


curl 'http://10.40.55.182:11180/website/face/v2/login' \
  -H 'Connection: keep-alive' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'timestamp: 1616997978546' \
  -H 'FP-frontend-request-id: 2d708a1a-07b3-4df0-962f-39ad2055971c' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36' \
  -H 'requestId: 161699797854684' \
  -H 'Origin: http://10.40.55.182:11180' \
  -H 'Referer: http://10.40.55.182:11180/fp/login' \
  -H 'Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' \
  -H 'Cookie: currentLanguage=cn; yt_token=eyJtZXRhIjp7ImlzQWR2YW5jZWQiOnRydWV9LCJleHBpcmVzIjoxNjE2OTk4NzI1MTUxfQ==' \
  --data-raw '{"name":"admin","password":"0192023a7bbd73250516f069df18b500"}' \
  --compressed \
  --insecure



ubectl label nodes wxeg0059 fp.k8s.machine.Majordomo=true
beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,fp.k8s.machine.CPU=true,fp.k8s.machine.Lucifron=true,fp.k8s.machine.Majordomo=true,fp.k8s.machine.P4=true,fp.k8s.machine.T4=false,fp.k8s.machine.TF=false,fp.k8s.machine.clean_ragnaros_data=false,fp.k8s.pod.body.retrieve=true,fp.k8s.pod.face.retrieve=true,fp.k8s.pod.vehicle.retrieve=true,fp.k8s.svc.elasticsearch=true,fp.k8s.svc.es=true,fp.k8s.svc.kafka=true,fp.k8s.svc.mongo=true,fp.k8s.svc.mongodb=true,fp.k8s.svc.ragnaros=true,kubernetes.io/arch=amd64,kubernetes.io/hostname=wxeg0081,kubernetes.io/os=linux,node-role.kubernetes.io/master=,servertype=gpu,txwl.k8s.svc.api=true,txwl.k8s.svc.data-docking=true,txwl.k8s.svc.distributor=true,txwl.k8s.svc.flink=true,txwl.k8s.svc.nginx=true,txwl.k8s.svc.product=true,txwl.k8s.svc.subject-repo=true,txwl.k8s.svc.web=true
