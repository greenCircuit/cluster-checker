from kubernetes import client, config
import json

# Configs can be set in Configuration class directly or using helper utility
try:
    config.load_kube_config()
except:
    config.load_incluster_config()

v1 = client.CoreV1Api()
api = client.CustomObjectsApi()

# status struct that holds status of k8s objects
class Status:
    def __init__(self, name, ns, status, condition, object):
        self.name = name
        self.ns = ns
        self.status = status
        self.condition = condition
        self.object = object

    def __str__(self):
        return (f"Name: {self.name}, Namespace: {self.ns}, Status: {self.status}, Condition: {self.condition}")
    
    def __dict__(self):
        return {
            "name": self.name,
            "namespace": self.ns,
            "status": self.status,
            "condition": self.condition
        }


def string_status(statuses):
    return [obj.__str__() for obj in statuses]

def json_status(statuses):
    converted =  [obj.__dict__() for obj in statuses]
    return json.dumps({ "failed": converted })


# get all pods inside cluster
def get_all_pods():
    fail_pods = []
    pass_pods = []
    pods = v1.list_pod_for_all_namespaces(watch=False)
    for pod in pods.items:
        pod_status = Status(pod.metadata.name, pod.metadata.namespace, bool(pod.status.conditions[0].status), "", "pod")
        if pod_status.status == True:
            pass_pods.append(pod_status)
        else:
            fail_pods.append(pod_status)

    return {"pass": pass_pods, "fail": fail_pods}



def get_crs(group, version, plural, ns):
    fail_obj = []
    pass_obj = []

    crs = api.list_namespaced_custom_object(group, version, ns, plural)
    for cr in crs["items"]:
        condition = cr["status"]["conditions"][0]
        status = bool(condition.get("status"))
        message = condition.get("message")
        status = Status(cr["metadata"]["name"], cr["metadata"]["namespace"], status, message, plural) 
        status.__str__()
        if status.status == True:
            pass_obj.append(status)
        else:
            fail_obj.append(status)
    return {"pass": pass_obj, "fail": fail_obj}


x = get_crs("helm.toolkit.fluxcd.io",  "v2",  "helmreleases",  "flux-system")
print(string_status(x["pass"]))