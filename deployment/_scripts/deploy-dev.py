import subprocess

p = subprocess.Popen(['kubectl', 'kustomize', 'overlays/dev'], stdout=subprocess.PIPE)
text = p.communicate()[0].decode("utf-8")

print(text)
