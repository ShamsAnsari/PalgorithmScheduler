UML Class Diagram
```mermaid
classDiagram
    AccountManager *-- User
    User *-- Schedule
    Schedule *-- Event

    class Pickler{
        +bool file_exists
        +str file_path
        +save(self, account_manager)
        +load(self) AccountManager
    }

    class AccountManager{
        +list users
        +add_user(self, user)
        +check_credentials(self, userid, password) bool
        +get_user(self, userid, password) User
    }

    class User{
        +schedule: Schedule
        +str name
        +str userid
        +str password
        +__init__(self, name, userid, password)
        +__eq__(self, other)
    }

    class Schedule{
        +list events
        +add_event(self, event)
        +delete_event(self, event)
        +__str__(self) str
    }

    class Event{
        +str name
        +str description
        +int day
        +tuple<int, int> start
        +tuple<int, int> end
        +datetime time
        +__init__(self, name,day, start, end, description)
        +createKey(self) function~x~
    }
```

First Draft by Shams A.
Created using: 
https://mermaid-js.github.io/mermaid/#/classDiagram
