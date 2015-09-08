#!/bin/sh

if [ ! -n "$1" ]
then
        exit 1
fi

EMMC_DEVICE="/dev/mmcblk0"
RET_PARTX=$(/usr/sbin/partx -s ${EMMC_DEVICE})
PARTITION=${EMMC_DEVICE}p$(IFS=; echo $RET_PARTX | /bin/awk -v part=$1 'tolower($6) == part {print $1}')

if [ ${EMMC_DEVICE}p != ${PARTITION} ]
then
	/sbin/resize2fs -f ${PARTITION}
	exit 0
fi
exit 1
