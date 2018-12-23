import unittest
from dbus import sig_iter, decode, decode_variant


class TestDbusSigIterator(unittest.TestCase):

    def test_sig_iterator(self):
        sig = 'bnyaiu'
        self.assertEqual(
            ['b', 'n', 'y', 'ai', 'u'],
            list(sig_iter(sig)),
        )

    def test_sig_iterator_nested_arrays(self):
        sig = 'aiaai'
        self.assertEqual(
            ['ai', 'aai'],
            list(sig_iter(sig)),
        )

    def test_sig_iterator_dict(self):
        sig = 'i{su}ai'
        self.assertEqual(
            ['i', '{su}', 'ai'],
            list(sig_iter(sig)),
        )

    def test_sig_iterator_struct(self):
        sig = 's(iib)au'
        self.assertEqual(
            ['s', '(iib)', 'au'],
            list(sig_iter(sig)),
        )


class TestDbusPDUDecoder(unittest.TestCase):

    def test_decode_basic_type_sequence(self):
        sig = 'ibu'
        pdu = ('9', '0', '45')
        self.assertEqual(
            [9, False, 45],
            decode(sig, pdu),
        )

    def test_decode_variant(self):
        variant = ('b', '1')
        self.assertEqual(
            True,
            decode_variant(variant),
        )
        variant = ('s', 'hello')
        self.assertEqual(
            'hello',
            decode_variant(variant),
        )
        variant = ('ai', ['1', '2'])
        self.assertEqual(
            [1, 2],
            decode_variant(variant),
        )

    def test_decode_variant_in_pdu(self):
        sig = 'vi'
        pdu = (('b', '0'), '45')
        self.assertEqual(
            [False, 45],
            decode(sig, pdu),
        )

        sig = 'vs'
        pdu = (('u', '8768'), 'foo')
        self.assertEqual(
            [8768, 'foo'],
            decode(sig, pdu),
        )

        sig = 'vb'
        pdu = (('as', ['foo', 'bar']), '1')
        self.assertEqual(
            [['foo', 'bar'], True],
            decode(sig, pdu),
        )

    def test_decode_array(self):
        sig = 'ai'
        pdu = ('9', '0', '45')
        self.assertEqual(
            [[9, 0, 45]],
            decode(sig, pdu),
        )

    def test_decode_array_of_strings(self):
        sig = 'as'
        pdu = ('foo', 'bar', 'baz')
        self.assertEqual(
            [['foo', 'bar', 'baz']],
            decode(sig, pdu),
        )

    def test_decode_array_of_arrays(self):
        sig = 'aab'
        pdu = (('0', '1', '1'), ('1', '0', '1'))
        self.assertEqual(
            [[[False, True, True], [True, False, True]]],
            decode(sig, pdu),
        )

    def test_decode_dict(self):
        sig = 'a{su}'
        pdu = (('foo', '45'), ('bar', '668'))
        self.assertEqual(
            [{'foo': 45, 'bar': 668}],
            decode(sig, pdu),
        )
