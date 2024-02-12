def check_cpu_constrained():
    """Returns True if the CPU is having too much usage, False otherwise."""
    return psutil.cpu_percent(1) > 75
