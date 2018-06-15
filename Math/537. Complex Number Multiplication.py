class Solution:
    def complexNumberMultiply_not_opt(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_plus = a.find('+')
        b_plus = b.find('+')

        a_i = a.find('i')
        b_i = b.find('i')

        res_a = complex(int(a[:a_plus]), int(a[a_plus+1:a_i]))
        res_b = complex(int(b[:b_plus]), int(b[b_plus+1:b_i]))

        res = res_a * res_b

        if res.real != 0:
            if res.imag < 0:
                res = str(res).replace('j','i').replace('(','').replace(')','')
                return res[:1] + res[1:].replace('-','+-')
            else:
                return str(res).replace('j','i').replace('(','').replace(')','')
        else:
            return "0+" + str(res).replace('j','i').replace('(','').replace(')','')


    def complexNumberMultiply(self, a, b):

        a_plus = a.find('+')
        b_plus = b.find('+')

        a_i = a.find('i')
        b_i = b.find('i')

        real_a = int(a[:a_plus])
        real_b = int(b[:b_plus])

        img_a = int(a[a_plus+1:a_i])
        img_b = int(b[b_plus+1:b_i])

        res_real = real_a * real_b - img_a * img_b
        res_img = real_a * img_b + img_a * real_b

        return str(res_real) + "+" + str(res_img) + "i"


sol = Solution()

print sol.complexNumberMultiply("20+22i", "-18+-10i")
print sol.complexNumberMultiply_not_opt("20+22i", "-18+-10i")



# O(1), O(1)