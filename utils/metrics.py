import time


def measure_latency(
    model_function,
    messages
):

    start = time.time()

    response = model_function(
        messages
    )

    latency = round(
        time.time() - start,
        2
    )

    return response, latency