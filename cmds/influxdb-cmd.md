# influxdb

## http

> http://10.40.46.24:8086/query?q=SHOW+TAG+VALUES+FROM+%22txwl_spring_boot_percentile%22+WITH+KEY+%3D+%22uri%22+where+%22application%22%3D'resource-manager'&db=platform_monitor
>



SELECT SUM(val) FROM (SELECT mean(value) AS val FROM jvm_memory_max WHERE $timeFilter AND area = 'nonheap' AND "application" =~ /^$application$/ GROUP BY time($__interval),*) GROUP BY time($__interval) fill(null)


SELECT SUM(val) FROM (SELECT mean(value) AS val FROM jvm_memory_max WHERE time > now() - 1h AND area = 'nonheap' AND "application" =~ /witcher/ GROUP BY time(5s))



SELECT SUM(val) FROM (SELECT mean(value) AS val FROM jvm_memory_committed WHERE $timeFilter AND area = 'heap' AND service =~ /^$service/ GROUP BY time($__interval),*) GROUP BY time($__interval) fill(linear)

SELECT SUM(val) FROM (SELECT mean(value) AS val FROM jvm_memory_used WHERE $timeFilter AND area = 'heap' AND service =~ /^$service/ GROUP BY time($__interval),*) GROUP BY time($__interval) fill(linear)


SELECT SUM(val) FROM (SELECT mean(value) AS val FROM jvm_memory_max WHERE $timeFilter AND area = 'heap' AND application =~ /witcher/ GROUP BY time($__interval),*) where $timeFilter GROUP BY time($__interval) fill(linear)


SELECT mean("value") FROM "jvm_memory_used" WHERE ("application" =~ /^witcher/ AND "area" = 'heap') AND time > now() - 30m GROUP BY time(1s) fill(null)



SELECT mean("value") FROM "jvm_memory_max" WHERE ("area" = 'heap' AND "application" =~ /^$application$/) AND $timeFilter GROUP BY time(1s) fill(null)
SELECT mean("value") FROM "jvm_memory_committed" WHERE ("area" = 'heap' AND "application" =~ /^$application$/) AND $timeFilter GROUP BY time(1s) fill(null)
SELECT mean("value") FROM "jvm_memory_used" WHERE ("area" = 'heap' AND "application" =~ /^$application$/) AND $timeFilter GROUP BY time(1s) fill(null)

SELECT mean("value") FROM "jvm_memory_used" WHERE ("area" = 'nonheap' AND "application" =~ /^$application$/) AND $timeFilter GROUP BY time(1s) fill(null)