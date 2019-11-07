from VerifyKit import Verify

verify = Verify(server_key="{SERVER-KEY}")
verify.validation(session_id='{SESSION-ID}')

if verify.is_valid:
    print(verify.response())

elif verify.is_valid == False:
    print(verify.response())
