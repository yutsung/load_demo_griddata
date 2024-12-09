import numpy as np


def load_0p01d_data(data_path='.'):
    t2m = np.fromfile(f'{data_path}/t2m_binary_f4.bin', 'f4').reshape(581, 701)
    u10 = np.fromfile(f'{data_path}/u10_binary_f4.bin', 'f4').reshape(581, 701)
    v10 = np.fromfile(f'{data_path}/v10_binary_f4.bin', 'f4').reshape(581, 701)
    tp  = np.fromfile(f'{data_path}/tp_binary_f4.bin',  'f4').reshape(581, 701)
    return tp*1000, t2m-273.15, u10, v10, np.sqrt(u10**2 + v10**2)


if __name__ == '__main__':
    tp, t2m, u10, v10, ws10 = load_0p01d_data()