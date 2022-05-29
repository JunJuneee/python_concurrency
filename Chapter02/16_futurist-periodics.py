import time

from futurist import periodics


@periodics.periodic(1)
def every_one(started_at):
    print("1: %s" % (time.time() - started_at))


@periodics.periodic(4)
def print_stats():
    print("stats: %s" % list(w.iter_watchers()))


w = periodics.PeriodicWorker([
    (every_one, (time.time(),), {}),
    # (print_stats, (), {})
])

# 위에 처럼 추가할 수도 있는데,
# add를 사용하면 그냥 worker에 추가
w.add(print_stats)
w.start()
