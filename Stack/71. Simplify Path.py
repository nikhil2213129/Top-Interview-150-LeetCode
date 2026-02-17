class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        values = path.split("/")
        directory = []
        for i in values:
            if not i or i == ".":
                continue
            if i == "..":
                if directory:
                    directory.pop()
            else:
                directory.append(i)
        finalpath = "/"+"/".join(directory)
        return finalpath

            
