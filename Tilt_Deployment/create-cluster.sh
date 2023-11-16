#!/bin/bash

# Here we will set the name for our local cluster
# whatever that my be
CLUSTER_NAME="local-cluster"

# Create a KinD cluster with a local Docker registry
kind create cluster --name "$CLUSTER_NAME" --config - <<EOF
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 5000
    hostPort: 5000
EOF

# Set up the local Docker registry
# Connects the kind registry to the network allowing
docker network connect "kind" "kind-registry"
docker run -d --name "kind-registry" --network "kind" -p "5000:5000" registry:2
