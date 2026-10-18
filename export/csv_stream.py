"""[synthetic demo] Stream the CSV export in chunks: large dashboards no longer
time out."""


def stream_rows(rows, chunk=5000):
    for i in range(0, len(rows), chunk):
        yield rows[i : i + chunk]
