class Calculator:

    def eval(self,*args,**kwrags):

        if kwrags["operend"]=="+":

            print("sum",sum(args))

        elif kwrags["operend"]=="*":

            result=1

            for num in args:

                result=result*num

            print("product",result)

        elif kwrags["operend"]=="min":

            print("min",min(args))

        elif kwrags["operend"]=="max":

            print("max",max(args))

        elif kwrags["operend"]=="sort":

            print("sort",sorted(args))

cal_instance=Calculator()

cal_instance.eval(10,20,30,40,operend="+")

cal_instance.eval(10,20,30,40,operend="*")

cal_instance.eval(10,20,30,40,operend="min")

cal_instance.eval(10,20,30,40,operend="max")

cal_instance.eval(10,20,30,40,operend="sort")
