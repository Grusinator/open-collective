import os
import importlib
from invoke import Collection, Task

def is_task_module(module_name):
    if not module_name.endswith('.py') or module_name == '__init__.py':
        return False

    module_path = os.path.join(os.path.dirname(__file__), module_name)
    spec = importlib.util.spec_from_file_location(module_name[:-3], module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name, value in module.__dict__.items():
        if isinstance(value, Task):
            return True

    return False

task_files = [f for f in os.listdir(os.path.dirname(__file__)) if is_task_module(f)]
modules = [importlib.import_module(f'tasks.{f[:-3]}') for f in task_files]

ns = Collection()

for module in modules:
    for name, value in module.__dict__.items():
        if isinstance(value, Task):
            ns.add_task(value)