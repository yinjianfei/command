git clone git@gitlab.yitu-inc.com:main/ficus2.git
git submodule update --init --recursive common external inference/face_v2 inference/stem
bash ci/set_ficus_tools.sh
输出 export PATH="/home/ficusadmin/workspace/ficus2/.ficus/wrapper:$PATH"
*****将以上输出加入到你的 shell 配置文件中, 比如 ~/.bashrc, ~/.zshrc 等
*****机器上有多个 ficus2 时, 只需要将一个加入 PATH 即可, ficus2 命令会基于执行时 pwd 所在的 ficus2 操作

source ~/.bashrc