# wiserheatingapi-examples
Sample scripts that use the Python Wiser Heating api from Angelo Santagata https://github.com/asantaga/wiserheatingapi

<h3>Heating Schedule Advance and Undo Advance</h3>

This extra capability requires two new library funtions **setRoomScheduleAdvance** and  **setRoomScheduleAdvanceUndo** that are in https://github.com/steversig/wiserheatingapi/wiserHeatingAPI/wiserHub.py and have had a pull request #23 issued to merge them upstream.

<h4>Advance</h4> advance.py sets the temperature of a room to the next set point. If you select **All** then all rooms are done. Need to quote rooms with spaces in their names such as "Bed 1"

eg **./advance.py Hall**
or **./advance.py All**
or **./advance.py "Bed 1"**

<h4>AdvanceUndo</h4> undoadvance.py reverts back to the current set point. If you select **All** then all rooms are done. Need to quote rooms with spaces in their names such as "Bed 1"

eg **./undoadvance.py Hall**
or **./undoadvance.py All**
or **./undoadvance.py "Bed 1"**

<h3>Heating Schedule Backup and Restore</h3>

<h4>Export</h4> export_schedules.py exports the current heating schedules for all rooms to a text file

eg **./export_schedules.py winter.txt**

**SAVE** your existing schedules **FIRST** and then modify them using the app to suit the season and then save them again with a new name

The export/import files are text but include long formatted Wiser Hub data structures

There are comments before each room in the export files to show you the **roomId** and **Name**. These are currently ignored during import.

<h4>Import</h4> import_schedules.py imports the current heating schedules for all rooms from a text file

eg **./import_schedules.py autumn.txt**

**WARNING**

If you add or remove rooms then you will have to recreate or modify the export files before they can be successfully imported.

The comments are there to help but its your responsibility to get it right. 

You should be able to comment lines out if you only want to restore the schedule for some of the rooms.

Importing is done by id number and does not currently check names ... or if the id now belongs to another room ...
