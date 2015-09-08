#!/bin/sh

echo -e "[${_G}set cpufreq governor${C_}]"
# Set default cpufreq governor
echo slp > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
if [ $? -ne 0 ];then
        echo -e "\t[${_Y}slp not exits, set default ondemand${C_}]"
        echo ondemand > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
fi
