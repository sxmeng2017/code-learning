class Solution():
    def combine(self,n,k):
        res = []
        def dsf(current, start):
            if (len(current)==k):
                res.append(current[:])
                #这里将长度符合的数列添加进去
                return
        for i in range(start, n+1):
            current.append(i)
            #这里的这句将当前数字添加进去
            dsf(current, i + 1)
            current.pop()
            #将位置弹出来一个
            #上面这个过程满足先找和1组合，然后找和2组合的思维过程
        dsf([],1)
        return res

