from test.utils.env_variables import *
from bandwidth.model.call_state import CallState
from bandwidth.model.call_state_enum import CallStateEnum
from bandwidth.model.update_call import UpdateCall

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
                body = UpdateCall(state=CallStateEnum("completed"))
                get_call_response: CallState = self.calls_api_instance.get_call_state(BW_ACCOUNT_ID, callId, _return_http_data_only=False)
                if get_call_response[0].state == 'active':
                    self.calls_api_instance.update_call(BW_ACCOUNT_ID, callId, body, _return_http_data_only=False)
                elif get_call_response[0].state == 'complete':
                    self.callIdArray.remove(callId)
            self.callIdArray.clear()
        pass        