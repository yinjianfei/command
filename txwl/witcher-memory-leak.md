## releate issues

https://github.com/spring-cloud/spring-cloud-gateway/issues/810
https://github.com/reactor/reactor-netty/issues/1286
https://github.com/reactor/reactor-netty/issues/1287
https://github.com/reactor/reactor-netty/issues/1254
https://github.com/reactor/reactor-netty/issues/1144
https://github.com/reactor/reactor-netty/issues/1130


## PrematureCloseException: Connection prematurely closed BEFORE response 
https://github.com/reactor/reactor-netty/issues/1038
https://github.com/spring-projects/spring-framework/issues/23249


## org.springframework.core.io.buffer.DataBufferLimitException: Exceeded limit on max bytes to buffer : 262144

https://github.com/spring-projects/spring-boot/issues/24417

## 增加debug日志
io.netty.util.internal.PlatformDependent to DEBUG 
io.netty=DEBUG
reactor.netty=DEBUG

## leak 检测机制 
https://www.jianshu.com/p/af5419b7dc0a
issue https://github.com/reactor/reactor-netty/issues/1408



## Not using exchange

The only reason to ever use exchange() is if you need to access the status and headers before any of the body has been read and that is rarely necessary and in any case then you take over handling the body and have to make sure the body is consumed in all cases which is something that retrieve() takes care of.



## outofdirectmemory

netty参数 https://caorong.github.io/2018/10/02/netty-%E5%8F%82%E6%95%B0%E6%95%B4%E7%90%86/
http://codefun007.xyz/view/article_detail.htm?id=783

https://dzone.com/articles/troubleshooting-problems-with-native-off-heap-memo

http://www.mastertheboss.com/other/java-stuff/troubleshooting-outofmemoryerror-direct-buffer-memory

netty 内存管理 https://www.cnblogs.com/rickiyang/p/13253203.html
-Dio.netty.allocator.maxOrder=4

jcmd <pid> VM.native_memory detail

//打对象 内存一直增加
https://github.com/netty/netty/issues/8317


##
-XX:+UseStringDeduplication
-XX:+UseG1GC


tar -chvf runtime.tar face_platform_runtime/infrastructure/ face_platform_runtime/config/ face_platform_runtime/shared/plugin_module/witcher

把runtime.tar scp到另外一个机器上
修改face_platform_runtime/shared/plugin_module/witcher
    /home/jianfei.yin/workspace/witcher/witcher-service/build/libs/witcher-service-0.0.1-SNAPSHOT.jar