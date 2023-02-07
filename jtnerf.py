import jittor
import os,sys,json,time
import argparse

parser = argparse.ArgumentParser(description="Jittor-NeRF")
parser.add_argument('--config',help = "Name Of Config")                   # 步骤三，后面的help是我的描述
args = parser.parse_args()   

if __name__ == "__main__":
    config_path = "./configs/"+args.config