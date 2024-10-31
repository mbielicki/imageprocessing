from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_color_arg


def to_one_channel(args, arr):
    assert_only_allowed_args(args, ['--input', '--output', '--channel'])

    colors = arr.shape[2]

    if colors > 1:
        channel = get_color_arg(args, '--channel')
    else:
        channel = 0

    return arr[:, :, channel]
