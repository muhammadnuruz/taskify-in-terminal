from authentication import AuthenticationFunction

if __name__ == "__main__":
    authentication_status = AuthenticationFunction()
    if authentication_status:
        pass
    else:
        print("""|-----------|
|Good Bye :)|
|-----------|""")
        exit()
