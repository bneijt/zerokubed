import time
import zmq
import arrow

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    print("%s: waiting" % str(arrow.get()), flush=True)
    message = socket.recv()
    print("%s: Received request: %s" % (str(arrow.get()), message), flush=True)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"OK")
