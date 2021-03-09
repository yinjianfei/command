http://prometheus-prometheus-oper-prometheus:9090/prometheus/

kubectl port-forward --address=0.0.0.0 prometheus-prometheus-oper-operator-fb558979d-n7blq 19090:9090 -n monitor

curl '10.105.56.117:9090/prometheus/api/v1/labels'
curl -g 'http://localhost:9090/api/v1/series?'

curl http://10.105.56.117:9090/prometheus/api/v1/targets

curl 'http://10.105.56.117:9090/prometheus/api/v1/targets?state=active'
curl -G http://10.105.56.117:9090/prometheus/api/v1/targets/metadata?metric=witcher
    --data-urlencode 'metric=witcher' 



kubectl -n monitor get secret prometheus-prometheus-prometheus-oper-prometheus -ojson |jq -r '.data["prometheus.yaml.gz"]'|base64 -d| gunzip|grep witcher




## paas dashboard

apiVersion: v1
kind: ConfigMap
metadata:
  labels:
    app: prometheus-operator-grafana
    chart: prometheus-operator-6.11.0
    grafana_dashboard: "1"
    heritage: Tiller
    prometheus: kube-prometheus
    release: prometheus
  name: dashboard-grafana-spring-boot-monitor
  namespace: monitor
data:
  grafana_spring_boot_monitor.json: |
    {{ .Files.Get "config/grafana/grafana_spring_boot_monitor.json" | trim | nindent 4}}