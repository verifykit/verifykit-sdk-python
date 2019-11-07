from VerifyKit import Verify

verify = Verify(server_key="baa0ce9020fa13f3cc50878a73cae9671f4e5021ef1dc2e2e132c055294432c")
verify.validation(session_id='zsq52wOOuqFGgVSg')

if verify.is_valid:
    print(verify.response())

elif verify.is_valid == False:
    print(verify.response())
