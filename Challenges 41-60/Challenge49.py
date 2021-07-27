import unittest


def is_anagram(string_a: str, string_b: str) -> bool:
    string_a = list(string_a.lower())
    string_b = list(string_b.lower())
    string_a.sort()
    string_b.sort()
    return string_a == string_b  # Put your code here!!!


class TestIsAnagram(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_anagram('cristian', 'Cristina'))

    def test_2(self):
        self.assertTrue(is_anagram('Dave Barry', 'Ray Adverb'))

    def test_3(self):
        self.assertFalse(is_anagram('Nope', 'Note'))

    def test_4(self):
        self.assertFalse(is_anagram('Apple', 'Appeal'))

    def test_5(self):
        self.assertTrue(is_anagram('', ''))

    def test_6(self):
        a = (
            "tITFzWyQIHWJPCnUOvSSURnSeFxWTo EIpsKmjoRTVgoVfNoipJqMPAKOcLpDCHQFCLIcmBWyjPNgUpuhwZxAxaxyLqVqtZJPburcvljvE"
            "AfbbRxdpJxBQfqaTfJMPGOGWADty GNqZT o SOAUVQYEYhxCYMiVYlSCTWMkXqlzdyeFJAeKQe XyEVahKjinxMMqDLXytXoMfGSrTHci"
            "CwofGZOwoKBuzlJxugya NgEEChGTtlVnPTLaObTYjZYYQ AIgixgJgazYZHrtKaEAtsifWwFrKXuOWZlEdqy Ne HWZBvpTRFAsXQKrrm"
            "xvwhLkgfObFZUKifKugFWFAlfkmjHxbtDIFaoTeOFOogdtUSuU TDwDWkPrkuMZcIuVU ksDywLBKdfWzopxuwLZvaQncUvqfxLkNwpKTu"
            "qSwqtrTpAxWDnSIuBgQYNKKSuHzfuDfXjLTQZrIVxhiIRXieVOtuLl lBpLahhJDOTSdQibMzfW vFkNNhWcOjMMV AZMhomYQqvPmEpln"
            "FUmVL  ocPwzqeCcMLmzuJzIWHHFiLUvPTZTtel IMKGnDyfTJHQHnOfHFRaQiafTV EyujnDNHBRHtqipFwTksIj PsUuJVkDtMsjNoKg"
            "ztJjoQIVYfkvMlQNPqhPbtCWwgyMAVlFaXDRlwIabtCaOcHMlNomgcjvCFtpuogBsdLOPPVuDNtZNhsEQtQKccaxHEISZVYQUaNCrLWvwo"
            "FsOnlpuNBYyolQYOAwjpGvbLwrSC xYLAdJuROSlHPCIonMyxvl wjn  NRsYdcyGdTXMWGhJuXgyJpUnFjbFtwlDTxahhHakLkJnSBRWv"
            "nqkHauxDsXGnPYjHtuQGdlGfCsaWEGjczhkOllqxcGlBgTgcgAnvIMsSbOmontvMCkCgeFodCQgqNxYYAwzyXVcxFLnKFbVEMStyYxSepc"
            "UWvWvEDtZtDtiGKJywZSreBTiafhtpluRArWkPFdPVEAej"
        )
        b = (
            "AhPDveheBVSivLphpWVk QCLGzLGZxnfNSnajZUEzvBNTDvxKTbsdlpDOJcCRecyIMmGbivjCiBtSDOBFhAijhVCHwuGtzNooMnNOfNDUL"
            "FlTXHWbrLJZslYatPODwbXlZMDLcwdELwkfrwnzXjuMBGLykIOQqfoyUYnPsQFLwbdrgoQLpTIFBAcSrQOFG NPsfXzKhAWKdpdWOtKkcq"
            "qWEPySIdUoBrg gyucLJxTfFMylayhfZTOpnnwueyFO oUHxHo SwjlMWHxvkJavm DWNOYl aWBffHumlHcUIUaTuehmwInBGgMtunquX"
            "TuYICQEJVnvTvYpjwQVjnoJqXcjlWbEqkfKRDDxkiTauHADPCfeAnOqKCYvNkVgAVECcQGSOyHnsjWoYwKzohYTYNmMHEzYPzKllJDm pp"
            "yxqKthsIaPLFfdGqVTrMSkMjgMQMVtTxfVPrws TxqaZmlEhggURAJDGKNlfWcxIusgTJQ VZtZuJOj Wo ScfvXccYiYatWVFDFXiSZuo"
            "jzMEivCZRONlTdwuybimlRILFnWnhPcWcvigypMtWGfHpTKhzjJ ZAzyVkNWEewlQhlAnLDRkHxBKQnwsbxcpuHaAtVgCFEptJPJZFySwt"
            "yaugNZEvRuiuovY epFbFaCluWyzDe VTuFAZoiIFtKIpCdoBqQYyaulejSZDtNCRFiVduCgRjXsOABTdtToq THWaVz SitFOPxMGJIll"
            "tHyTHSM oPTWHFfwMQgSLsfUgLgwrE NOCvLhfLrKrZPp jyNvLcxwxPPqKQyAcQIeBUoQXYnMoWrQS tZsIuAFHvWGxafKqNXXvmMpOmY"
            "gUxDFDxnatxbJtujQSPkbuqRhEFFtbPVJtxqbKagOIxGCGYQdatxZtUKfHkUlrAl oAtTQMEYSuqTkKYxOVMkcCNllvxSIJEokjgwkLgHV"
            "wJxWUqhiNUIGsaMneROatCYtALjFQAModWPa pgTXsVreR"
        )
        self.assertTrue(is_anagram(a, b))

    def test_7(self):
        a = (
            "tITFzWyQIHWJPCnUOvSSURnSeFxWTo EIpsKmjoRTVgoVfNoipJqMPAKOcLpDCHQFCLIcmBWyjPNgUpuhwZxAxaxyLqVqtZJPburcvljvE"
            "AfbbRxdpJxBQfqaTfJMPGOGWADty GNqZT o SOAUVQYEYhxCYMiVYlSCTWMkXqlzdyeFJAeKQe XyEVahKjinxMMqDLXytXoMfGSrTHci"
            "CwofGZOwoKBuzlJxugya NgEEChGTtlVnPTLaObTYjZYYQ AIgixgJgazYZHrtKaEAtsifWwFrKXuOWZlEdqy Ne HWZBvpTRFAsXQKrrm"
            "xvwhLkgfObFZUKifKugFWFAlfkmjHxbtDIFaoTeOFOogdtUSuU TDwDWkPrkuMZcIuVU ksDywLBKdfWzopxuwLZvaQncUvqfxLkNwpKTu"
            "qSwqtrTpAxWDnSIuBgQYNKKSuHzfuDfXjLTQZrIVxhiIRXieVOtuLl lBpLahhJDOTSdQibMzfW vFkNNhWcOjMMV AZMhomYQqvPmEpln"
            "FUmVL  ocPwzqeCcMLmzuJzIWHHFiLUvPTZTtel IMKGnDyfTJHQHnOfHFRaQiafTV EyujnDNHBRHtqipFwTksIj PsUuJVkDtMsjNoKg"
            "ztJjoQIVYfkvMlQNPqhPbtCWwgyMAVlFaXDRlwIabtCaOcHMlNomgcjvCFtpuogBsdLOPPVuDNtZNhsEQtQKccaxHEISZVYQUaNCrLWvwo"
            "FsOnlpuNBYyolQYOAwjpGvbLwrSC xYLAdJuROSlHPCIonMyxvl wjn  NRsYdcyGdTXMWGhJuXgyJpUnFjbFtwlDTxahhHakLkJnSBRWv"
            "nqkHauxDsXGnPYjHtuQGdlGfCsaWEGjczhkOllqxcGlBgTgcgAnvIMsSbOmontvMCkCgeFodCQgqNxYYAwzyXVcxFLnKFbVEMStyYxSepc"
            "UWvWvEDtZtDtiGKJywZSreBTiafhtpluRArWkPFdPVEAej"
        )
        b = (
            "ZJMJTtfkmERGGvIWKRIzJrPfKHkMwzlGjitXeqxAJivHNYKxIAjGkUKmxemXJ QgrJVKWJFszpyxjzLLHTiTdVGAteKbLnqhAMijJYBPaf"
            " wvi ySUBbIKSTPCkSGLsRojXrMxgTdPEZVXMCFQkyeFHfNsaKgIOPJJMFulkEoDarrjaBclgXXtwUkdzlvroPQZZsPYjQngQYvGdoIADD"
            "CyzXXUzqgxaQaNkstVOSBaYmGjkctedizWoFdjowmRkaFRgzMoGcJDUPrDRGCmAQzTbvUNrwmAfjBlNoKCWkOfypuYDYTHNNwNZQFpaoZn"
            "TneWThtjEgpiasfFlgMlTVtuuOAYUmhUoCgQIHKQYwiuyIZSPiWZQZuhffWdakLxoSNERtnylOewHyrfGxNmYlKxSYFGXpzEqPSrbGLgfw"
            "rGWKfZptgbayxJHGVNDzjGJlgKgvlACQYbklNmEeRGpnSBqHFMxAah XjzETJJeMrZXanKqaqIGRAbRvRwG IXKNaZZNHOTYAqreLwURTO"
            "vkuAOgrcqhfVyBPBVGFuhLbsPVxWiXIfDujKuJOtU hQAXwSyEYkVAyMkgDfmMGFrKtviSPGJhVvVyrfGQRtaWGHHgvDa MtKrGOHqkErV"
            "dUTHnTFFEQqSZBiXanRytczOcKdPyzj KWILMUTgaRiWHx RaeJfoCKOAICCjFccFhmPFkBQSQkGQpFhNxfFKxzAcHpEDfeUkxVEGWonDN"
            "ITcIDBgDUqAFuJPQrrACllcezJCkHtUuuTDIZnjXeHJphohHYxgEdBJsWXOctUraGLPZjCpvClKCFtulwPmDHHmBYTDTaTcWjPQurtnAzD"
            "FrMggDtNOHSxKfZIKtIPMhZqHUZwlFwzlnKJoepKsvAbturSvbpxVIfryGNqVydO YOZMlpyrHZCfYFQlvsyRhYLdIKBsuDHruhXCCIfRm"
            "lRnSiFxQmBKloZMJynAjaDZuYLKwbfHWDYBFIzHiAOOeJO"
        )
        self.assertFalse(is_anagram(a, b))


if __name__ == "__main__":
    unittest.main()