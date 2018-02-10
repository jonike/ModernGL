import unittest

from moderngl.mgl import fmtdebug


GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_DOUBLE = 0x140A
GL_HALF_FLOAT = 0x140B


class TestBuffer(unittest.TestCase):

    def check(self, fmt, res):
        self.assertEqual(fmtdebug(fmt), res)

    def test_format_1(self):
        self.check('1f', (4, 1, 0, True, ((4, 1, GL_FLOAT, False),)))
        self.check('2f', (8, 1, 0, True, ((8, 2, GL_FLOAT, False),)))
        self.check('3f', (12, 1, 0, True, ((12, 3, GL_FLOAT, False),)))
        self.check('4f', (16, 1, 0, True, ((16, 4, GL_FLOAT, False),)))
        self.check('1i', (4, 1, 0, True, ((4, 1, GL_INT, False),)))
        self.check('2i', (8, 1, 0, True, ((8, 2, GL_INT, False),)))
        self.check('3i', (12, 1, 0, True, ((12, 3, GL_INT, False),)))
        self.check('4i', (16, 1, 0, True, ((16, 4, GL_INT, False),)))
        self.check('1u', (4, 1, 0, True, ((4, 1, GL_UNSIGNED_INT, False),)))
        self.check('2u', (8, 1, 0, True, ((8, 2, GL_UNSIGNED_INT, False),)))
        self.check('3u', (12, 1, 0, True, ((12, 3, GL_UNSIGNED_INT, False),)))
        self.check('4u', (16, 1, 0, True, ((16, 4, GL_UNSIGNED_INT, False),)))

    def test_format_2(self):
        self.check('1f1', (1, 1, 0, True, ((1, 1, GL_UNSIGNED_BYTE, True),)))
        self.check('1f2', (2, 1, 0, True, ((2, 1, GL_HALF_FLOAT, False),)))
        self.check('1f4', (4, 1, 0, True, ((4, 1, GL_FLOAT, False),)))
        self.check('1f8', (8, 1, 0, True, ((8, 1, GL_DOUBLE, False),)))

    def test_format_3(self):
        self.check('1f1f', (0, 0, 0, False, ()))
        self.check('3f3f4i', (0, 0, 0, False, ()))
        self.check('3f 3f 4i', (40, 3, 0, True, ((12, 3, GL_FLOAT, False), (12, 3, GL_FLOAT, False), (16, 4, GL_INT, False))))

    def test_format_4(self):
        self.check('3f 3f /v', (24, 2, 0, True, ((12, 3, GL_FLOAT, False), (12, 3, GL_FLOAT, False))))
        self.check('3f 12x 3f /v', (36, 2, 0, True, ((12, 3, GL_FLOAT, False), (12, 12, 0, False), (12, 3, GL_FLOAT, False))))

    def test_format_5(self):
        # vert, norm, text, color
        self.check(
            '3f 3f 2f 4f1',
            (36, 4, 0, True,
                (
                    (12, 3, GL_FLOAT, False),
                    (12, 3, GL_FLOAT, False),
                    (8, 2, GL_FLOAT, False),
                    (4, 4, GL_UNSIGNED_BYTE, True),
                )
            )
        )

        # vert, norm, text, color
        self.check(
            '3f4 3f4 2f4 4f1',
            (36, 4, 0, True,
                (
                    (12, 3, GL_FLOAT, False),
                    (12, 3, GL_FLOAT, False),
                    (8, 2, GL_FLOAT, False),
                    (4, 4, GL_UNSIGNED_BYTE, True),
                )
            )
        )

        # vert, norm, padding, color
        self.check(
            '3f 3f 2x4 4f1',
            (36, 3, 0, True,
                (
                    (12, 3, GL_FLOAT, False),
                    (12, 3, GL_FLOAT, False),
                    (8, 2, 0, False),
                    (4, 4, GL_UNSIGNED_BYTE, True),
                )
            )
        )

    def test_format_6(self):
        self.check('2f/i', (0, 0, 0, False, ()))


if __name__ == '__main__':
    unittest.main()
