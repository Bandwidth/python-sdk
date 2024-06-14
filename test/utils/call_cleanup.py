import time
from bandwidth.exceptions import NotFoundException
from test.utils.env_variables import *
from bandwidth.models.call_state import CallState
from bandwidth.models.call_state_enum import CallStateEnum
from bandwidth.models.update_call import UpdateCall

TEST_SLEEP = 3
MAX_RETRIES = 10

def callCleanup(self):
        """
           Whenever we create an actual call, we'll add the call_id to the callIdArray. Then when the integration test is done, as part of tearDown we'll:
                Do a get to check is the call status is still active
                    If so, update to completed to end the call
                    If not, pop that callID off the array
                Once we go through the whole array, we clear the array so it's empty for the next integration test.
           if the status is active, send UpdateCall to change to completed
        """

        if len(self.callIdArray) > 0:
            for callId in self.callIdArray:
                retries = 1
                repeat = True
                body = UpdateCall(state=CallStateEnum("completed"))

                while (repeat and retries <= MAX_RETRIES):
                    try:
                        get_call_response: CallState = self.calls_api_instance.get_call_state(BW_ACCOUNT_ID, callId)
                        if get_call_response.state == 'active':
                            self.calls_api_instance.update_call(BW_ACCOUNT_ID, callId, body)
                        elif get_call_response.state == 'complete':
                            self.callIdArray.remove(callId)

                        # We succeeded, break the loop
                        repeat = False
                    except NotFoundException:
                        retries += 1
                        print(f"Call ID was not registered, trying again attempt {retries}")
                        time.sleep(TEST_SLEEP)

            self.callIdArray.clear()
        pass
