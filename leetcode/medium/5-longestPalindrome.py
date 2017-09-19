import sys

class Solution(object):
	'''
    def longestPalindrome(self, s):
        
        if s == ''.join(list(reversed(list(s)))):
        	return s

        for i in range(len(s) - 1, -1, -1):
        	palindrome = self.findPalindrome(s, i)
        	
        	if palindrome:
        		return palindrome
        	

        return None
    '''
	def findPalindrome(self, s, x):

		for i in range(1 + len(s) - x):#list(reversed(range(1 + len(s) - x))):
			#print s, s[i:x], ''.join(list(reversed(list(s[i:x])))), i, x
			if s[i:x] == ''.join(list(reversed(list(s[i:x])))):
				return s[i:x]
			#print i
			x += 1

		return None
	#print s, x, len(s) - x

	def longestPalindrome(self, s):
		if len(s)==0:
			return 0

		maxLen = 1
		start = 0
		for i in xrange(len(s)):

			if i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
				start = i - maxLen - 1
				maxLen += 2
				continue


			if i-maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
				start = i-maxLen
				maxLen += 1


		return s[start:start+maxLen]


s = Solution()
#abb
#ss = 'babad'
ss = 'ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy'
res = s.longestPalindrome(ss)
print res