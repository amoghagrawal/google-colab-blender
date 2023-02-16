#Info about the runtime
!cat /etc/os-release
!nvidia-smi
!nvcc --version

#This first Block is required as some weird behaviors with libtcmalloc appeared in the colab VM. 
import os
os.environ["LD_PRELOAD"] = ""
!apt update
!apt remove libtcmalloc-minimal4
!apt install libtcmalloc-minimal4
os.environ["LD_PRELOAD"] = "/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4" #no idea if libtcmalloc_minimal.so.4 or libtcmalloc_minimal.so.4.5.3 works better
!echo $LD_PRELOAD

#This is for Blender, GPU and sheepit.
!apt update
!apt install libboost-all-dev
!apt install libgl1-mesa-dev
!apt install libglu1-mesa 
!apt install libsm-dev
!apt install libxkbcommon0

#@title Setup
#@markdown Enter some dogshit 
username = "username" #@param {type: "string"}
key = "password" #@param {type: "string"}
computemethod = "GPU" #@param ["GPU", "CPU"] {allow-input: false}
downloadUrl = "https://www.sheepit-renderfarm.com/media/applet/client-latest.php"
#@markdown ---
!wget $downloadUrl -O client.jar

if computemethod == "CPU":
  !java -jar client.jar -ui oneLine/text -cache-dir /content/cache -compute-method $computemethod -login $username -password $key -ui text\n
else:
  !java -jar client.jar -ui oneLine/text -cache-dir /content/cache -compute-method GPU -gpu OPTIX_0 -login $username -password $key -ui text
