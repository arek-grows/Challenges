import unittest


def sock_pairs(sock_drawer: str) -> int:
    total = 0
    sock_set = set(sock_drawer)
    for sock in sock_set:
        total += sock_drawer.count(sock) // 2
    return total  # Put your code here


class TestSockPairs(unittest.TestCase):
    def test_0(self):
        self.assertEqual(1, sock_pairs("AA"))

    def test_1(self):
        self.assertEqual(2, sock_pairs("ABABC"))

    def test_2(self):
        self.assertEqual(4, sock_pairs("CABBACCC"))

    def test_3(self):
        self.assertEqual(1, sock_pairs("AACDE"))

    def test_4(self):
        self.assertEqual(0, sock_pairs("ACDBE"))

    def test_5(self):
        self.assertEqual(0, sock_pairs(""))

    def test_6(self):
        self.assertEqual(2, sock_pairs("ABABAB"))

    def test_7(self):
        self.assertEqual(2, sock_pairs("AAAAA"))

    def test_8(self):
        self.assertEqual(3, sock_pairs("AAACCBB"))

    def test_9(self):
        sock_drawer = "".join(
            [
                "SCQTXMTAOJFEUPEHEAFRGBRVUMCHPDGOHBKQUGSOLWFKJVBWMBJITCVSKJBYFSSXNCOIRIRTHFKBJPLQZNAMDUOJRUORMHCFHYGW",
                "TMNSCKTACRNILQAVWISNGKHFAMUKGZCGJOSPCIBOCAYSGTJQXSOLYWKRHAOCCGWVWMGFWRUVDGKQXHTMOVBWQBJSWDSGOOGYMYGL",
                "TQLWPEZTXUHTVYCAAPKYIDKWQPQMDEQSKSSUXCWRBGZOCXWVDFSSPESVPZWQQSGCTMKMHOMIVUXSLHHUZQSZZMSSFKBMHPSOWXUI",
                "CHTEIQQKKJPQEPLZVEQPEJFUOMQDZFIILOVXTZAEWDJHQWZJVJMEWMOCSIRJYPAXCTJRGNUKKRHKVRHWRIRQGZODZMNYBEYDMMCL",
                "DNBOMBJYQBBBDBLAYFKMLFZBYIYHCBDYFYQYBOASCCLYMAMYZVKDZUDIMXVRWZLLANUWVQKVMSXNEOJVEQZSWXUHCQGWPPEXEAFX",
                "FNBBTUUXPRWFLIQFDUWQIBLSQCBDEUGOINRLKLTHHARZGOBOSXIDOEVCVYKGRVTRAQHUBCYTJXMJAYZSNPPQFGPBRWXMQERHASIA",
                "ERKARPBGRJRPVOSWZWACUJEMSJQLGUPAWKLXVOSGQALRAQGPHCFWLYCFIBEMQJSGZFFULQGDKABILLBGELKULBPIVDFMXFGJBVKF",
                "HJWWDDXLMDTPZDZEWAAKUFAAREQXBQVBYDBUSHLVDNANGSTSTIBKIHSTAEYSCJPRWKBKOFLPITYABATATCOQBPFFQVOXNCKWIWHP",
                "OLQEXHJKPKBQMAWPCALHBCNFXUJTDTMYDOLNWEYOBRATHUECTFATPROADPGYMKEJZTRAXZECQCMNKYSEFWYIQTXKMMAFZHXPUMQV",
                "GPPSBADXQJYYSLVBKENVGMXHNKFESHDJAEVGDEUFAWUYSEVUDWCBXGRZTNXPYUOZGMDTLOZERTLYRAQPKZZSNPVFLDWJVDEDDZML",
                "GSQWJMMKHGLAYUCGGXDOSTORHLFIWVGDVSNBFFCNIFAEKXPEUOAQFEZITMBVYPFWEJHUZPQZQNZJOUJEXIBSZCSYEOBZNCLYUJMA",
                "TQCHEMYICUBCTTGENMQETRROQVAHGMPHUURQXUSTOOEXJNFZRRYUZDOVSUDPAFBUENBQZJBMCVIYDPWCWBOHBYSMIPERVYNASPCS"
            ]
        )
        self.assertEqual(594, sock_pairs(sock_drawer))

    def test_10(self):
        self.assertEqual(0, sock_pairs("Z"))



if __name__ == "__main__":
    unittest.main()