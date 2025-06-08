# About 
Run test against cluster to see if k8s objects are in ready state. Send slack notification the results of tests \
Tests are run inside k8s cronjob, but can also can run locally

# Use case
Wanted to send daily notifications with the state of my cluster. Don't go to grafana or run kubectl commands to make sure my services are working

# Usage
## Install
- requirements.txt have all python dependencies
- `./scripts/buildIms.sh builds imgs and upload to registry, will need to modify parts of the script to point to your registry

## Usage
- `./scripts/enrypoint.sh` will run tests
- need to have KUBECONFIG env variable if want to run outside cluster
- inside cluster use service account to communicate with cluster
- `helm upgrade --install --create-namespace robot -n services .`


## Why use this
### Why no grafana alerts based on prometheus metrics
- Wanted to capture status fields of objects so notifications would include why things are failing
- Wanted to send notifications that verify that things are working in case alerting is wrong
- Provide nicer dashboard hos things are working
![report](https://github.com/greenCircuit/cluster-checker/blob/main/imgs/report.png?raw=true)

## TODO
send request to endpoints to verify that thing are working. Will add endpoints to Values.yaml file so don't hard code any urls