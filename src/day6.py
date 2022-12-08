from collections import deque
from typing import List

import utils.io


def find_end_of_first_distinct_seq(data: List[str], seq_len: int) -> int:
    marker_start = None

    # Buffer contains all but last char in sequence
    buffer = deque(data[0 : seq_len - 1], maxlen=seq_len - 1)
    for ind, d in enumerate(data[seq_len - 1 :]):
        # If new char not in buffer and buffer has no repeating items, we're done
        if d not in buffer:
            if len(set(buffer)) == seq_len - 1:
                marker_start = ind + seq_len
                break
        buffer.append(d)
    return marker_start


if __name__ == "__main__":
    data = utils.io.read_file_lines("input/day6")[0]

    print("Part I")
    print(find_end_of_first_distinct_seq(data, 4))

    print("Part II")
    print(find_end_of_first_distinct_seq(data, 14))
