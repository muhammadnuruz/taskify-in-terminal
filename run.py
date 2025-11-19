from authentication import AuthenticationFunction

if __name__ == "__main__":
    auth = AuthenticationFunction()
    if auth:
        print("Welcome! Authentication successful!")
    else:
        print("|-----------|\n|Good Bye :)|\n|-----------|")
