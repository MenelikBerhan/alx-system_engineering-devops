# Description for Scripts in `0x01-shell_permissions` Directory

- **0-iam_betty** __Strong__ Switches the current user to the user `betty`.
- **1-who_am_i** __Strong__ Prints the effective username of the current user.
- **2-groups** __Strong__ Prints all the groups the current user is part of.
- **3-new_owner** __Strong__ Changes the owner of the file `hello` to the user `betty`.
- **4-empty** __Strong__ Creates an empty file called `hello`.
- **5-execute** __Strong__ Adds execute permission to the owner of the file `hello`.
- **6-multiple_permissions** __Strong__ Adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.
- **7-everybody** __Strong__  Adds execution permission to the owner, the group owner and the other users, to the file `hello`.
- **8-James_Bond** __Strong__ Sets the permission to the file `hello` as follows:
       * Owner: no permission at all
       * Group: no permission at all
       * Other users: all the permissions
- **9-John_Doe** __Strong__ Sets the mode of the file `hello` to this: ```-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello```
- **10-mirror_permissions** __Strong__ Sets the mode of the file `hello` the same as `olleh`’s mode.
- **11-directories_permissions** __Strong__ Adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.
- **12-directory_permissions** __Strong__ Creates a directory called `my_dir` with permissions 751 in the working directory.
- **13-change_group** __Strong__ Changes the group owner to `school` for the file `hello`.
- **100-change_owner_and_group** __Strong__ Changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.
- **101-symbolic_link_permissions** __Strong__ Changes the owner and the group owner of a symbolic link file `_hello` to `vincent` and `staff` respectively.
- **102-if_only** __Strong__ Changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.
- **103-Star_Wars** __Strong__ Play the StarWars IV episode in the terminal.
