import subprocess


def file_len(fname):
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])


input = "/home/arne/scans/Krater7.zfs.asc.txt"
output = "/home/arne/scans/Krater7.zfs.pcd"

count = file_len(input)




header ="""# .PCD v.7 - Point Cloud Data file format
VERSION .7
FIELDS x y z rgb
SIZE 4 4 4 4
TYPE F F F I
COUNT 1 1 1 1
WIDTH %d
HEIGHT 1
POINTS %d
DATA ascii\n""" % (count, count)

print(header)