def integerToRoman(n):
    a = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    b = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    s = ""
    for i in range(len(a))[::-1]:
        while n >= b[i]:
            s += a[i]
            n -= b[i]
    return s


print(integerToRoman(90))


'''
String integerToRoman(int n) {
    String[] a = new String[]{"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
    int[] b = new int[]{1,4,5,9,10,40,50,90,100,400,500,900,1000};
    String s = "";
    for (int i = a.length - 1; i >= 0; i--) {
        while (n >= b[i]) {
            s += a[i];
            n -= b[i];
        }
    }
    return s;
}
'''
