车辆 
rtsp://10.10.67.124:8554/video/car/15.185.231.221_1min.264
rtsp://10.40.120.38:8554/video/15.185.116.252.264
rtsp://10.40.120.38:8554/video/15.185.116.219.264


[
    {
        "id": "2222",
        "taskType": "REALTIME_VIDEO",
        "device": "4f25709b755b4cf1a88ed3ada4c3286c@TFS4202002140095",
        "dataSinkEndpoints": [
            {
                "protocol": "OneApiEndpoint",
                "url": "http://10.10.24.132:30084/v1/dynamicRepos/subjects",
                "trackFrameSelector": [
                    "EXIT"
                ]
            }
        ],
        "params": {
            "recgObjectType": "VIDEO_FACE_RECOGNITION",
            "enableDrawer": false,
            "enableDrawerImage": false,
            "recognitionMode": "1111",
            "sourceEndpoint": {
                "protocol": "RtspEndpoint",
                "url": "rtsp://10.10.67.124:8554/video/car/15.185.231.221_1min.264",
                "trackFrameSelector": null
            }
        },
        "enabled": true
    }
]