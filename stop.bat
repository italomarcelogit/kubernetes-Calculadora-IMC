kubectl delete -f yaml-mongo/service.yaml
kubectl delete -f yaml-mongo/deployment.yaml

kubectl delete -f yaml-app/service.yaml
kubectl delete -f yaml-app/deployment.yaml