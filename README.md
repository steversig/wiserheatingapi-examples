# wiserheatingapi-examples
Sample scripts that work with the python wiserheatingapi from Angelo Santagata https://github.com/asantaga/wiserheatingapi

<h3>Heating Schedule Backup and Restore</h3>
These two scripts allow you to save and restore configurations for different times of the year and easily get them back

export_schedules.py exports the current heating schedules for all rooms to a text file
eg **./export_schedules.py winter.txt**

import_schedules.py imports the current heating schedules for all rooms from a text file
eg **./import_schedules.py autumn.txt**

**SAVE** your existing schedules **FIRST** and then modify them using the app to suit the season and then save them again with a new name

The export/import files are text but include long formatted Wiser Hub data structures

There are comments before each room in the export files to show you the **roomId** and **Name**. These are currently ignored during import.

**WARNINGS**
If you add or remove rooms then you will have to recreate or modify the export files before they can be successfully imported.

The comments are there to help but its your responsibility to get it right. 

You should be able to chop lines out if you only want to restore the schedule for some of the rooms.

Importing is done by id number and does not currently check names ... or if the id has changed ...
