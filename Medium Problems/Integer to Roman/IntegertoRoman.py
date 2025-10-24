class Solution:
    def intToRoman(self, num: int) -> str:
        #create a dictionary that binds a value to a letter of a roman numeral
        #starting from the highest value of roman numeral, repeatedly subtract until the number becomes less than the value we are subtracting
        #if the number is still greater than the value, the add the corresponding roman numeral to the result
        #do it for each value in the dictionary
        #after all dictionary values have been finished, return the result that should contain all the roman numerals in the proper order
        
        dictionary = [ (1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),
                        (100,"C"),(90,"XC"),(50,"L"),(40,"XL"),
                        (10,"X"),(9,"IX"),(5,"V"),(4,"IV"),
                        (1,"I"), ]

        res = ""
        for val,rom in dictionary:
            while num >= val:
                num -= val
                res += rom
        return res
