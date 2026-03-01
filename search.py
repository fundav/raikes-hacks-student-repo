import os
for root, dirs, files in os.walk('student-dummy-repo/src'):
    for file in files:
        if file.endswith('.py'):
            path = os.path.join(root, file)
            content = open(path).read()
            if '.get_member' in content:
                print(f"{path}: {content.count('.get_member')}")
