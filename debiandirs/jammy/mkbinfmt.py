# mkbinfmt.py
import importlib.util, sys, os.path

magic = "".join(["\\x%.2x" % c for c in importlib.util.MAGIC_NUMBER])

name = sys.argv[1]

binfmt = '''\
package %s
interpreter /usr/bin/%s
magic %s\
''' % (name, name, magic)

#filename = '/usr/share/binfmts/' + name
#open(filename,'w+').write(binfmt)

sys.stdout.write(binfmt)
sys.stdout.write('\n')
