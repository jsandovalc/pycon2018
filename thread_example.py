import time
from twisted.internet import reactor, threads, defer

# To be executed in thread, not coroutine.
def do_long_calculation():
    time.sleep(3)
    return 3

@defer.inlineCallbacks
def print_result():
    # Await thread temination
    x = yield threads.deferToThread(do_long_calculation)
    print(x)

print_result().addCallback(lambda ign: reactor.stop())
reactor.run()
