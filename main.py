from auth.authentication import AuthenticationFunction
from tasks.manage import taskManager

if __name__ == "__main__":
    while True:
        auth, msg, user, gmail = AuthenticationFunction()
        if auth:
            print("Welcome! Authentication successful!")
            while True:
                status = taskManager(user, gmail)
                if not status:
                    break
        else:
            print("|-----------|\n|Good Bye :)|\n|-----------|")
            break
