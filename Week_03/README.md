学习笔记


1. 递归的实现、特性以及思维要点
重复点用一段逻辑

recursion

def recursion(level, param1, param2, ...):
    if level > MAX_LEVEL:
        process_result
        result 
    
    # process logic in current level 
    process(level, data...)

    # drill down
    self.recursion(level+1, p1, ...)

    # reverse the current level status if needed

思维要点：
1. 不要进行人肉递归
2. 寻找最小解决单元
3. 数学归纳法思维


2. 分治、回溯的实现和特性
分治、回溯是特殊的递归，
分治分成多个子问题，最后组合子问题的解
回溯 一种试错方式，符合条件的当成结果，不符合条件就跳过
最优重复性动态规划
最近重复性，


python 总结：
nnn = [1,2,3]
rst = nnn[4:]
结果为 []， 当取子数组时， index越界之间返回空数组