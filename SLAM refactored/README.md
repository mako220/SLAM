Steps to run the program :

Libraries which need compilation :

*Pangolin
*G2opy

Dependencies needed to install libraries:

*sudo apt install libglew-dev
*sudo apt install cmake
*sudo apt install libpython3-dev
*sudo apt-get install ffmpeg libavcodec-dev libavutil-dev libavformat-dev libswscale-dev
*sudo apt install libeigen3-dev


Following downloads can be inside project folder -
Pangolin build instructions :

git clone https://github.com/uoip/pangolin.git
cd pangolin
mkdir build
cd build
cmake ..
make -j4 (replace 4 with number of CPU cores in your system)
cd ..
python3 setup.py install

G2opy instructions : 

git clone https://github.com/uoip/g2opy.git
cd g2opy
mkdir build
cd build
cmake -DPYBIND11_PYTHON_VERSION=3.6 .. (3.6 needs to be replaced with python version installed in your system which can be found by - python3 --version)
make -j4 (replace 4 by number of CPU cores in your system)
cd ..
python3 setup.py install

Additional libraries needed for running the program :
*sudo apt install python3-pip
*pip3 install opencv-python
*pip3 install numpy
*pip3 install scikit-learn
*pip3 install subprocess.run
*pip3 install PyOpenGL
*pip3 install pygame

run command -

python3 slam.py <video.mp4> (where video.mp4 is a video file)
