kubectl apply -f yaml-mongo/deployment.yaml
kubectl apply -f yaml-mongo/service.yaml

kubectl apply -f yaml-app/deployment.yaml
kubectl apply -f yaml-app/service.yaml