import sys

"""
1080p (Full HD)	24, 25, 30	8 Mbps 8000
1080p (Full HD)	48, 50, 60	12 Mbps 12000
1440p (2K)	24, 25, 30	16 Mbps 16000
1440p (2K)	48, 50, 60	24 Mbps
2160p (4K UHD)	24, 25, 30	35–45 Mbps
2160p (4K UHD)	48, 50, 60
"""

MIN_STREAM_BITRATE: int = 5000
MIN_STREAM_HOURS: int = 1

stream_bitrate: int = 0
stream_hours: int = 0


def data_usage(stream_bitrate: int, stream_hours: int) -> None:
    cal_data_usage(hours_to_seconds(stream_hours), stream_bitrate, stream_hours)


def hours_to_seconds(stream_hours) -> int:

    converted_seconds: int = stream_hours * 60 * 60
    return converted_seconds


def cal_data_usage(
    stream_seconds: int, STREAMING_BITRATE: int, stream_hours: int
) -> None:

    bitratein_mb: int = STREAMING_BITRATE // 1000
    data_usage: int = ((bitratein_mb) * stream_seconds) // 8 / 1000

    print(
        f"To stream for {stream_hours} hour{'s' if stream_hours > 1 else ''}, you would need approx: --> {data_usage} GB"
    )


try:
    stream_bitrate = int(input("Enter the streaming bitrate: "))
    if stream_bitrate < MIN_STREAM_BITRATE:
        raise ValueError(f"Invalid Bitrate!,  Allowed >={MIN_STREAM_BITRATE}")

    stream_hours = int(input("Enter the streaming duration in hours: "))

    if stream_hours < MIN_STREAM_HOURS:
        raise ValueError(f"Minimum  {MIN_STREAM_HOURS} stream duration is required")

    # Kept the else for readability purpose
    else:
        data_usage(stream_bitrate, stream_hours)
except ValueError as val_err:
    print(val_err)


finally:
    sys.exit()
