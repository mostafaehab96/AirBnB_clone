<div align="center">
  <h1>AirBnB clone - The Console</h1>
</div>

<img align="center" src="https://i.imgur.com/MQq3ABc.png](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230516T144858Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d4a69b3046e258c22945058febce7f3d660175ff21b919b242d884f30116f233" alt="Logo">

## Description

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

<img src="https://i.imgur.com/4biBGlj.png](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230516T144858Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3fe5d35beb3bbccfa32a8e1637606d5e3432da76fb487b4f2f693e27cb857d62" alt="Project">


## Console

* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)
* The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

## Commands

| Command     | Description | Format |
| ----------- |:------------| :-------|
| help        | Shows all allowed commands (documented and not) or gives information about a specific command. | `help` / `help <command>` |
| quit        | Exits the program. | `quit` |
| create      | Creates a new instance. | `create <classname>` |
| show        | Shows a specific instance by its `classname` and its `id`. | `show <classname> <id>` / `<classname>.show(id)`|
| all         | Displays all stored instances of a class or all stored instances by its `classname`. | `all` / `all <classname>` / `<classname>.all()`
| update      | Updates an instance (adds or modifies attributes) by its `classname`, `id`, `attribute` and its `value` to add/modify.  | `update <classname> <id> <attribute> <attrvalue>` / `<classname>.update(id, attribute name, attribute vlaue)` / `<classname>`.update(id, dictionary representation)` |
| destroy     | Deletes an instance by its `classname` and its `id`. | `destroy <classname> <id>` |
