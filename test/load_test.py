import tracemalloc
import linecache
import os

from bandwidth.configuration import Configuration
from bandwidth.api_client import ApiClient

def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print("#%s: %s:%s: %.1f KiB"
              % (index, frame.filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

class LoadTestClient():
    def __init__(self, hostUrl):
        self.config = Configuration(
            host=hostUrl
        )
        self.test_client = ApiClient(configuration=self.config)

    def test_get(self, requests: int) -> None:
        for i in range(requests):
            self.test_client.call_api(
                resource_path='/test/get',
                method='GET'
            )
    
    def test_post(self, requests: int) -> None:
        for i in range(requests):
            self.test_client.call_api(
                resource_path='/test/post',
                method='POST'
            )


tracemalloc.start()

load_test = LoadTestClient(hostUrl='https://d815f3b06d79650d7a886f0c2ce1955d.m.pipedream.net')

load_test.test_get(500)

snapshot = tracemalloc.take_snapshot()
# top_stats = snapshot.statistics('lineno')
display_top(snapshot)

# print("[ Top 10 ]")
# for stat in top_stats[:10]:
#     print(stat)
 
# stopping the library
tracemalloc.stop()

assert(True == False)
