# I02 — Session scenario matrix

| ID | Scenario | Expected behavior |
|---|---|---|
| S01 | Logon | establish configured logical session |
| S02 | Heartbeat | liveness during quiet periods |
| S03 | Test Request | prove peer responsiveness |
| S04 | high sequence | detect gap; request missing range |
| S05 | resend | replay recoverable messages |
| S06 | gap fill | advance non-replayed range by policy |
| S07 | duplicate | identify replay/lower sequence |
| S08 | reconnect | preserve logical session state |
| S09 | restart | restore persisted sequence/correlation |
| S10 | logon disagreement | recover or use governed procedure |
| S11 | New Order | produce business state response |
| S12 | Reject | preserve reason/correlation |
| S13 | Cancel | pending until venue confirms |
| S14 | Cancel/Replace | requested values not authoritative until accepted |
| S15 | Cancel Reject | actual venue state remains authoritative |
