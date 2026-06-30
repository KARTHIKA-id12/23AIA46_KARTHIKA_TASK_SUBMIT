# vehicle maintenance scheduler microservice
# complete integration of logging middleware in this project

# data
# 1--time it take to do the repair
# 2--score repreesnts how important it is to complete the task

# choosing right set of tasks -- high efficiency
# challenge: to pick a combination of both
#  --total time spent does not exceed available mechanics-hours
#  --total score is as high as possible
# note: the no.tasks can be large so solution should be efficient

# resources:
# depot api(GET):
# http://4.224.186.213/evaluation-service/depots
# response

{
    "depots":[
        {
            "ID:1,
            "MechanicHours":135
        }
    ]
}

# vehicle api
# http://4.224.186.213/evaluation-service/vehicles

# response
{
    "vehicles":[
        {
            "TaskID":"264e---"
            "Duration":1,
            "Impact":5
        }
    ]
}

