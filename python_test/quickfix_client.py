import quickfix as fix

class MyApplication(fix.Application):
    def onCreate(self, sessionID):
        print(f"Session created: {sessionID}")

    def onLogon(self, sessionID):
        print(f"Logged on: {sessionID}")

    def onLogout(self, sessionID):
        print(f"Logged out: {sessionID}")

    def toAdmin(self, message, sessionID):
        pass

    def fromAdmin(self, message, sessionID):
        pass

    def toApp(self, message, sessionID):
        pass

    def fromApp(self, message, sessionID):
        try:
            print(f"Received message: {message}")
        except fix.UnsupportedMessageType as e:
            print(f"Unsupported message type: {e}")

def main():
    settings = fix.SessionSettings("client.cfg")
    application = MyApplication()
    storeFactory = fix.FileStoreFactory(settings)
    logFactory = fix.FileLogFactory(settings)

    initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)
    initiator.start()

    while True:
        try:
            input("Press Enter to send a test message or Ctrl+C to exit...\n")
            test_message = "8=FIX.4.4|35=8|49=Client|56=Server|34=1|11=Test123|54=2|"
            session = fix.Session.lookupSession(settings.get().getString("BeginString"))
            if session:
                fix.Session.sendToTarget(fix.Message(test_message), session.getSessionID())
        except (KeyboardInterrupt, EOFError):
            print("Exiting...")
            initiator.stop()
            break

if __name__ == "__main__":
    main()
