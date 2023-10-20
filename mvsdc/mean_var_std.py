import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    np_arr = np.array(list)
    three_dim = np_arr.reshape(3,3)

    # along both axes and when flattened.
    mean_rows = np.mean(three_dim, axis=0)
    mean_cols = np.mean(three_dim, axis=1)
    mean = np.mean(three_dim)

    var_rows = np.var(three_dim, axis=0)
    var_cols = np.var(three_dim, axis=1)
    var = np.var(three_dim)

    std_rows = np.std(three_dim, axis=0)
    std_cols = np.std(three_dim, axis=1)
    std = np.std(three_dim)

    max_rows = np.max(three_dim, axis=0)
    max_cols = np.max(three_dim, axis=1)
    max = np.max(three_dim)

    min_rows = np.min(three_dim, axis=0)
    min_cols = np.min(three_dim, axis=1)
    min = np.min(three_dim)

    sum_rows = np.sum(three_dim, axis=0)
    sum_cols = np.sum(three_dim, axis=1)
    sum = np.sum(three_dim)

    mr = mean_rows.ravel()
    mc = mean_cols.ravel()
    vr = var_rows.ravel()
    vc = var_cols.ravel()
    sr = std_rows.ravel()
    sc = std_cols.ravel()
    mxr = max_rows.ravel()
    mxc = max_cols.ravel()
    mir = min_rows.ravel()
    mic = min_cols.ravel()
    sur = sum_rows.ravel()
    suc = sum_cols.ravel()


    calculations  = {
        'mean': [mr.tolist(), mc.tolist(), mean.tolist()],
        'variance': [vr.tolist(), vc.tolist(), var.tolist()],
        'standard deviation': [sr.tolist(), sc.tolist(), std.tolist()],
        'max': [mxr.tolist(), mxc.tolist(), max.tolist()],
        'min':[mir.tolist(), mic.tolist(), min.tolist()],
        'sum':[sur.tolist(), suc.tolist(), sum.tolist()]
    }

    return calculations