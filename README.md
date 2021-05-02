# COWIN_notification


This script is created for the purpose of sending notifications to a browser in Mobile/desktop environment when a vaccination appointment slot is available on the COWIN platform.
It uses a public API to get the status of the appointment. This script in its current state is meant for personal usage.

The notification service used is not owned/managed by me in any shape or form. For more info please go to notify.run
The script is pretty straight forward. 

Variables and usage:

district: a district code. Refer to districts.txt file to find your district code.
date_range: define for which weeks you want to search appoitments. 01-05-2021 means the week from 01-05-2021 to 07-05-2021
polling_rate: is defined in seconds(recommended: >20s). How often one would want to search. Please don't keep it very low as this is a public API for public welfare. Do not put any unecessary load on these APIs. I will not be responsible for anything which happens if you don't heed this warning. 



If you want to learn how to use the notify service, please refer to the guide at notify.run
