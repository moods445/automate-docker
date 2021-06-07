import logging
import os
import platform
import subprocess

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)

#  获取配置文件


def config():
    configfile = ".gitautomate"
    if "Windows" == platform.system():
        return os.environ['HOME'] + "\\" + configfile
    else:
        return os.environ['HOME'] + "/" + configfile


def run(cmd, dir):
    st = subprocess.run(cmd, capture_output=True, cwd=dir)
    if st.returncode != 0:
        logging.error('exec %s error in %s : %s', cmd, dir, st.stderr)
    return st


if not os.path.isfile(config()):
    open(config(), "w")

encoding = "GBK"
f = open(config(), "r")
logging.info("reading configuration from %s", config())
lines = f.readlines()
if len(lines) == 0:
    logging.info("nothing to auto commit")
    exit()
for p in lines:
    dir = p.strip("\n").strip("\r")
    logging.info("handle %s", dir)
    st = run("git status", dir)
    if "working tree clean" not in st.stdout.decode(encoding):
        run("git add .", dir)
    if "nothing to commit" not in st.stdout.decode(encoding):
        run("git commit -m \"add automate\"", dir)
    run("git push", dir)
    subprocess.run("git status",  cwd=dir)

logging.info("push all")
