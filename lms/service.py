import sys, os, pkg_resources, string

def main():
    if not os.path.isdir("/etc/init.d"):
        print("This system may not be using SysVinit")
        sys.exit(1)

    with open(pkg_resources.resource_filename(__name__, 'data/init'), "r") as init_script:
        with open("/etc/init.d/lms", "w") as f:
            f.write(init_script.read())

    os.chmod("/etc/init.d/lms", 0o755)

    with open(pkg_resources.resource_filename(__name__, 'data/init.config'), "r") as init_config:
        with open("/etc/default/lms", "w") as f:
            f.write(string.Template(init_config.read()).substitute({
                "TARGET" : os.path.abspath(sys.argv[2]),
                "ARGS" : " ".join(sys.argv[3:]),
                "USER" : sys.argv[1]
            }))

    print("Enable Autostart: sudo update-rc.d lms defaults")
    print("Disable Autostart: sudo update-rc.d -f lms remove")
