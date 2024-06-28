# MyRoutine
Demo Organisational App in JS and HTML

## Features
- Create Routines
- Save and Load Routines
- Run through a routine
- Count down timer for each step in a routine
- Get stars for completing steps in a routine
- Allows for Different users
- Display Number of stars

### Additional Potential Features
- Interesting animation
- Add icons to steps
- Translate to windows app/mobile app

## Structure and Technology
- Database to store user and routine data - SQL Server
- Server to run webpage and send and retrieve data to and from database - Python
- Webpage user interace - HTML, JS, and CSS

### Webpages
- Homepage (/app) - choose a user
- User Homepage (/app/{username}) - has options to create, run, delete routines and display total number of stars earnt
- Create routine (/app/{username}/routine/create) - option to create and save routine
- Edit routine (/app/{username}/routine/{routine-id}) edit or delete a routine
- Edit step (/app/{username}/routine/{routine-id}/steps/{step-id}) edit or delete a step
- Run routine (/app/{username}/routine/{routine-id}/run) - run a routine

## Data Structures
>Note that the names used are NOT final
### Database
User:
- ID
- Name
- Stars

Routine:
- ID
- Name
- User ID

Step:
- ID
- Name
- Order
- Time Alloted
- Routine ID

### Python Dicts
User:
- ID : int
- Name: string
- Stars: int
- Routines : dict list

Routine:
- ID : int
- Name : string
- Steps : dict list

Step:
- ID: int
- Order: int (zero-indexed)
- Name: string
- Time alloted : int (seconds)

### JSON/JS Object
User:
- ID : int
- Name: string
- Stars: int
- Routines : object array

Routine:
- ID : int
- Name : string
- Steps : object array

Step:
- ID: int
- Order: int (zero-indexed)
- Name: string
- Time alloted : int (seconds)

#### Example JSON
`{
    "User": {
        "ID" : 0,
        "Name" : "Micah",
        "Stars" : 5,
        "Routines" : [
            {
                "ID" : 1,
                "Name" : "Routine1",
                "Steps" : [
                    {
                        "ID" : 1,
                        "Order" : 0
                        "Name" : "Step 1",
                        "Time Alloted" : 10
                    },
                    {
                        "ID" : 2,
                        "Order": 1
                        "Name" : "Step 2",
                        "Time Alloted" : 30
                    }
                ]
            }
        ]
    }
}`

  
