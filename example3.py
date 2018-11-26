# using BertClient in multicast way

import sys
import threading

from service.client import BertClient


def client_clone(id, idx):
    bc = BertClient(port=int(sys.argv[1]), port_out=int(sys.argv[2]), identity=id)
    for j in bc.listen():
        print('clone-client-%d: received %d x %d' % (idx, j.shape[0], j.shape[1]))


if __name__ == '__main__':
    bc = BertClient(port=int(sys.argv[1]), port_out=int(sys.argv[2]))
    # start two cloned clients sharing the same identity as bc
    for j in range(2):
        t = threading.Thread(target=client_clone, args=(bc.identity, j))
        t.start()

    with open('README.md') as fp:
        data = [v for v in fp if v.strip()]

    for _ in range(3):
        bc.encode(data)
