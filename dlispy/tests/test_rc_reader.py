from io import BytesIO

from ..RCReader import readByRC, readByRC_vectorized


def test_vectorized_sshorts_use_one_byte_representation():
    payload = bytes((0x01, 0xFE, 0x7F))

    result = readByRC_vectorized(12, BytesIO(payload), 3)

    assert result.tolist() == [1, -2, 127]


def test_vectorized_ushorts_use_one_byte_representation():
    payload = bytes((0x01, 0xFE, 0xFF))

    result = readByRC_vectorized(15, BytesIO(payload), 3)

    assert result.tolist() == [1, 254, 255]


def test_vectorized_short_widths_match_scalar_reader():
    for code, payload in ((12, bytes((0x80,))), (15, bytes((0xFF,)))):
        scalar = readByRC(code, BytesIO(payload))
        vectorized = readByRC_vectorized(code, BytesIO(payload), 1)

        assert vectorized.tolist() == [scalar]
