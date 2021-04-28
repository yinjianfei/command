#!/usr/bin/env python2
#coding: utf-8

import os
import json
import sys

def readConfig(config_path):
    if not os.path.exists(config_path):
        print("config file not exists: " + config_path)
        return None
    with open(config_path, 'rw') as f:
        content = json.load(f)
    return content

def getSubConfig(config, key_name):
    if config.has_key(key_name):
        return config[key_name]
    else:
        print(key_name + " missing field/type error")
        return None

def configureP2P(p2p_config, common_path):
    print("Configure P2P")
    file_path = os.path.join(common_path, "huiju_p2p_config.json")
    content = readConfig(file_path)
    content["config_based_direct_connection"]=p2p_config["config_based_direct_connection"]
    with open(file_path, 'w') as f:
        json.dump(content, f, sort_keys=True, indent=4, separators=(',', ':'))
    return True
# def configureImageStorage(image_storage_config, common_path):
#     print("Configure ImageStorage")
#     file_path = os.path.join(common_path, "huiju_image_storage_config.json")
#     content = readConfig(file_path)
#     content["p2p_config"]["p2p_http_request_service_ip"]=image_storage_config["p2p_config"]["p2p_http_request_service_ip"]
#     with open(file_path, 'w') as f:
#         json.dump(content, f, sort_keys=True, indent=4, separators=(',', ':'))
#     return True

def configureDynamicResource(dynamic_config, common_path):
    print("Configure DynamicResource")
    #do nothing
    return True

def configureDynamicData(dynamic_config, common_path):
    print("Configure DynamicData")
    file_path = os.path.join(common_path, "gather_dynamic_data_config.json")
    content = readConfig(file_path)
    track_config = getSubConfig(dynamic_config, "track_aggregation_config")
    if not track_config:
        return False
    content["image_flow_node_list"]=track_config["image_flow_node_list"]
    content["vehicle_node_list"]=track_config["vehicle_node_list"]
    # save config file
    with open(file_path, 'w') as f:
        json.dump(content, f, sort_keys=True, indent=4, separators=(',', ':'))
    return True
def configureDynamicMachine(dynamic_config, common_path):
    print("Configure DynamicMachine")
    file_path = os.path.join(common_path, "machine_config.json")
    content = readConfig(file_path)
    tool_config = getSubConfig(dynamic_config, "tool_config")
    if not tool_config:
        return False
    content["tool_config"]["p2p_node_ip"] = tool_config["p2p_node_ip"]
    # save config file
    with open(file_path, 'w') as f:
        json.dump(content, f, sort_keys=True, indent=4, separators=(',', ':'))
    return True
def configureKv(kv_config, common_path):
    print("Configure kv")
    file_path = os.path.join(common_path, "image_storage_client_config.json")
    content = readConfig(file_path)
    content["sources"]["kv"]["hobbit_kv_ip"] = kv_config["hobbit_kv_ip"]
    content["sources"]["kv2"]["hobbit_kv_ip"] = kv_config["hobbit_kv_ip"]
    # save config file
    with open(file_path, 'w') as f:
        json.dump(content, f, sort_keys=True, indent=4, separators=(',', ':'))
    return True


def main(config_path, common_path):
    print("starting config ...")
    config_path = os.path.join(config_path, "config.json")    
    config = readConfig(config_path)
    p2p_config = getSubConfig(config, "p2p_config")
    if not p2p_config:
        return -1
    dynamic_config = getSubConfig(config, "dynamic_aggregation_config")
    if not dynamic_config:
        return -1
    kv_config = getSubConfig(config, "kv_config")
    if not kv_config:
        return -1
    if not configureP2P(p2p_config, common_path):
        print("update P2P config failed!")
        return -1
    if not configureDynamicResource(dynamic_config, common_path):
        print("update DynamicResource config failed!")
        return -1        
    if not configureDynamicMachine(dynamic_config, common_path):
        print("update DynamicMachine config failed!")
        return -1   
    if not configureDynamicData(dynamic_config, common_path):
        print("update DynamicMachine config failed!")
        return -1    
    if not configureKv(kv_config, common_path):
        print("update kv config failed!")
        return -1
    print("update config success!")
    return 0

if __name__ == "__main__":
    rtn = main(sys.argv[1], sys.argv[2])
    if rtn != 0:
        sys.exit(1)
