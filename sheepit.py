#This first Block is required as some weird behaviors with libtcmalloc appeared in the colab VM.
import os
os.environ["LD_PRELOAD"] = ""
!apt update
!apt remove libtcmalloc-minimal4
!apt install libtcmalloc-minimal4
os.environ["LD_PRELOAD"] = "/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4.3.0"
!echo $LD_PRELOAD
!apt update

#This is for Blender, GPU and sheepit.
!apt install libboost-all-dev
!apt install libgl1-mesa-dev
!apt install libglu1-mesa libsm-dev
!sudo add-apt-repository ppa:thomas-schiex/blender -y
!sudo apt-get update
!wget http://sheepit-renderfarm.com/media/applet/client-latest.php -O sheepit.jar
!java -jar sheepit.jar -login user -password password1 -ui text -gpu CUDA_0 -compute-method GPU -rendertime 30 #--verbose #ONLY FOR TESTING
#run the next command if you don't want ANY cell output
