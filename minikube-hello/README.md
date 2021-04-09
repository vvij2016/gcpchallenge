# Solution for minikube-hello challenge
Vidushika Vij   
04/08/2021   

## Installing Minikube on my MAC
I followed the steps to install minikube on my Mac.   

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
sudo install minikube-darwin-amd64 /usr/local/bin/minikube
minikube start
```
## Deploy docker container for the app on local minikube
I enabled local docker repository in minikube

```
eval $(minikube docker-env)
```

Using the docker container for the app to local minikube repository

```
minikube image load node:6-alpine
docker build -t hello-node .
```

This created a docker image in my local minikube repository.   

## Kubenetes app deployments
I created a deployment.yaml and service.yaml file to deploy an app using this docker image using the commands

```
kubectl apply -f deployment.yaml
kubectl get pods
kubectl apply -f service.yaml
kubectl get services
```

The app is deployed successfully and running. 

## Creating a configmap
I created a configmap with a key used in deployment.yaml file

```
kubectl create configmap special-config --from-literal=hello.name=Vidushika
```

## Testing the app
For testing the app on my Mac I had to run minikube tunnel command in a seperate terminal window 

```
minikube tunnel
```
and then I am able to see the message

```
curl 10.101.31.227:8080
```
This printed the configmap key defined.   
**Hello Vidushika!**



