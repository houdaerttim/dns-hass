from resettabletimer import ResettableTimer
import time
import datetime
import threading
from api_utils import escape_hatch 
## Variables


class Heater:
    state = False

def turn_off_heater(heater):
    heater.state = False
    return heater.state

def turn_on_heater(heater):
    heater.state = True
    return heater.state

def heating(temp_act):
    time.sleep(1)
    temp_act += 0.2
    return round(temp_act, 1)

def get_heater_status():
    return False
def get_temp_act():
    return 17.5
def get_temp_req():
    return 19.5
def turn_off_timer():
    print('turn off timer @ ' + str(datetime.datetime.now()))
def get_heater_start_time():
    return datetime.datetime.now()

def create_timer(heater):
    return threading.Timer(5, turn_off_timer)

def check_heating_needed(act, req):
    if act <= req:
        return True
    return False


def main():
    
    while 2 > 1:
                
        heater = Heater()
        heater.state = get_heater_status()
        temp_req = get_temp_req()
        temp_act = get_temp_act()
        #t = create_timer(heater)
        #print actuals:
        #print(f"Actuals: Req: {temp_req}; Act: {temp_act}; Heater = {heater.state} Timer = {t.is_alive()}")
        print(f"Actuals: Req: {temp_req}; Act: {temp_act}; Heater = {heater.state}")
        time.sleep(2)
        while (check_heating_needed(temp_act, temp_req)):
            if not heater.state:
                #turn_on_heater()
                heater.state = turn_on_heater(heater)
                heater_start_time = get_heater_start_time()
                #print('timer start @ ' + str(datetime.datetime.now()))
                #t.start()
            if heater.state: temp_act = heating(temp_act)
            print(f"Actuals: Req: {temp_req}; Act: {temp_act}; Heater = {heater.state}")
        
        #Stop heater
        print(f"Actuals: Req: {temp_req}; Act: {temp_act}; Heater = {heater.state}")
        
        #while now-time - heating_started-tim < 10: 
        #keep heater running avoiding multiple on/off's
        
    
def run():
    main()

run()


def create_timer(heater):
    return threading.Timer(5, turn_off_timer)
