import sys

# appending to python path so can import files outside 
def append_path():
    sys.path.append("../")
    sys.path.append("../../")
    # where to find python files if running inside pod
    sys.path.append("/app/")
    sys.path.append("/app/tests")
    sys.path.append("/app/tests/health")
append_path()
