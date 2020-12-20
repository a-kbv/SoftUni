def pc_parts(usd_cpu=float(input()), usd_gpu=float(input()), usd_ram=float(input()), n_ram=int(input()), discount=float(input())):
    return f"Money needed - {(((usd_cpu * 1.57) * (1 - discount)) + ((usd_gpu * 1.57) * (1 - discount)) + ((usd_ram * 1.57) * n_ram)):.2f} leva."
print(pc_parts())