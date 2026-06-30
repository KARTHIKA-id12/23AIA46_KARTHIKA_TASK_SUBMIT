# Notification System Design

# Stage 1

#Task 1: REST API design and structure to show notifications when logged in**

# Request
#Endpoint:`GET /api/v1/notifications`
Headers:
{
  "Authorization": "Bearer <JWT_TOKEN>",
  "Accept": "application/json"
}

# Response
Status Code: `200 OK`
Headers:
{
  "Content-Type": "application/json"
}

# body
{
  "status": "success",
  "data": {
    "notifications": [
      {
        "id": "1",
        "message": "result are out",
        "isRead": false,
        "createdAt": "004 3 4"
      }
    ]
  }
}
# this query is accurate but slow becaus there are more than 5 lakh rows
# we sort using orderby and desc




