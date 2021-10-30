class PyRockRES:
  defaultConfig="[server]\nip=127.0.0.1\nlocalPort=19132\nbuffer=1024\n[debug]\nsendUDPBuffer=toCSV"
  disconnection="\033[1;31mCLIENT \033[33m{}\033[31m USING {} DISCONNECTED AT {}\033[0m"
  disconnectionLog="CLIENT {} USING {} DISCONNECTED AT {}\n"
  fail="\033[1;31mFailed!\033[0m"
  helpMessage="\nCommands:\n\t\"-h\" (or \"--help\"):\tShows this help message."
  newConnection="\033[1;32mCLIENT \033[33m{}\033[32m USING {} CONNECTED AT {}\033[0m"
  newConnectionLog="CLIENT {} USING {} CONNECTED AT {}\n"
  OK="\033[1;32mOK!\033[0m"
  serverStart="\033[34mSERVER ONLINE AT {}:{}\033[0m"