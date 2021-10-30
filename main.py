import socket, configparser, sys, os
print("\033[33mPy\033[34mCraft\033[0m v0.0\nmade by \033[31mel\033[34mbu\033[32mrg\033[0m")
print("Loading Resources...",end="")
import res
r=res.PyRockRES()
print(r.OK)
try:
  conf=os.environ['HOME']+"/.pyrockrc"
  if sys.argv[1]:
    print("DETECTED CL ARGUMENTS")
    if (sys.argv[1]=="-h" or sys.argv[1]=="--help"):
      print(r.helpMessage)
      quit()
    if (sys.argv[1]=="-c" or sys.argv[1]=="--config"):
      print("PyRock will load config from "+sys.argv[2])
      conf=sys.argv[2]
    if (sys.argv[1]=="-s" or sys.argv[1]=="--setup"):
      print("Making PyRock config...",end="")
      try:
        tf=open(os.environ['HOME']+"/.pyrockrc","w+")
        tf.write(r.defaultConfig)
        tf.close()
        print(r.OK)
      except:
        print(r.fail)
      print("Making Directories...",end="")
      try:
        os.mkdir(os.environ['HOME']+"/.pyrock/")
        os.mkdir(os.environ['HOME']+"/.pyrock/.debug/")
        print(r.OK)
      except:
        print(r.fail+" (They might already be there...)")
      quit()
except Exception as e:
  if e.__class__.__name__=="SystemExit":
    quit()
  conf=os.environ['HOME']+"/.pyrockrc"
print("checking if config exists...",end="")
try:
  cfg=open(conf,"r")
  cfg.close()
  print(r.OK)
except Exception as e:
  print(r.fail)
  if e.__class__.__name__=="FileNotFoundError":
    print("Error:\n\tType:\tFileNotFoundError\n\tErrno:\t"+str(e.errno)+"\n\tInfo:\t"+e.strerror+"\n\tFile:\t"+e.filename,file=sys.stderr)
rc=configparser.ConfigParser()
rc.read(conf)
try:
  if rc['debug']:
    print("DEBUG MODE")
    dbg={}
    if rc['debug']['sendUDPBuffer']:
      if rc['debug']['sendUDPBuffer']=="toCSV":
        dbg.udpio=open(os.environ['HOME']+"/.pyrock/.debug/udbBuffer","a+")
except:
  pass
print("Setting up socket...",end="")
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((rc['server']['ip'], int(rc['server']['localPort'])))
print(r.OK+'\n'+r.serverStart.format(rc['server']['ip'],rc['server']['localPort']))
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(int(rc['server']['buffer']))

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    print("\033[33mRECEIVED MESSAGE \"{}\" FROM \"{}\"\033[0m".format(message,address))
    if dbg.udpio:
      dbg.udpio.write("RECEIVED MESSAGE \"{}\" FROM \"{}\"".format(message,address))
    UDPServerSocket.sendto(str.encode("null"), address)