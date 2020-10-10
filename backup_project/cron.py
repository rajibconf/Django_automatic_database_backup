from django.core.management import call_command

def my_backup():
    try:
        call_command('dbbackup')
        call_command('mediabackup')
    except(ValueError):
        pass
 
