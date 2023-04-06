import os
import sysconfig

torch_path = os.path.join(sysconfig.get_paths()["purelib"], "torch\\lib")
paths = os.environ.get("PATH", "")
if os.path.exists(torch_path):
    print(f"torch found: {torch_path}")
    if torch_path in paths:
        print("torch already set")
    else:
        print("run:")
        os.environ['PATH'] = paths + os.pathsep + torch_path + os.pathsep
        print(f'set Path={paths + os.pathsep + torch_path + os.pathsep}')
else:
    print("torch not found")
