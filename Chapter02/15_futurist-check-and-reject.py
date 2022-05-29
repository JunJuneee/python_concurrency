import futurist
from futurist import rejection
import random


def compute():
    return sum(
        [random.randint(1, 100) for i in range(1000000)])


with futurist.ThreadPoolExecutor(
        max_workers=8,
        # 작업 거부 가능
        # 메모리 오버플로를 피하기 위해 큐의 최대 크기를 제한
        check_and_reject=rejection.reject_when_reached(16)) as executor:
    futures = [executor.submit(compute) for _ in range(20)]
    # 통계 기능 제공
    # <ExecutorStatistics object at 0x10542eb00 (failures=0, executed=20, runtime=123.10, cancelled=0)>
    print(executor.statistics)

results = [f.result() for f in futures]
print(executor.statistics)

print("Results: %s" % results)
