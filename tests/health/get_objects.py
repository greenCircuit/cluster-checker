from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
v1 = client.CoreV1Api()

# status struct that holds status of k8s objects
class Status:
    def __init__(self, name, ns, status, condition):
        self.name = name
        self.ns = ns
        self.status = status
        self.condition = condition

    def __str__(self):
        return("%s\t%s\t%s" % (self.name, self.ns, self.status, self.condition))


# get all pods inside cluster
def get_all_pods():
    fail_pods = []
    pass_pods = []
    pods = v1.list_pod_for_all_namespaces(watch=False)
    for pod in pods.items:
        pod_status = Status(pod.metadata.name, pod.metadata.namespace, bool(pod.status.conditions[0].status), "")
        if pod_status.status == True:
            pass_pods.append(pod_status)
        else:
            fail_pods.append(pod_status)

    return {"pass": pass_pods, "fail": fail_pods}


