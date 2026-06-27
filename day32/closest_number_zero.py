class ClosestNumberToZero:


    def solution(self,lst):

        closest=lst[0]

        for num in lst:

            if abs(num)<abs(closest):

                closest = num

        if closest <0 and abs (closest) in lst:

            print(abs(closest))

        else:

            print(closest)

cls=ClosestNumberToZero()

cls.solution([1,2,3,-1,-2])
