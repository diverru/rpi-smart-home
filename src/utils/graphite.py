import statsd

from utils.env import Env


class Graphite:
    def __init__(self):
        self._graphite = statsd.StatsClient(
            Env.GRAPHITE_HOST.resolve(), int(Env.GRAPHITE_PORT.resolve())
        )
        self._pipeline = None

    def __enter__(self):
        self._pipeline = self._graphite.pipeline()
        self._pipeline.__enter__()
        return self

    def __exit__(self, *args, **kwargs):
        assert self._pipeline
        self._pipeline.__exit__(*args, **kwargs)
        self._pipeline = None

    def send(self, param, value):
        target = self._pipeline or self._graphite
        target.incr(param, value)

    def send_timing(self, param, value):
        target = self._pipeline or self._graphite
        target.timing(param, value)

    def send_gauge(self, param, value):
        target = self._pipeline or self._graphite
        target.gauge(param, value)
