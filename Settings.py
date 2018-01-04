import random

xx=True
xxx=False
debugLevel1=xxx
debugLevel2=xxx
debug=xxx
debugDetail=False
debugTimer=xxx
sleepTime =0.0

"""jobCreator Constants"""
#capacity = 20 ########################################################
capacity = 80
loadMin = 0.6 #########################################################
loadMax= 0.0
CosFluctuate= 0.22 ####################################################
avgSysLoad=1.1
NumberOfTimeInterval=100 ##############################################
eachTimeInterval=10
maxRunTime=3 ###########################################################
vmCores = [2,4,8,16] ###################################################
deadLineMin =2 #########################################################
deadLineMax=4
maxVMsize =16
maxVMoptions=3 #########################################################
minScaleFactor=1.4 #####################################################
maxScaleFactor=2
switchCaseDic={ 2: random.randint(1,2), 4: random.randint(1,2), 8: 1, 16: 1, }


"""Scheduler Constants"""
#resources = "~input/resources.txt"
#resources = [[4,8,0,0,1],[4,8,0,0,2],[2,4,0,0,3],[2,4,0,0,4]]
#resources = [[8,32,0,0,1],[8,32,0,0,2],[4,8,0,0,3],[4,8,0,0,4],[2,4,0,0,5],[2,4,0,0,6],[2,4,0,0,7],[2,4,0,0,8]]
resources = [[16,64,0,0,1],[16,64,0,0,2],[8,32,0,0,3],[8,32,0,0,4],[4,8,0,0,5],[4,8,0,0,6],[4,8,0,0,7],[4,8,0,0,8],[2,4,0,0,9],[2,4,0,0,10],[2,4,0,0,11],[2,4,0,0,12],[2,4,0,0,13],[2,4,0,0,14],[2,4,0,0,15],[2,4,0,0,16]]
duration=NumberOfTimeInterval*eachTimeInterval+400 ##################################################### additional for last time jobs dead
MEO=True
firstOptionOnly=False
lastOption=False
bidDegree=100



"""sampleJob #            [s,[[e1],[e2],[e3]],d,b,id],"""
#jobList = "~input/jobList.txt"
testMEO=[   [0,[[1,2,21],[2,2,11],[4,2,7]],23,15,1],#26
            [0,[[2,2,27],[4,2,15]],29,10,2],#29
            [0,[[1,4,20],[2,4,11],[4,4,6]],24, 28,3],
            [10, [[1,4,7], [2,4,4], [4,4,3]], 10, 4,4],
            [10, [[1,8,9], [2,8,5]], 14, 1,5],
            [10, [[1,2,17], [2,2,10]], 27, 14,6],
            [20, [[1,4,15], [2,4,11]], 16, 6,7],
            [20, [[2, 2, 19], [2, 8, 7]], 22, 8,8],
            [20, [[1, 4, 20], [2, 4, 12]], 24, 9,9],
            [20, [[4, 2, 8], [4, 4, 5]], 21, 5,10],
            [20, [[2, 4, 10], [1, 4, 6]], 16, 4,11],   #do no takeplace in 20 let id 9 scale
        ]
testFirst=[   [0,[[1,2,21],[2,2,11],[4,2,7]],23,5,1],#26
            [0,[[2,2,27],[4,2,15]],29,10,2],#29
            [0,[[1,4,20],[2,4,11],[4,4,6]],24, 8,3],
            [10, [[1,4,7], [2,4,4], [4,4,3]], 10, 4,4],
            [10, [[1,8,9], [2,8,5]], 14, 8,5],
            [10, [[1,2,17], [2,2,10]], 27, 4,6],
            [20, [[1,4,15], [2,4,11]], 16, 6,7],
            [20, [[2, 2, 19], [2, 8, 7]], 22, 8,8],
            [20, [[1, 4, 20], [2, 4, 12]], 24, 9,9],
            [20, [[4, 2, 8], [4, 4, 5]], 21, 5,10],
            [20, [[1, 4, 10], [2, 4, 6]], 16, 4,11],
        ]
