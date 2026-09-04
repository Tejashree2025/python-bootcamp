"""1108. Defanging an IP Address
Solved
Easy
Topics
premium lock icon
Companies
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"""


class Solution:
    def defangIPaddr(self, address: str) -> str:

       return address.replace(".","[.]")


    #2nd code without using bulit-in function

    ans =""

        for i in address:
            if i!=".":
                ans+=i
            else:
                ans+="[.]"
        return ans