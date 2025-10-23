class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #create 2 helper methods, one to convert to binary and one to convert back to int
        #for every 1 found in binary sequence, add a power of 2 to the total result
        #while the result of the binary to integer is still greater than 0, we add a modular 2 to the result and floor divide the current number by 2
        #first we run a and b through integer conversion then we add then and run them through binary conversion

        def binaryToInt(binary: str) -> int:   
            res = 0
            for i in range(1,len(binary)+1):
                if binary[-i] == "1":
                    res += 2**(i-1)
            return res

        def intToBinary(num: int) -> str:
            res = ""
            if num == 0:
                return "0"
            while num != 0:
                res += str(num%2)
                num = num//2
            return res[::-1]

        return intToBinary(binaryToInt(a) + binaryToInt(b))

