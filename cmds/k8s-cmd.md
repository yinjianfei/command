kubectl delete pod [pod name] --force --grace-period=0 -n [namespace]

kubectl get nodes --show-labels
kubectl label nodes <node-name> <label-key>=<label-value> 

kubectl label nodes wxeg0059 fp.k8s.machine.Majordomo=true


kubectl exec fp-website-deployment-7496c5fd5b-bdg88 -- sh -c 'printenv'|grep WITCHER