import numpy as np

from cli.allowed_args import assert_only_allowed_args


def mse(args: dict, input_im: np.ndarray, ref_im: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input', '--reference'])

    x = ref_im.copy()

    x -= input_im
    x **= 2

    mse = np.mean(x)

    return f"Mean Square Error: {mse:.2f}"

def pmse(args: dict, input_im: np.ndarray, ref_im: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input', '--reference']) 

    x = ref_im.copy().astype(np.float64)

    x -= input_im
    x **= 2
    x /= np.max(ref_im) ** 2

    pmse = np.mean(x)

    return f"Peak Mean Square Error: {pmse:.4f}"

def snr(args: dict, input_im: np.ndarray, ref_im: np.ndarray) -> str:
    pass

def psnr(args: dict, input_im: np.ndarray, ref_im: np.ndarray) -> str:
    pass

def md(args: dict, input_im: np.ndarray, ref_im: np.ndarray) -> str:
    pass