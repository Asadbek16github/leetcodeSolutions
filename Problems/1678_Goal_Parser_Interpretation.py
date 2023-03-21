class Solution:
    def interpret(self, command: str) -> str:
        coun, res = '', ''

        for i in command:
            coun+=i
            if coun == 'G':
                res+='G'
                coun=''
            elif coun == '(al)':
                res+='al'
                coun=''
            elif coun == '()':
                res+='o'
                coun=''
        return res