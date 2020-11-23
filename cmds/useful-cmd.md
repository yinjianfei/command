# useful

# network

iftop

# disk

ddstat
iotop

public static void main(String[] args) throws IOException, YituException {
        Tool tool = new Tool();

            InputStream inputStream = new FileInputStream(new File("/home/ficusadmin/workspace/frontend/ryan_test/src/main/resources/camera_device_excel/cn.xls"));


            List<CameraDevice> devices = tool.excelToDeviceList(inputStream, "cn", true, false);
            ObjectMapper objectMapper = new ObjectMapper();
            objectMapper.setSerializationInclusion(JsonInclude.Include.NON_DEFAULT);

            String string = objectMapper.writeValueAsString(devices);
            System.out.println(string);


//
//        String devices = "[{\"name\":\"飓风1\",\"url\":\"rtsp://10.40.46.23:5880/proxyStream\",\"checkpoint_type\":1,\"identification_type\":2,\"type\":0,\"user_name\":\"test\",\"password\":\"2134\",\"meta\":{\"GEOGRAPHY_X\":\"121.4704241\",\"GEOGRAPHY_Y\":\"31.2356648\"},\"rec_params\":{\"video_resolution_mode\":0},\"administrative_division\":{\"province\":\"31\",\"city\":\"01\",\"county\":\"05\",\"town\":\"\",\"village\":\"\",\"custom_region_id\":-1,\"custom_region_name\":\"\"},\"administrative_display_name\":{\"province_name\":\"上海市\",\"city_name\":\"市辖区\",\"county_name\":\"长宁区\",\"town_name\":\"\",\"village_name\":\"\",\"custom_region_name\":\"\"},\"custom_fields\":{}},{\"name\":\"飓风2\",\"url\":\"rtsp://10.40.46.23:5881/proxyStream\",\"checkpoint_type\":1,\"identification_type\":2,\"type\":0,\"meta\":{\"GEOGRAPHY_X\":\"121.503941\",\"GEOGRAPHY_Y\":\"31.2646857\"},\"rec_params\":{\"video_resolution_mode\":0},\"administrative_division\":{\"province\":\"31\",\"city\":\"01\",\"county\":\"05\",\"town\":\"\",\"village\":\"\",\"custom_region_id\":-1,\"custom_region_name\":\"\"},\"administrative_display_name\":{\"province_name\":\"上海市\",\"city_name\":\"市辖区\",\"county_name\":\"长宁区\",\"town_name\":\"\",\"village_name\":\"\",\"custom_region_name\":\"\"},\"custom_fields\":{}},{\"name\":\"飓风3\",\"url\":\"rtsp://10.40.181.34:6301/proxyStream\",\"checkpoint_type\":2,\"identification_type\":3,\"type\":0,\"meta\":{\"GEOGRAPHY_X\":\"121.4644159\",\"GEOGRAPHY_Y\":\"31.2550742\"},\"rec_params\":{\"video_resolution_mode\":0},\"administrative_division\":{\"province\":\"31\",\"city\":\"01\",\"county\":\"05\",\"town\":\"\",\"village\":\"\",\"custom_region_id\":-1,\"custom_region_name\":\"\"},\"administrative_display_name\":{\"province_name\":\"上海市\",\"city_name\":\"市辖区\",\"county_name\":\"长宁区\",\"town_name\":\"\",\"village_name\":\"\",\"custom_region_name\":\"\"},\"custom_fields\":{}}]";
//        ObjectMapper objectMapper = new ObjectMapper();
//        CollectionType collectionType = objectMapper.getTypeFactory().constructCollectionType(List.class, CameraDevice.class);
//        List<CameraDevice>  deviceList = objectMapper.readValue(devices, collectionType);
//
//        OutputStream outputStream = new FileOutputStream(new File("/home/ficusadmin/workspace/frontend/ryan_test/src/main/resources/camera_device_excel/cn.xls"));
//
//        outputStream = tool.deviceListToExcel(deviceList, outputStream, "cn", true, false);
//        outputStream.flush();
//        outputStream.close();
    }