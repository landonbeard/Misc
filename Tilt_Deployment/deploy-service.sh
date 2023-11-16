#!/bin/bash

# Install and configure Tilt if not already done
tilt ci init

# Create a Tiltfile for the project
# includes the path to you dockerfile
# kubernetes_yaml refrences a kubernetes.yaml for resource definitions for the app
# kubernetes_resource specifies a kube resource with the name and port settings
# which allows service for 8081
cat <<EOF > Tiltfile
local_docker_build(
    'tilt-app',
    '.',
    dockerfile='./Dockerfile',
)

kubernetes_yaml('kubernetes.yaml') 

kubernetes_resource(
    'tilt-app',
    resource_name='tilt-app',
    port_forwards=8081,
    local='8081',
)

EOF

# Start Tilt to deploy the service
tilt up
