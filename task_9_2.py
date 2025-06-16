import pkg_resources
installed_packages = pkg_resources.working_set

packages_list = sorted(["%s = %s" % (i.key,i.version) for i in installed_packages])

for m in packages_list:
    print(m)

