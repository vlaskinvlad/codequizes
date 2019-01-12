def ab(a, b):
    def ab_aux(a,b, last):
        if a == 0: return "1"*b if b < 3 else raise ValueError("unable to make a string ")
        if b == 0: return "0"*a if a < 3 else raise ValueError("unable to make a string")
        if last == '1':
            return "00" + ab_aux(a-2,b,'0') if a > 2 else '0' + ab_aux(a-1,b,'0')
        if last == '0':
           return '11' + ab_aux(a, b-2,'1') if b > 2 else '1' + ab_aux(a, b-1, '1')
    return ab_aux(a, b, '0' if b > a else '1')


if __name__ == '__main__':
    print(ab(10,12))
