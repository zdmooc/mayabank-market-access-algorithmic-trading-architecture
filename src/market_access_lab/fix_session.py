from dataclasses import dataclass,field

@dataclass
class FixLikeSession:
    next_outgoing_seq:int=1
    expected_incoming_seq:int=1
    connected:bool=False
    sent_history:dict[int,str]=field(default_factory=dict)

    def connect(self): self.connected=True
    def disconnect(self): self.connected=False

    def send(self,payload):
        if not self.connected: raise RuntimeError("disconnected")
        seq=self.next_outgoing_seq
        self.sent_history[seq]=payload
        self.next_outgoing_seq+=1
        return {"seq":seq,"payload":payload}

    def receive(self,seq,payload):
        expected=self.expected_incoming_seq
        if seq==expected:
            self.expected_incoming_seq+=1
            return {"status":"ACCEPTED","seq":seq,"payload":payload}
        if seq>expected:
            return {"status":"SEQUENCE_GAP","expected":expected,"received":seq,
                    "resend_begin":expected,"resend_end":seq-1}
        return {"status":"DUPLICATE_OR_REPLAY","expected":expected,"received":seq}

    def replay(self,begin,end):
        return [{"seq":s,"payload":self.sent_history[s],"poss_dup":True}
                for s in range(begin,end+1) if s in self.sent_history]
